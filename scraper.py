import requests
from bs4 import BeautifulSoup
import re

root_url = "https://github.com"
website = requests.get(root_url + "/trending/python?since=daily&spoken_language_code=en")

parser = BeautifulSoup(website.content, "html.parser")

trending_repos = parser.find_all("article", class_="Box-row")
for repo in trending_repos:
  repo_header = repo.find("h1").find("a")
  repo_name = "".join(repo_header.text.split())
  repo_link = root_url + repo_header["href"]
  print(repo_name, end="\n")
  print(repo_link, end="\n")
  repo_stars = repo.find("a", href=repo_header["href"] + "/stargazers").text.strip()
  print(f"{repo_stars} stars", end="\n")
  repo_forks = repo.find("svg", class_="octicon-repo-forked").find_parent().text.strip()
  print(f"{repo_forks} forks", end="\n")
  repo_stars_today_element = repo.find(text=re.compile("stars today"))
  repo_stars_today = 0 if repo_stars_today_element is None else repo_stars_today_element.text.strip().split()[0]
  print(f"{repo_stars_today} stars today", end="\n"*2)