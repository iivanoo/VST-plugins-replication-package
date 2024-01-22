import os
import pandas as pd 

repo_url_list = []
github_repositories_url = pd.read_csv("CSVs Used//final_data_curated - final_data_curated_categorized.csv")
repo_url_list.extend(github_repositories_url["html_url"].to_list())

os.chdir("Repositories\\")
for repo in repo_url_list:
    os.system("git clone " + repo + ".git")