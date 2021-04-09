#!/usr/bin/env python3

import os
from os.path import join, dirname
from github import Github
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

API_KEY = os.getenv('API_KEY')

def main():

  g = Github(API_KEY)

  list_of_users = ['paromitaroy',]
  
  topic_count = 0
  for user in list_of_users:
    repo_count = 0
    for repo in g.get_user(user).get_repos():
      repo_count+=1
      for topic in repo.get_topics() :
        if topic == "devops-blue-iguana":
          topic_count = topic_count + 1
          print("Owner :", user,"\nRepository : ", repo.git_url, "\nDescription :",repo.description,"\nCreatedOn :", repo.created_at,"\nStars :",repo.stargazers_count, "\nOpenIssues :", repo.open_issues,"\nPrivate:", repo.private, "\nTopics: ", repo.get_topics(),"\n\n")
  
  if topic_count == 0:
    print ("No repos exist with topic devops-blue-iguana for", user)

if __name__ == '__main__':
   main()
