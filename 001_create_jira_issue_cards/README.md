# Lab 001 - Create JIRA issue cards

## Requirement

We need create JIRA issue cards from a list of tasks for differents collaborators in a list.

```
user_list = [
    "john doe",
    "marie jones",
    "jane smith",
]

tasks_list = [
    {
        "summary": "Task 1",
        "description": "Description task 1",
        "labels": ["task_1", "automation"]
    },
    {
        "summary": "Task 2",
        "description": "Description task 2",
        "labels": ["task_2", "automation"]
    },
    ...
]
```

## Referencies

- [Jira REST API examples](https://developer.atlassian.com/server/jira/platform/jira-rest-api-examples/)
- [REST API v2](https://developer.atlassian.com/cloud/jira/platform/rest/v2/intro/#version)
