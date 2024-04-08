"""
Example lists:

userList: user dictionaries with user data: name and accountId
tasksList: task dictionaries with issue data: summary, description, and labels
"""
userList = [
    {"name": "john doe", "id": "60031:aaaaaaaa-ccbb-2222-ffff-000000000001"},
    {"name": "marie jones", "id": "60032:aaaaaaaa-ccbb-2222-ffff-000000000002"},
    {"name": "jane smith", "id": "60033:aaaaaaaa-ccbb-2222-ffff-000000000003"},
]

description = """
Fundamentals chapter:

- https://www.youtube.com/watch?v=rvTejAg_fbY
- https://www.youtube.com/watch?v=GZ9q0kkDw-o
"""

taskList = [
    {
        "summary": "Task 1",
        "description": description,
        "issueType": "Task",
        "labels": ["task_1", "automation"]
    },
    {
        "summary": "Task 2",
        "issueType": "Task",
        "description": "Description task 2",
        "labels": ["task_2", "automation"]
    },
]
