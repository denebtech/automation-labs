from config import logger
from constants import userList, taskList
from utils import create_issues


def main():
    for user in userList:
        response = create_issues(tasks=taskList, user=user)
        logger.info("User: %s, %s", user["name"], response)


if __name__ == "__main__":
    main()
