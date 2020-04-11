import os
import calling
import main
project = '''
1. Project list
2. Repo list
3. Project info
4. Create project
5. Get users who has permission in project
6. Get project administrators for project
7. Get Project Groups
8. Get groups with admin permissions
9. Project summary
10. Grant project permission to an specific user
11. Grant project permission to an specific group
12. back?
'''

def manage_project():
    os.system("cls")
    # key = calling.project_key()
    print(project)
    task_input = input()
    if task_input == "1":
        # Project list
        print(calling.bitbucket.project_list())
        input("press any key to continue")
        main.menu()
    elif task_input == "2":
        # Repo list
        project_key = calling.project_key()
        print(calling.bitbucket.repo_list(project_key))
        input("press any key to continue")
        main.menu()
    elif task_input == "3":
        # Project info
        project_key = calling.project_key()
        print(calling.bitbucket.project(project_key))
        input("press any key to continue")
        main.menu()
    elif task_input == "4":
        # Create project
        project_key = calling.project_key()
        name = input("Enter project name \n")
        description = input("Enter description \n")
        print(calling.bitbucket.create_project(project_key, name, description))
        input("press any key to continue")
        main.menu()
    elif task_input == "5":
        # Get users who has permission in project
        project_key = calling.project_key()
        limit = input("Enter limit \n")
        print(calling.bitbucket.project_users(project_key, limit, filter_str=None))
        input("press any key to continue")
        main.menu()
    elif task_input == "6":
        # Get project administrators for project
        project_key = calling.project_key()
        print(calling.bitbucket.project_users_with_administrator_permissions(project_key))
        input("press any key to continue")
        main.menu()
    elif task_input == "7":
        # Get Project Groups
        project_key = calling.project_key()
        limit = input("Enter limit \n")
        print(calling.bitbucket.project_groups(project_key, limit , filter_str=None))
        input("press any key to continue")
        main.menu()
    elif task_input == "8":
        # Get groups with admin permissions
        project_key = calling.project_key()
        print(calling.bitbucket.project_groups_with_administrator_permissions(project_key))
        input("press any key to continue")
        main.menu()
    elif task_input == "9":
        # Project summary
        project_key = calling.project_key()
        print(calling.bitbucket.project_summary(project_key))
        input("press any key to continue")
        main.menu()
    elif task_input == "10":
        # Grant project permission to an specific user
        project_key = calling.project_key()
        username = input("Enter your username \n")
        permission = input("Enter your permission \n")
        print(calling.bitbucket.project_grant_user_permissions(project_key, username, permission))
        input("press any key to continue")
        main.menu()
    elif task_input == "11":
        # Grant project permission to an specific group
        project_key = calling.project_key()
        groupname = input("Enter your group name \n")
        permission = input("Enter your permission \n")
        print(calling.bitbucket.project_grant_group_permissions(project_key, groupname, permission))
        input("press any key to continue")
        main.menu()
    elif task_input == "12":
        os.system("cls")
        main.menu()
    else:
        manage_project()