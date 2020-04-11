import os
import calling
import main
code = '''
1. Get repositories list from project
2. Create a new repository
3. Get branches from repo
4. Creates a branch using the information provided in the request
5. Delete branch from related repo
6. Get pull requests
7. Get pull request activities
8. Get pull request changes
9. Get pull request commits
10. Add comment into pull request
11. Get tags for related repo
12. Get project tags
13. Set tag
14. Delete tag
15. Get diff
16. Get commit list from repo
17. Get change log between 2 refs
18. Get raw content of the file from repo
19. back?
'''

def manage_code():
    os.system("cls")
    print(code)
    task_input = input()
    if task_input == "1":
        # Get repositories list from project
        project_key = calling.project_key()
        limit = input("Enter limit \n")
        print(calling.bitbucket.repo_list(project_key, limit))
        input("press any key to continue")
        main.menu()
    elif task_input == "2":
        # Create a new repository.
        project_key = calling.project_key()
        repository = input("Enter repository name \n")
        print(calling.bitbucket.create_repo(project_key, repository, forkable=False, is_private=True))
        input("press any key to continue")
        main.menu()
    elif task_input == "3":
        # Get branches from repo
        project = calling.project_key()
        repository = input("Enter repository name \n")
        limit = input("Enter limit \n")
        print(calling.bitbucket.get_branches(project, repository, filter='', limit=limit , details=True))
        input("press any key to continue")
        main.menu()
    elif task_input == "4":
        # Creates a branch using the information provided in the request.
        project_key = calling.project_key()
        repository = input("Enter repository name \n")
        name = input("Enter name of your branch \n")
        start_point = input("Enter start point \n")
        message = input("Enter message \n")
        print(calling.bitbucket.create_branch(project_key, repository, name, start_point, message))
        input("press any key to continue")
        main.menu()
    elif task_input == "5":
        # Delete branch from related repo
        project_key = calling.project_key()
        repository = input("Enter repository name \n")
        name = input("Enter name of your branch \n")
        end_point = input("Enter end point \n")
        print(calling.bitbucket.delete_branch(project_key, repository, name, end_point))
        input("press any key to continue")
        main.menu()
    elif task_input == "6":
        # Get pull requests
        project = calling.project_key()
        repository = input("Enter repository name \n")
        print(calling.bitbucket.get_pull_requests(project, repository, state='OPEN', order='newest', limit=100, start=0))
        input("press any key to continue")
        main.menu()
    elif task_input == "7":
        # Get pull request activities
        project = calling.project_key()
        repository = input("Enter repository name \n")
        pull_request_id = input("Enter pull request id \n")
        print(calling.bitbucket.get_pull_requests_activities(project, repository, pull_request_id))
        input("press any key to continue")
        main.menu()
    elif task_input == "8":
        # Get pull request changes
        project = calling.project_key()
        repository = input("Enter repository name \n")
        pull_request_id = input("Enter pull request id \n")
        print(calling.bitbucket.get_pull_requests_changes(project, repository, pull_request_id))
        input("press any key to continue")
        main.menu()
    elif task_input == "9":
        # Get pull request commits
        project = calling.project_key()
        repository = input("Enter repository name \n")
        pull_request_id = input("Enter pull request id \n")
        print(calling.bitbucket.get_pull_requests_commits(project, repository, pull_request_id))
        input("press any key to continue")
        main.menu()
    elif task_input == "10":
        # Add comment into pull request
        project = calling.project_key()
        repository = input("Enter repository name \n")
        pull_request_id = input("Enter pull request id \n")
        text = input("Enter text \n")
        print(calling.bitbucket.add_pull_request_comment(project, repository, pull_request_id, text))
        input("press any key to continue")
        main.menu()
    elif task_input == "11":
        # Get tags for related repo
        project = calling.project_key()
        repository = input("Enter repository name \n")
        print(calling.bitbucket.get_tags(project, repository, filter='', limit=99999))
        input("press any key to continue")
        main.menu()
    elif task_input == "12":
        # Get project tags
        project = calling.project_key()
        repository = input("Enter repository name \n")
        tag_name = input("Enter tag name id \n")
        print(calling.bitbucket.get_project_tags(project, repository, tag_name))
        input("press any key to continue")
        main.menu()
    elif task_input == "13":
        # Set tag
        project = calling.project_key()
        repository = input("Enter repository name \n")
        commit_revision = input("Enter commit revision \n")
        tag_name = input("Enter tag name id \n")
        print(calling.bitbucket.set_tag(project, repository, tag_name, commit_revision, description=None))
        input("press any key to continue")
        main.menu()
    elif task_input == "14":
        # Delete tag
        project = calling.project_key()
        repository = input("Enter repository name \n")
        tag_name = input("Enter tag name id \n")
        print(calling.bitbucket.delete_tag(project, repository, tag_name))
        input("press any key to continue")
        main.menu()
    elif task_input == "15":
        # Get diff
        project = calling.project_key()
        repository = input("Enter repository name \n")
        path = input("Enter path \n")
        hash_oldest = input("Enter hash oldest \n")
        hash_newest = input("Enter hash newest \n")
        print(calling.bitbucket.get_diff(project, repository, path, hash_oldest, hash_newest))
        input("press any key to continue")
        main.menu()
    elif task_input == "16":
        # Get commit list from repo
        project = calling.project_key()
        repository = input("Enter repository name \n")
        hash_oldest = input("Enter hash oldest \n")
        hash_newest = input("Enter hash newest \n")
        print(calling.bitbucket.get_commits(project, repository, hash_oldest, hash_newest, limit=99999))
        input("press any key to continue")
        main.menu()
    elif task_input == "17":
        # Get change log between 2 refs
        project = calling.project_key()
        repository = input("Enter repository name \n")
        ref_from = input("Enter ref from \n")
        ref_to = input("Enter ref to \n")
        print(calling.bitbucket.get_changelog(project, repository, ref_from, ref_to, limit=99999))
        input("press any key to continue")
        main.menu()
    elif task_input == "18":
        # Get raw content of the file from repo
        project = calling.project_key()
        repository = input("Enter repository name \n")
        filename = input("Enter filename \n")
        print(calling.bitbucket.get_content_of_file(project, repository, filename, at=None, markup=None))
        input("press any key to continue")
        main.menu()
    elif task_input == "19":
        os.system("cls")
        main.menu()
    else:
        manage_code()