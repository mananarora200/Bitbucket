from atlassian import Bitbucket

bitbucket = Bitbucket(
    url='http://localhost:7990',
    username='manan',
    password='tanviiloveu7')

def project_key():
    prj = input("Enter the project key \n")
    return prj.upper()
def repo_id():
    return input("Enter the repository id \n")