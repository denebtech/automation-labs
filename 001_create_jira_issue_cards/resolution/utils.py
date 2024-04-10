import json
import os
import requests
from config import logger
from requests.auth import HTTPBasicAuth

workspace = os.getenv(key="JIRA_WORKSPACE", default="http://example.atlassian.net") 
url = f"{workspace}/rest/api/2/issue"
user = os.getenv(key="JIRA_USER", default="email@example.com")
token = os.getenv(key="JIRA_TOKEN", default="replace-me")
project_key = os.getenv(key="JIRA_PROJECT_KEY", default="replace-me")

headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
}

auth = HTTPBasicAuth(user, token)


def response_message(status_list):
    if any(status != 201 for status in status_list):
        return "Issues created with errors"

    return "Issues successfully created"


def create_issues(tasks, user):
    status_list = []
    
    for task in tasks:
        payload = json.dumps({
            "fields": {
                "project": {
                    "key": project_key
                },
                "summary": task["summary"],
                "description": task["description"],
                "issuetype": {
                    "name": task["issueType"]
                },
                "assignee": {
                    "id": user["id"]
                },
                "labels": task["labels"]
            }
        })

        response = requests.request(
            "POST",
            url,
            data=payload,
            headers=headers,
            auth=auth
        )
        status_list.append(response.status_code)

        if response.status_code != 201:
            logger.error(
                "HTTP %s, User: %s, error in task '%s', reason: %s",
                response.status_code,
                user["name"],
                task["summary"],
                response.reason
            )

    message = response_message(status_list)

    return message
