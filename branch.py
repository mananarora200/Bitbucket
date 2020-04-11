import os
import main
import calling
branch = '''
1. Set branches permissions
2. Delete a single branch permission by premission id
3. Get a single branch permission by permission id
4. back?
'''

def manage_branch():
    os.system("cls")
    print(branch)
    task_input = input()
    if task_input == "1":
        # Set branches permissions
        project_key = calling.project_key()
        print(calling.bitbucket.set_branches_permissions(project_key, multiple_permissions=False, matcher_type=None, matcher_value=None, permission_type=None, repository=None, except_users=[], except_groups=[], except_access_keys=[], start=0, limit=25))
        input("press any key to continue")
        main.menu()
    elif task_input == "2":
        # Delete a single branch permission by premission id
        project_key = calling.project_key()
        permission_id = input("Enter permission id \n")
        repository = input("Enter repository \n")
        print(calling.bitbucket.delete_branch_permission(project_key, permission_id, repository))
        input("press any key to continue")
        main.menu()
    elif task_input == "3":
        # Get a single branch permission by permission id
        project_key = calling.project_key()
        permission_id = input("Enter permission id \n")
        repository = input("Enter repository \n")
        print(calling.bitbucket.get_branch_permission(project_key, permission_id, repository))
        input("press any key to continue")
        main.menu()
    elif task_input == "4":
        os.system("cls")
        main.menu()
    else:
        manage_branch()