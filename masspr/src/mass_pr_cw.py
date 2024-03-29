from github import Github
from git import Repo
import os
import argparse
import utils

parser = argparse.ArgumentParser()
parser.add_argument('-t', '--token', type=str, required=true, help="Github Token")
parser.add_argument('-r', '--service-repo', type=str, required=true, help="Servcie repo")
parser.add_argument('-b', '--feature-branch', type=str, required=true, help="Name of branch")
args =  parser.parse_args()
repos = args.service_repo.split(',')
github_token = args.tokenfeature_branch = args.feature_branch

#Github Enterprise with custom hostname
print("Creating Github client")
g= Github(base_url= "host/api/v1", login_or_token=github_token)
org=  g.get_organization('git org name')

for repo_name in repos:
print('---------')
print(f"Trying for {repo_name}")
folder_name = "temp-"+ repo_name
repo_url_base = "git host"
org_name= "git org name"
user_name = g.get_user().login
repo_url = f"{repo_url_base}/{org_name}/{repo_name}.git"
remote-service_repo = org.get-repo(repo_name)

# crate feature_branch
print(f"Creating feature branch - {repo_name}")
source_branch_name =  "develop"
target_branch_name = feature_branchsource_branch = remote -service_repo.het_branch(source_branch_name)

try:
  remote_service_repo.create_git_ref(ref='refs/head'+ target_branch_name, sha=source_branch.commit.sha)
  except Exception as e:
   if "Reference already exists" in str(e):
   print("Branch already exist ::")

# Make a folder

print(f"craeting temp folder- {folder_name}")
os.makedir(folder_name)


# clone service-repo

print(f"cloning {repo_url}")
repo_instance = Repo.clone_from(repo_url, folder_name)
print("checking out feature branch")
repo_instance.git.checkout(feature_branch)

# Update file
print("updating file")
find_tg=""
replace_tg=""
words_to-update_in_gears_file={
find_tg:replace_tg
}

utils.replace_words_move_file(f"{folder_name}/filename", f"{folder-name}/filename_temp", {})
os.remove(f"{folder_name}/filename")
utils.replace_words_move_file(f"{folder_name}/filename_temp", f"{folder_name}/Filename", words_to_update_in_gears_file)
os.remove(f"{folder_name}/filename_temp")

# commit and push

print("Add, commit, push")
repo_instance.git.add(['Gearsfile'])
repo_instance.index.commit("update commit message")
origin = repo_instance.remote(name = 'origin')
origin.push()


# create PR
print("Creating PR")
try:
remote_service_repo.create_pull("","",f'{source_branch_name}', f''{target_branch_name}', True)
except Exception as e:
if "A PR already exist" in str(e):
print("A pull request already exist...")
else
raise e
print("---------------")

Print("All steps executed")

