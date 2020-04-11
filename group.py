import os
import calling
import main
group = '''
1. Get group of members
2. All project administrators
3. back?
'''

def manage_group():
    os.system("cls")
    print(group)
    task_input = input()
    if task_input == "1":
        # Get group of members
        group = input("Enter group \n")
        limit = input("Enter limit \n")
        print(calling.bitbucket.group_members(group, limit))
        input("press any key to continue")
        main.menu()
    elif task_input == "2":
        # All project administrators
        print(calling.bitbucket.all_project_administrators())
        input("press any key to continue")
        main.menu()
    elif task_input == "3":
        os.system("cls")
        main.menu()
    else:
        manage_group()