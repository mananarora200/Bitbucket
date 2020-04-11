import os
import calling
import main
repo = '''
1. Get single repository
2. Disable branching model
3. Enable branching model
4. Get branching model
5. Set branching model
6. Grant repository permission to an specific user
7. Grant repository permission to an specific group
8.Delete a repository (DANGER!)
9.back?
'''

def manage_repo():
    os.system("cls")
    print(repo)
    task_input = input()
    if task_input == "1":
        # Get single repository
        project_key = calling.project_key()
        repository_slug = input("Enter repository slug \n")
        print(calling.bitbucket.get_repo(project_key, repository_slug))
        input("press any key to continue")
        main.menu()
    elif task_input == "2":
        # Disable branching model
        project_key = calling.project_key()
        repo_key = input("Enter repository key \n")
        print(calling.bitbucket.disable_branching_model(project_key, repo_key))
        input("press any key to continue")
        main.menu()
    elif task_input == "3":
        # Enable branching model
        project_key = calling.project_key()
        repo_key = input("Enter repository key \n")
        print(calling.bitbucket.enable_branching_model(project_key, repo_key))
        input("press any key to continue")
        main.menu()
    elif task_input == "4":
        # Get branching model
        project_key = calling.project_key()
        repo_key = input("Enter repository key \n")
        print(calling.bitbucket.get_branching_model(project_key, repo_key))
        input("press any key to continue")
        main.menu()
    elif task_input == "5":
        input("For future use, press any key")
        os.system("cls")
        main.menu()
    elif task_input == "6":
        # Grant repository permission to an specific user
        project_key = calling.project_key()
        repo_key = input("Enter repository key \n")
        username = input("Enter username \n")
        permission = input("Enter permission \n")
        print(calling.bitbucket.repo_grant_user_permissions(project_key, repo_key, username, permission)) 
        input("press any key to continue")
        main.menu()
    elif task_input == "7":
        # Grant repository permission to an specific group
        project_key = calling.project_key()
        repo_key = input("Enter repository key \n")
        groupname = input("Enter groupname \n")
        permission = input("Enter permission \n")
        print(calling.bitbucket.repo_grant_group_permissions(project_key, repo_key, groupname, permission))
        input("press any key to continue")
        main.menu()
    elif task_input == "8":
        # Delete a repository (DANGER!)
        project_key = calling.project_key()
        repository_slug = input("Enter repository slug \n")  
        print(calling.bitbucket.delete_repo(project_key, repository_slug)) 
        input("press any key to continue")
        main.menu()
    elif task_input == "9":
        os.system("cls")
        main.menu()
    else:
        manage_repo()
    