DOCUMENTS = [
    """
    Understanding Custom Fields

    Yegor Gilyov Oct 4, 2023—Nov 24, 2023

    We introduced Custom Fields in 2015, and back then it was a game changer. With Custom Fields, you can extend your tasks with attributes that are specific for your domain, or your project, or your process, or your team. It was one of the early steps from an online project management tool to a collaborative work management platform. And we actually pioneered this. For example, Asana rolled out their implementation of Custom Fields about a year later, in 2016.

    Being an extremely powerful capability, Custom Fields are also believed to be one of the most complicated parts of the Wrike conceptual model. In this document I’m trying to shed some light on the difficulties you may face trying to understand Custom Fields. It doesn’t pretend to be a comprehensive overview, but hopefully it can serve as a good starting point.
    Custom Fields in Wrike are first-class citizens
    The very first thing you need to know about Custom Fields is that in most cases they don’t belong to the context where you create them and where you work with them. 

    Imagine you open a project in Table view and add a new column by creating a new Custom Field. You might think that you simply add a column to this specific view of this specific project, but in reality your operation has much wider implications:

    This new field will appear in all work items contained in that project, at any level of hierarchy. 
    This new field can be turned on in any other view of that project, and also in any view of projects and folders contained in that project, and also (that might surprise you) in any view of projects and folders above that project in hierarchy.
    The potential scope of using that field isn’t limited to the points above, as it can be easily added to any other project, folder, or Custom Item Type within this space or even within the entire account (if you made that field account-level). In case one field is used in multiple places, it’s important to remember that changes in the field configuration immediately affects all those places. 

    Let me stress it one more time. You may see a Custom Field in your project as a column in Table view and assume that it belongs to that project. Or you may see a Custom Field in Work Item View of an item of a specific type (Custom Item Type) and assume it belongs to that type. In both cases such assumptions will be wrong. Custom Fields in Wrike are first-class citizens — they don’t belong neither to containers (projects or folder) nor to types. They might be only associated with such containers and types. In most platforms that allow you to customize their information models fields don’t behave that way. There are reasons why Wrike is different, and there are certain capabilities unlocked by this peculiarity. But as it’s counter-intuitive, it’s really important to understand it from the very beginning. 

    Now I hope I have your full attention and you are well prepared to dive into the details.
    Two levels of management: account and space
    You may ask, if Custom Fields belong neither to projects nor to Custom Item Types, what on earth are places they belong to? Certainly they can’t exist just in the void. The answer is that being elements of configuration, Custom Fields akin Workflows, Custom Item Types, and Blueprints. That means that a Custom Field belongs to either the entire account, or one of the spaces. Respectively, we call them account-level or space-level Custom Fields.

    Initially we had account-level Custom Fields only, and everyone was able to create a new field. As a result, accounts were polluted with dozens and even hundreds of redundant Custom Fields. That's why we decided to introduce space-level Custom Fields and by default a new field will be a space-level one, even if you have permissions to make it account-level. The idea is that every team or department can create fields they need to use in their space without bloating the custom field library at the account level. 

    Fields can be moved between those two categories. You can take a space-level field and make it account-level, and vice versa. 

    Bottomline: space-level Custom Fields can be used in the space they belong to, account-level Custom Fields can be used anywhere.
    Two paradigms of configuration: location-based and type-based
    Having figured out where Custom Fields belong, let’s shed light on their complicated relationships with locations (projects and folders) and Custom Item Types.
    Location-based configuration
    Custom Fields added to a project or a folder appear in all items downstream the work graph. We call it CF inheritance. It makes perfect sense from the perspective of Table view. As you can see all nested items in a hierarchical table, every new column manifests as a field in every row of that table. For example, when you add a field “Cost” to a work breakdown structure of your project, you do expect this field to be added to every element of that structure, across all levels.

    With that being said, CF inheritance is believed to be a big point of frustration as oftentimes work items become polluted with Custom Fields unintentionally inherited from the higher levels of Work Graph. For example, when you simply tag your project by some folder, normally you wouldn’t expect that suddenly all the items in your project become polluted with fields from that folder (and/or other folders or projects that contain that folder), but that’s how CF inheritance works, and it cannot be opted out of, even if you hate it and don’t think you need it. In real life pretty often we can’t even determine where inherited fields come from: you may see a task with some fields but you may have no idea in which folder or project above this task in the hierarchy those fields have been added.

    Another problem with CF inheritance is that given that usually there are multiple sources from where fields might be inherited, it’s practically impossible to customize the order of how those fields are displayed in the work item view. We don’t have a better option than to show them sorted alphabetically.
    Type-based configuration
    In order to address the problems highlighted above, we introduced Custom Item Types as a new (and hopefully better) way to manage configuration. In CIT editor, you can define a set of Custom Fields for this type, and all work items based on this type will have that set of fields. 

    Given that one work item can be based on one type only, and (so far) there is no such thing as CIT inheritance, type-based configuration works in a more straightforward and predictable way than the location-based one. When you add a field to your “Bug” type, this field is added to all items of that type — it’s as simple as that. 

    In the Work Item View, we show fields configured in CITs in the main section in the order defined in CIT editor (also some of the fields might be promoted as “top” fields to be shown at the very top), and all other fields (inherited ones) in the “More fields” section that can be collapsed.

    Bottomline: Now we see that two paradigms (location-based and type-based) of managing Custom Fields configuration compete with each other. Practically you can not use only type-based configuration, because every time when you add a field as a column in Table view, it’s added to this location. 
    The difference between “Belongs to” and “Added to”
    Just to summarize:

    A Custom Field may belong either to a space or to the entire account. That defines the scope where this Custom Field can be used: in one space only, or anywhere within the account. A Custom Field belongs to one place only.
    A Custom Field may be added to locations (projects and folders) and to Custom Item Types. Adding a Custom Field to a Custom Item Type means that every item based on that type will have that field. Adding a Custom Field to a location means that all items within that location (across all levels of hierarchy) will have that field. You can add a Custom Field to as many locations and types as you want.

    Adding/removing Custom Fields to/from a location may well be confused with showing/hiding columns in Table view. That’s not exactly the same. The fact that a Custom Field is added to a location doesn’t necessarily mean that the corresponding column is visible in Table view.
    FAQ
    Q: What happens with an item when I move it from location A → B?
    A: The fields inherited from location A (and all locations above location A in the hierarchy) aren’t shown in this item anymore. Instead, you see other fields that are inherited from location B.

    Q: What happens with values in fields if I move the item to a location that doesn't have that field?
    A: You won’t be able to see those fields anymore, but we don’t erase the data. If you move the item back, you will see the values that were there initially.

    Q: What happens when I cross-tag?
    A: Using the terminology from set theory, if an item is cross-tagged with locations A and B, you see a union of two sets of inherited Custom Fields. 

    Q: How does adding a CF in one view affect other views?
    A: The mechanics of adding Custom Fields works at the level of locations, not at the level of views. Practically that means that in any view that supports Custom Fields you can show or hide any field that exists in this location. When you add a field in the context of one of the views, it’s added to the location, and it’s shown in this view, but by default it remains hidden in other views.
    But what the hell
    As you have successfully gone through 3 pages of this document, two questions are likely to arise: why is it so complicated and why are all those details important?

    Short answer to both questions: it’s so complicated because we keep adding new layers of complexity without fully understanding what we already have, and it’s crucial to embrace all those details just to stop digging that hole and instead try to make this complexity work for our (and user) benefit. 

    I see this as a repetitive pattern:

    We become overwhelmed with the complexity. It’s so complex that we don’t believe users can make sense of it, so it can’t be helpful for them, so we don’t see how it can be helpful for us.
    So, we decide to pretend the complexity doesn’t exist (it’s easy, as it is not visible on the surface), and focus on solving specific user needs by adding some shortcuts that are easy to grasp both for users and for us.
    As we add those shortcuts without fully understanding the underlying complexity, in some cases they lead to unexpected and unwanted results. Also, trying to ignore the complexity, we fail to leverage all the information that already exists in the system.
    And even if we are smart enough to avoid really unwanted results, those shortcuts contribute to the overall complexity, so it’s a sort of vicious loop. Go to step 1 and repeat.

    Let’s break the vicious loop.
    Is it all we need to know about Custom Fields?
    Surely no, there is much more. Just to name a few topics that worth digging into: custom sharing of Custom Fields, aggregation, formulas. Also, every view where Custom Fields can be displayed deserve a separate conversation.

    So, there is one more document where we are going to explain all those details: Custom Fields and where to find them (work in progress)



    Presentation at Product Design Show & Tell 23 Nov 2023

    Slides

    Miro board



    End of document

    """,
    
    """
    Understanding Workflows, Part 1

    Or: How to give yourself a migraine.

    To (attempt to) understand Workflows, we need to understand that Wrike has 2 different paradigms through which configuration propagates to items. One applies to generic tasks, projects and folders and the other applies to CITs. This is true for both workflows and fields, but I will focus just on workflows here, because that is confusing enough by itself.
    Two paradigms of item configuration
    Tasks, Projects and Folders are configured based on where they are in the work structure. What workflow they are created with and what fields they have is determined by their parent container's configuration. Depending on where you create a Task/Project/Folder, their workflow and fields will be completely different.
    Custom Item Types are configured based on what they are. What workflow they are created with and what fields they have is determined by their own configuration. No matter where you create a new Custom Item Type, their workflow and fields will be the same.
    Understanding Tasks/Projects/Folders creation in detail
    REMEMBER: This ONLY applies to generic tasks and projects. CITs work completely differently and do not interact with this system (directly).
    Every new task or project created in a space will be assigned a workflow and initial status upon creation. To decide what workflow should be assigned to an item when it is created, we have a default task workflow and default project workflow setting. In space settings it looks like this:

    In the example here, the workflow assigned as both the default task workflow and the default project workflow is a workflow called "Default Workflow". This is (regrettably) an account-wide workflow that every Wrike instance used to come with. We have renamed this now to the "Standard workflow", which may be a minor (?) improvement.
    What this means in theory is that any new project created in this space will be assigned the default project workflow upon creation, and every task the default task workflow. 
    WARNING: IMPORTANT NUANCE AHEAD!
    But Folders and Projects have their own default task workflow and default project workflow setting, which are allowed to be different from the ones at the space level.
    You can see this, when you create a Project/Folder via the wizard, although only the default task workflow is exposed via UI:

    These settings can also be changed at any point later via the more menu of the work item view for projects/folders:

    This means every project/folders is allowed to independently decide what workflow should be assigned to tasks or projects created within them. What the default task/project workflow of each project/folder is set to when it is created (unless explicitly changed by the user), depends on the corresponding setting of its parent.
    What happens when I change the default task/project workflow of a folder/project?
    Only items created in future as children of this container will be affected. Existing items will keep the workflow they had at the time of their own creation.
    Will changing this setting change the corresponding settings on child containers?
    This change will propagate down the tree through all projects and folders that did not have their default task/project workflow changed by the user. Any leaf of the hierarchy that had its settings changed will be cut off from the change.
    Note that there is no way to tell if a project's/folder's default task/project workflow has been changed by the user or not via UI.
    Recap
    What workflow a generic task or generic project will be created with depends on its parent container settings. Changing these settings does not change the workflow of any already created items. It's not about what you are creating, but where you are creating it.
    Understanding Custom Item Type creation in detail
    The configuration of a Custom Item Type is static. Every instance of a Custom Item Type that is created will be the same based on the item type configuration:

    Changing the default workflow for the CIT in the Custom Item Type editor will only affect newly created items in future — but not already created items.
    That’s it (amazingly).
    Exceptions (Oh no!)
    Blueprints: If a Task/Project/Folder/CIT is created from a blueprint, the blueprint can override the workflow the item would otherwise be created with.
    Board view: The board view itself has a workflow set as a view setting (generally referred to as the "board workflow"). Items created on a board (generic and CIT) will be overridden to use the board workflow. This makes it impossible to create items that will immediately vanish from the board.
    Project Based CITs: While CITs do not derive their own workflow from their parent container like generic projects, they do allow you to set a default task workflow and default project workflow that differs from the space config. This is because Project-based CITs like regular generic projects can have generic children. This functionality is (thankfully) not exposed in the CIT editor.

    Conclusion
    Wrike is an environment in which the standard items (Tasks, Projects, Folders) behave completely differently than any Custom Item Types you create. So even if the way location-based config works wasn’t confusing already (which it definitely is!), having a competing config paradigm that is entirely different makes things extra confusing.

    Bonus: What is going on with the board view?
    When a board is created, a “board workflow” must be defined as a view setting of the board. This will be the workflow on which the status columns are based and only items that have this workflow will be shown in the regular status columns. Items from other workflows are shown in a “From other workflows” column off to the right —  invisible most of the time.
    Any newly created board view will be assigned the default task workflow of the container it is a view of at the time of creation. This ensures that generic Tasks created in views that are not this board view will appear on this board. Note that items created on the board itself will always use the board workflow regardless of the default task workflow (see “board view” above in the exceptions section).
    The problem Antonina is addressing is the following:
    If someone changes the default task workflow of the project/folder the board is a view of, tasks created in other views that are not the board will no longer appear on it.
    If you change the board workflow to a workflow that isn’t the default task workflow of the project, the same applies.
    She accomplishes this by alerting the user to the fact the board workflow and default task workflow are out of sync, and offers to remedy this by adjusting the default task workflow to be in line with the board workflow.
    However, this has no effect on custom item types. Custom item types created in the board will conform to the board workflow, but custom item types created in any other view, will have the workflow defined in their own config. Changing the default task workflow does nothing for CITs.
    It also provides no help to people deciding what workflow they might want to select when changing the board workflow. There is no sense which of the potential dozens of workflows available will end up showing items on the board (or not).

    In short, the board treats CITs as second class citizens and assumes generic Tasks are the de-facto currency of Wrike boards. This is not entirely unreasonable, because we currently ship Tasks/Projects/Folders as the default items you create — but it means that the board is essentially designed for the legacy way of config propagation, rather than the CIT-based world we want to transition to over time.


    """,

    """
    Understanding Workflows, Part 2

    There is more to workflows than meets the eye. They can do a lot more than just indicate status, but they are also more constrained than one may think initially.
    Key Take-aways
    Every status is in one of 4 universal status groups
    Transitions between statuses can be constrained
    Automated actions can be performed when status changes
    Status groups
    Any status in a workflow is always in one of 4 status groups. Active, Completed, Deferred, and Cancelled. These groups are universal across all workflows and not user-definable.
    This has multiple purposes: For reporting, every status belonging to one of 4 static status groups means that items from any workflow can be summarised from a high level (i.e. you could say what % of all tasks across Wrike is "completed" without knowing anything about a single particular workflow).
    They are also used across many different systems (inbox, notifications, quick filters, search etc.) to disregard work items that are not in the active status group. For example, tasks will only be considered overdue, if their status is in the "active" group.

    ⚠️ Status groups pitfalls

    Status group assignments are permanent. What status group a status belongs to can only be decided when it is created. It can never be changed by users, or anyone else. If a status was created in the wrong group, the only recourse is to delete it and re-create it in the correct one. The reason for this is how status groups are implemented on a technical level. The status group is baked into the ID of the status, which data-management-wise is unchangeable. This flaw of our architecture is something that comes at great cost to us and all our users.

    Re-ordering statuses is very limited. Another side-effect of this is that re-ordering statuses in a workflow is extremely limited. Since statuses cannot be moved between groups, statuses can only be re-ordered within group. Additionally, the first status in the "Active" and "Completed" group can also not be moved. Meaning that re-ordering is only possible for the Active and Completed groups if they have at least 3 statuses, and minimum 2 statuses for Deferred and Cancelled.

    "Active" and "Completed" always need to have one status. Any status can be deleted, unless it is the last status in the Active or Completed groups. These two groups need to always have one status in them. This means any workflow always has at least 2 statuses. This ensures any item in Wrike can be "checked" and "unchecked". Checking an item will assign the first status in the "Completed" group and unchecking it will assign the first status in the "Active" group.

    Status groups are mandatory. The big downside here is that in many cases a workflow just has 1 status per group, often sharing the group name. So there is an "Active" status in the "Active" group, another "Completed" status in the "Completed" group and so on. This is a large UX headache in combination with status groups not being editable. We need to teach everyone about status groups when they create their first status, regardless of whether higher level reporting or status grouping will be relevant to them at their scale.

    Workflow transitions
    Each status of a workflow can limit what other statuses it can be transitioned to. For example, you could configure that once something is marked as "completed", it can afterwards only be changed to "re-opened".

    ⚠️ Warning: By default, workflow transitions are not enforced — it only changes the UI. If a status has transitions specified, all non-specified statuses will be shown in an "other" submenu in the status picker. To enforce workflow transitions the workflow must have the "Lock transitions" option on the workflow enabled.

    Workflow Assignment
    You can select a specific person to assign a task to when a specific status is applied.
    Workflow Approval
    You can automatically create an approval when a work item has a specific status in the workflow applied. Various variables, such as approvers, approval due date and other can be specified here. You can also specify what status the work item should be transitioned to if the result of the Approval is either "Approved" or "Rejected".

    🤯Headache warning. Wait. Are "Approved" and "Rejected" statuses? No. They are the two possible outcomes of any Approval, regardless of workflow. If you wanted an approval decision to be reflected in an item's status, you would have to create an "Approved" and "Rejected" status as part of your workflow and then configure the automatically created Approval to transition the work item to those statuses based on the Approval outcome.


    """,

    """
    Addis Ababa

    Addis Ababa saw a wide-scale economic boom in 1926 and 1927, and an increase in the number of buildings owned by the middle class, including stone houses filled with imported European furniture. The middle class also imported newly manufactured automobiles and expanded banking institutions.[14] During the Italian occupation, urbanization and modernization steadily increased through a masterplan; it was hoped Addis Ababa would be a more "colonial" city and continued on after the occupation. Subsequent master plans were designed by French and British consultants from the 1940s onwards, focusing on monuments, civic structures, satellite cities and the inner-city. Similarly, the later Italo-Ethiopian masterplan (also projected in 1986) concerned only urban structure and accommodation services, but was later adapted by the 2003 masterplan.
    """,

    """
    Amharic
    
    Amharic has been the official working language of Ethiopia, language of the courts, the language of trade and everyday communications and of the military since the late 12th century. 
    """
] 