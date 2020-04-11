import branch
import group 
import manage_code 
import project 
import pull_request 
import repository 
import os

task='''
1. Manage projects
2. Manage repositories
3. Groups and Admin
4. Manage code and create repo
5. Branch permissions
6. Pull request management
7. exit?
'''

def menu():
    os.system("cls")
    print(task)
    task_input = input()
    if task_input == "1":
        project.manage_project()
    elif task_input == "2":
        repository.manage_repo()
    elif task_input == "3":
        group.manage_group()
    elif task_input == "4":
        manage_code.manage_code()
    elif task_input == "5":
        branch.manage_branch()
    elif task_input == "6":
        pull_request.manage_pull()
    elif task_input == "7":
        print("Good Bye and Thanks for using Bitbucket !!")
    else:
        os.system("cls")
        input("You have chosen wrong task, press any key to continue")
        menu()

if __name__=="__main__":
    menu()









