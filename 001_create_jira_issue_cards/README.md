# Lab 001 - Create JIRA issue cards

## Requirement

We need create JIRA issue cards from a list of tasks for differents collaborators in a list.

```
# example lists

userList = [
    {"name": "john doe", "id": "60031:aaaaaaaa-ccbb-2222-ffff-000000000001"},
    {"name": "marie jones", "id": "60032:aaaaaaaa-ccbb-2222-ffff-000000000002"},
    {"name": "jane smith", "id": "60033:aaaaaaaa-ccbb-2222-ffff-000000000003"},
]

taskList = [
    {
        "summary": "Task 1",
        "description": "Description task 1",
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
```

## Referencies

- [Jira REST API examples](https://developer.atlassian.com/server/jira/platform/jira-rest-api-examples/)
- [REST API v2](https://developer.atlassian.com/cloud/jira/platform/rest/v2/intro/#version)

## Resolution example

- [Resolution](./resolution/README.md)
