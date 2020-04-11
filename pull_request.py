import os
import calling
import main
pull = '''
1. Decline pull request
2. Check if pull request can be merged
3. Merge pull request
4. Reopen pull request
5. back?
'''

def manage_pull():
    os.system("cls")
    print(pull)
    task_input = input()
    if task_input == "1":
        # Decline pull request
        project_key = calling.project_key()
        pr_id = input("Enter pull request id \n")
        pr_version = input("Enter pull request version \n")
        repository = input("Enter repository \n")
        print(calling.bitbucket.decline_pull_request(project_key, repository, pr_id, pr_version))
        input("press any key to continue")
        main.menu()
    elif task_input == "2":
        # Check if pull request can be merged
        project_key = calling.project_key()
        pr_id = input("Enter pull request id \n")
        repository = input("Enter repository \n")
        print(calling.bitbucket.is_pull_request_can_be_merged(project_key, repository, pr_id))
        input("press any key to continue")
        main.menu()
    elif task_input == "3":
        # Merge pull request
        project_key = calling.project_key()
        pr_id = input("Enter pull request id \n")
        pr_version = input("Enter pull request version \n")
        repository = input("Enter repository \n")
        print(calling.bitbucket.bitbucket.merge_pull_request(project_key, repository, pr_id, pr_version))
        input("press any key to continue")
        main.menu()
    elif task_input == "4":
        # Reopen pull request
        project_key = calling.project_key()
        pr_id = input("Enter pull request id \n")
        pr_version = input("Enter pull request version \n")
        repository = input("Enter repository \n")
        print(calling.bitbucket.reopen_pull_request(project_key, repository, pr_id, pr_version))
        input("press any key to continue")
        main.menu()
    elif task_input == "5":
        os.system("cls")
        main.menu()
    else:
        manage_pull()