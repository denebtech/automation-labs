"""
Example lists:

userList: user dictionaries with user data: name and accountId
tasksList: task dictionaries with issue data: summary, description, and labels
"""
userList = [
    {"name": "john doe", "id": "70121:b34e3e78-fc7f-41f1-b8a2-4a59a10a4304"}
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
