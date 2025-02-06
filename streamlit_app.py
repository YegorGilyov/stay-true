__import__('pysqlite3')
import sys
sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')

import streamlit as st

import chromadb
from chromadb.config import Settings
import httpx
from sentence_transformers import SentenceTransformer
from openai import OpenAI
import pandas as pd
from documents import DOCUMENTS

def chunk_text(text, chunk_size=1000, overlap=100):
    """Split text into overlapping chunks"""
    chunks = []
    start = 0
    text_length = len(text)
    
    while start < text_length:
        end = start + chunk_size
        # If we're not at the last chunk, try to break at a period
        if end < text_length:
            # Look for the last period in the chunk
            last_period = text[start:end].rfind('.')
            if last_period != -1:
                end = start + last_period + 1
        
        chunks.append(text[start:end])
        start = end - overlap
    
    return chunks

def get_llm_response(claim: str, doc: str) -> str:
    client = OpenAI(
        api_key=st.secrets["openai_key"]
    )
    
    prompt = f"""Based on the following document, please tell if the claim contains something that explicitly contradicts the document."
    If the claim is focused on a different topic, answer 'Not relevant'.
    If the claim does not contradicts the document, answer 'No contradiction'.
    If the claim contradicts the document, answer 'Contradiction', and explain why in brackets.

    Document:
    {doc}

    Claim: {claim}
    """
    
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that answers questions based on the provided context."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=500
    )
    
    return response.choices[0].message.content

# Create a proper embedding function class
class BetterEmbeddingFunction:
    def __init__(self):
        # Load a pre-trained model that understands semantic meaning
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        
    def __call__(self, input: list[str]) -> list[list[float]]:
        # Convert text to semantic embeddings
        embeddings = self.model.encode(input)
        return embeddings.tolist()

# Create a persistent client with increased timeout
chroma_client = chromadb.Client(Settings(
    persist_directory="./chroma_db",
    anonymized_telemetry=False,
    allow_reset=True,
    is_persistent=True
))

# Delete collection if it exists
try:
    chroma_client.delete_collection(name="my_collection")
except Exception:
    pass  # Collection might not exist, that's ok

# Create new collection with local embedding function
collection = chroma_client.create_collection(
    name="my_collection",
    embedding_function=BetterEmbeddingFunction()
)

st.title("Stay true!")

st.subheader("Step 1: uploading documents")

uploaded_files = st.file_uploader("Choose files", accept_multiple_files=True, type=['txt'])

st.subheader("Step 2: making a claim")

claim = st.text_input("Enter your claim:")

if uploaded_files and (claim !=""): # and not st.session_state.processed_docs:
    try:
        st.subheader("Step 3: adding documents to the vector database")
        # Process and add each document
        for i, uploaded_file in enumerate(uploaded_files):
            doc = uploaded_file.getvalue().decode("utf-8")
            chunks = chunk_text(doc)
            collection.add(
                documents=chunks,
                ids=[f"doc_{i}_chunk_{j}" for j in range(len(chunks))],
                metadatas=[{"source": f"document_{i}", "title": doc.strip().split('\n')[0]} for _ in chunks]
            )
            st.write(f"Added {len(chunks)} chunks from file {uploaded_file.name}")

        st.subheader("Step 4: search for relevant documents")

        results = collection.query(
            query_texts=[claim],
            n_results=20,
            where={"source": {"$ne": ""}},  
            include=["metadatas", "distances", "documents"]
        )
        
        # Keep track of seen sources
        seen_sources = set()
        diverse_results = {
            'documents': [],
            'distances': [],
            'ids': [],
            'metadatas': []
        }
        
        # Filter results to include only one chunk per source document
        for i, (doc, distance, doc_id, metadata) in enumerate(zip(
            results['documents'][0],
            results['distances'][0],
            results['ids'][0],
            results['metadatas'][0]
        )):
            source = metadata['source']
            if (source not in seen_sources) and (len(diverse_results['documents']) < 3):
                seen_sources.add(source)
                diverse_results['documents'].append(doc)
                diverse_results['distances'].append(distance)
                diverse_results['ids'].append(doc_id)
                diverse_results['metadatas'].append(metadata)
                st.write(f"{metadata['title']} / distance: {distance:.4f}")

        st.subheader("Step 5: determining if there are discrepancies")

        for i, (doc, distance, doc_id) in enumerate(zip(
            diverse_results['documents'],
            diverse_results['distances'],
            diverse_results['ids']
        )):
            source = diverse_results['metadatas'][i]['source']
            title = diverse_results['metadatas'][i]['title']
            llm_response = get_llm_response(claim, doc)
            
            st.write(title)
            st.write(llm_response)
            st.write("---")

    except httpx.ReadTimeout as e:
        print("Timeout error occurred. Try using a VPN or check your internet connection.")
        print(f"Error details: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")