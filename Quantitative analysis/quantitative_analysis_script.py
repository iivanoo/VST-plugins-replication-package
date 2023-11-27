# library & dataset
import seaborn as sns
import pandas as pd 
import matplotlib.pyplot as plt
import scipy
import numpy as np
from datetime import date
import datetime
import matplotlib.ticker as mtick
import statsmodels.api as sm
import ast



# dataframe for repos data
df_repos = pd.read_csv('CSVs Used//final_data_curated - final_data_curated_categorized.csv')
df_programming_languages = pd.read_csv('CSVs Used//only_programming_languages_used_across_categorized_repositories.csv')
df_contributors = pd.read_csv('CSVs Used//contributors_details.csv')


##################################
########## REPO TOPICS ###########
##################################

# All tags from all the years
df_intermediary_topic = pd.DataFrame(data = df_repos['topics'])
df_intermediary_topic['topics'] = df_intermediary_topic['topics'].apply(ast.literal_eval)
df_topic = df_intermediary_topic.explode('topics')
df_topic2 = df_topic['topics'].value_counts()[:20].reset_index()
df_topic2.columns = ['Tag', 'Count']

topic = df_topic2.plot(x='Tag',y='Count',kind='bar',legend=False,figsize=(15,10))

topic.set(title='GitHub topics used across repositories')
topic.set(xlabel='Topics')
topic.set(ylabel='Repositories count')

plt.xticks(rotation=45, ha='right')
plt.savefig("Figures//topics.png")
plt.clf()

# All tags from the last 5 years - the gap contains leap years so there are 1827 days
till_5_years = pd.to_datetime(date.today() - datetime.timedelta(days=1827))

df_intermediary_topic_5_years = pd.DataFrame(data = df_repos[['topics', 'created_at']])
df_intermediary_topic_5_years['created_at'] =  pd.to_datetime(df_intermediary_topic_5_years['created_at'].str.slice(0,10),format='%Y-%m-%d')
df_intermediary_topic_5_years = df_intermediary_topic_5_years.sort_values(['created_at'])

df_intermediary_topic_5_years = df_intermediary_topic_5_years[df_intermediary_topic_5_years['created_at']>=till_5_years]
df_intermediary_topic_5_years['topics'] = df_intermediary_topic_5_years['topics'].apply(ast.literal_eval)

df_topic_5_years = df_intermediary_topic_5_years.explode('topics')
df_topic2_5_years = df_topic_5_years['topics'].value_counts()[:20].reset_index()
df_topic2_5_years.columns = ['Tag', 'Count']

topic_5_years = df_topic2_5_years.plot(x='Tag',y='Count',kind='bar',legend=False,figsize=(15,10))

topic_5_years.set(title='GitHub topics used across repositories in the last five years')
topic_5_years.set(xlabel='Topics')
topic_5_years.set(ylabel='Repositories count')

plt.xticks(rotation=45, ha='right')
plt.savefig("Figures//topics_last_5_years.png")
plt.clf()

# See the evolution of JUCE
topic = 'juce'
df_intermediary_topic_JUCE = pd.DataFrame(data = df_repos[['name','topics','created_at']])
df_intermediary_topic_JUCE['contains_juce_tag'] = df_intermediary_topic_JUCE['topics'].map(lambda x: topic in x)

df_topic_JUCE = df_intermediary_topic_JUCE.loc[df_intermediary_topic_JUCE['contains_juce_tag'] == True]
df_topic_JUCE['created_at'] =  pd.to_datetime(df_topic_JUCE['created_at'].str.slice(0,10),format='%Y-%m-%d')
year = df_topic_JUCE['created_at'].dt.year
df_topic_JUCE['count_per_year'] = df_topic_JUCE.groupby(year)['created_at'].transform('size')

evolution_JUCE_tag = sns.histplot(df_topic_JUCE['created_at'].dt.year, discrete=True, color='blue', kde=True)

evolution_JUCE_tag.set(title='Evolution of JUCE framework GitHub tags: (\'juce\',\'juce-framework\',\'juce-plugins\',\'juce-plugin\') over the years')
evolution_JUCE_tag.set(xlabel='Year')
evolution_JUCE_tag.set(ylabel='Repositories count')
evolution_JUCE_tag.set(xticks=df_topic_JUCE['created_at'].dt.year)

plt.savefig("Figures//juce_framework_over_the_years.png")
plt.clf()

#################################
########## CREATED AT ###########
#################################
plt.figure(figsize=(15,10))

# Count repos per year
df_created_at_count = pd.DataFrame(data = df_repos[['name','created_at']])
df_created_at_count['created_at'] = pd.to_datetime(df_created_at_count['created_at'].str.slice(0,10),format='%Y-%m-%d')
year = df_created_at_count['created_at'].dt.year
df_created_at_count['count_per_year'] = df_created_at_count.groupby(year)['created_at'].transform('size')

created_at = sns.histplot(df_created_at_count['created_at'].dt.year, discrete=True, color='blue', kde=True)

created_at.set(title='Created repositories per year')
created_at.set(xlabel='Year')
created_at.set(ylabel='Repositories count')
created_at.set(xticks=df_created_at_count['created_at'].dt.year)

plt.savefig("Figures//created_at.png")
plt.clf()


###################################
########## SIZE OF REPO ###########
###################################
plt.figure(figsize=(15,10))

size = sns.violinplot(data=df_repos, y=df_repos[df_repos["size"]<100000]["size"], palette='pastel')
sns.boxplot(y=df_repos[df_repos["size"]<100000]["size"], data=df_repos, palette='deep', width=0.3,boxprops={'zorder': 2})

size.set(title='Size of repositories')
size.set(xlabel='Repositories', ylabel='Size (Kb)')

plt.tight_layout()
plt.savefig("Figures//size.png")
plt.clf()



###########################################
########## PROGRAMMING LANGUAGE ###########
###########################################
plt.figure(figsize=(15,10))

programming = sns.histplot(df_programming_languages['language'], discrete=True, color='blue', kde=True)

programming.set(title='Most used Programming Language across repositories')
programming.set(xlabel='Programming Language Used')
programming.set(ylabel='Repositories count')

plt.xticks(rotation=45, ha='right')
plt.savefig("Figures//programming_language.png")
plt.clf()


#######################################
########## MEGA CONTRIBUTOR ###########
#######################################
plt.figure(figsize=(100,10))

programming = sns.histplot(df_contributors['login'], discrete=True, color='blue', kde=True)

programming.set(title='Contributors across the repositories')
programming.set(xlabel='Contributors GitHub Username')
programming.set(ylabel='Repositories count')

plt.xticks(rotation=90, ha='right')
plt.savefig("Figures//mega_contributor.png")
plt.clf()

##################################
########## STARS COUNT ###########
##################################
plt.figure(figsize=(15,10))

size = sns.violinplot(data=df_repos, y=df_repos[df_repos["stargazers_count"]<200]["stargazers_count"], palette='pastel')
sns.boxplot(y=df_repos[df_repos["stargazers_count"]<200]["stargazers_count"], data=df_repos, palette='deep', width=0.3,boxprops={'zorder': 2})

size.set(title='Stars count of repositories')
size.set(xlabel='Repositories', ylabel='Stars')

plt.tight_layout()
plt.savefig("Figures//stars_count.png")
plt.clf()


#####################################
########## WATCHERS COUNT ###########
#####################################
plt.figure(figsize=(15,10))

size = sns.violinplot(data=df_repos, y=df_repos[df_repos["subscribers_count"]<30]["subscribers_count"], palette='pastel')
sns.boxplot(y=df_repos[df_repos["subscribers_count"]<30]["subscribers_count"], data=df_repos, palette='deep', width=0.3,boxprops={'zorder': 2})

size.set(title='Watchers count of repositories')
size.set(xlabel='Repositories', ylabel='Watchers')

plt.tight_layout()
plt.savefig("Figures//watchers_count.png")
plt.clf()


##################################
########## FORKS COUNT ###########
##################################
plt.figure(figsize=(15,10))

size = sns.violinplot(data=df_repos, y=df_repos[df_repos["forks_count"]<100]["forks_count"], palette='pastel')
sns.boxplot(y=df_repos[df_repos["forks_count"]<100]["forks_count"], data=df_repos, palette='deep', width=0.3,boxprops={'zorder': 2})

size.set(title='Forks count of repositories')
size.set(xlabel='Repositories', ylabel='Forks')

plt.tight_layout()
plt.savefig("Figures//forks_count.png")
plt.clf()


#####################################
########## DEFAULT BRANCH ###########
#####################################
plt.figure(figsize=(15,10))

programming = sns.histplot(df_repos['default_branch'], discrete=True, color='blue', kde=True)

programming.set(title='Most encountered default branch across repositories')
programming.set(xlabel='Default Branch')
programming.set(ylabel='Repositories count')

plt.xticks(rotation=45, ha='right')
plt.savefig("Figures//default_branch.png")
plt.clf()


#############################
########## ISSUES ###########
#############################
issues_fig, ax_issues = plt.subplots(ncols=3,figsize=(15,10),sharey=True)

df_issues = pd.DataFrame(data = df_repos[['open_issues_only','closed_issues_only']])
df_issues['total_issues'] = df_issues['open_issues_only'] + df_issues['closed_issues_only']

issues_opened = sns.violinplot(data=df_issues, y=df_issues[df_issues["open_issues_only"]<15]["open_issues_only"], palette='Reds_d', ax=ax_issues[0])
sns.boxplot(y=df_issues[df_issues["open_issues_only"]<15]["open_issues_only"], data=df_issues, palette='Reds', width=0.3,boxprops={'zorder': 2},ax=ax_issues[0])
issues_closed = sns.violinplot(data=df_issues,  y=df_issues[df_issues["closed_issues_only"]<15]["closed_issues_only"], palette='Blues_d', ax=ax_issues[1])
sns.boxplot(y=df_issues[df_issues["closed_issues_only"]<15]["closed_issues_only"], data=df_issues,  palette='Blues', width=0.3,boxprops={'zorder': 2},ax=ax_issues[1])
issues_merged = sns.violinplot(data=df_issues, y=df_issues[df_issues["total_issues"]<15]["total_issues"], palette='Greens_d', ax=ax_issues[2])
sns.boxplot(y=df_issues[df_issues["total_issues"]<15]["total_issues"], data=df_issues, palette='Greens', width=0.3,boxprops={'zorder': 2},ax=ax_issues[2])



issues_opened.set(title='Opened issues across repositories')
issues_opened.set(xlabel='Repositories', ylabel='Opened Issues')

issues_closed.set(title='Closed issues across repositories')
issues_closed.set(xlabel='Repositories', ylabel='Closed Issues')

issues_merged.set(title='Opened and closed issues across repositories')
issues_merged.set(xlabel='Repositories', ylabel='Issues')

plt.tight_layout()
plt.savefig("Figures//issues.png")
plt.clf()


####################################
########## PULL REQUESTS ###########
####################################
prs_fig, ax_prs = plt.subplots(ncols=3,figsize=(15,10),sharey=True)

df_prs = pd.DataFrame(data = df_repos[['open_pull_requests','closed_pull_requests']])
df_prs['total_pull_requests'] = df_prs['open_pull_requests'] + df_prs['closed_pull_requests']

prs_opened = sns.violinplot(data=df_prs, y=df_prs[df_prs["open_pull_requests"]<15]["open_pull_requests"], palette='Reds_d', ax=ax_prs[0])
sns.boxplot(y=df_prs[df_prs["open_pull_requests"]<15]["open_pull_requests"], data=df_prs, palette='Reds', width=0.3,boxprops={'zorder': 2},ax=ax_prs[0])
prs_closed = sns.violinplot(data=df_prs, y=df_prs[df_prs["closed_pull_requests"]<15]["closed_pull_requests"], palette='Blues_d', ax=ax_prs[1])
sns.boxplot(y=df_prs[df_prs["closed_pull_requests"]<15]["closed_pull_requests"], data=df_prs,  palette='Blues', width=0.3,boxprops={'zorder': 2},ax=ax_prs[1])
prs_merged = sns.violinplot(data=df_prs, y=df_prs[df_prs["total_pull_requests"]<15]["total_pull_requests"], palette='Greens_d', ax=ax_prs[2])
sns.boxplot(y=df_prs[df_prs["total_pull_requests"]<15]["total_pull_requests"], data=df_prs, palette='Greens', width=0.3,boxprops={'zorder': 2},ax=ax_prs[2])



prs_opened.set(title='Opened pull requests across repositories')
prs_opened.set(xlabel='Repositories', ylabel='Opened Pull Requests')

prs_closed.set(title='Closed pull requests across repositories')
prs_closed.set(xlabel='Repositories', ylabel='Closed Pull Requests')

prs_merged.set(title='Opened and closed pull requests across repositories')
prs_merged.set(xlabel='Repositories', ylabel='Pull Requests')

plt.tight_layout()
plt.savefig("Figures//prs.png")
plt.clf()

####################################
########## COMMITS COUNT ###########
####################################
plt.figure(figsize=(15,10))

commits = sns.violinplot(data=df_repos, y=df_repos[df_repos["commits_number"]<250]["commits_number"], palette='Blues_d')
sns.boxplot(y=df_repos[df_repos["commits_number"]<250]["commits_number"], data=df_repos, palette='Blues', width=0.3,boxprops={'zorder': 2})

commits.set(title='Commits number across repositories')
commits.set(xlabel='Repositories')
commits.set(ylabel='Commits')

plt.xticks(rotation=45, ha='right')
plt.savefig("Figures//commits.png")
plt.clf()

#########################################
########## CONTRIBUTORS COUNT ###########
#########################################
plt.figure(figsize=(15,10))

contributors = sns.violinplot(data=df_repos, y=df_repos[df_repos["contributors_number"]<10]["contributors_number"], palette='Blues_d')
sns.boxplot(y=df_repos[df_repos["contributors_number"]<10]["contributors_number"], data=df_repos, palette='Blues', width=0.3,boxprops={'zorder': 2})

contributors.set(title='Contributors number across repositories')
contributors.set(xlabel='Repositories')
contributors.set(ylabel='Contributors')

plt.xticks(rotation=45, ha='right')
plt.savefig("Figures//contributors.png")
plt.clf()

###########################################
########## ORGANIZATION VS USER ###########
###########################################
plt.figure(figsize=(15,10))

organization = sns.histplot(df_repos['owner.type'], discrete=True, color='blue', kde=False)

organization.set(title='Owner type across repositories')
organization.set(xlabel='Owner type')
organization.set(ylabel='Repositories count')

plt.xticks(rotation=45, ha='right')
plt.savefig("Figures//organization_vs_user.png")
plt.clf()

# Repositories created per organization
df_organizations = df_repos.loc[df_repos['owner.type'] == 'Organization']
df_organizations['organization_name'] = df_organizations['full_name'].str.split('/',expand=True)[0]

df_organizations_repositories = df_organizations['organization_name'].value_counts().reset_index()
df_organizations_repositories.columns = ['Organization', 'Repositories developed']
df_organizations_repositories.to_csv('Output CSVs//total_number_of_repositories_developed_by_organizations.csv')

repositories_per_organization = df_organizations_repositories.plot(x='Organization',y='Repositories developed',kind='bar',legend=False,figsize=(15,10))

repositories_per_organization.set(title='GitHub repositories developer per organization')
repositories_per_organization.set(xlabel='Organization')
repositories_per_organization.set(ylabel='Repositories count')

plt.xticks(rotation=45, ha='right')
plt.savefig("Figures//repositories_per_organization.png")
plt.clf()

###################################
########## LICENSE TYPE ###########
###################################
plt.figure(figsize=(15,10))

license_type = sns.histplot(df_repos['license.key'], discrete=True, color='blue', kde=False)

license_type.set(title='Licenses type across repositories')
license_type.set(xlabel='License type')
license_type.set(ylabel='Repositories count')

plt.xticks(rotation=45, ha='right')
plt.savefig("Figures//licenses.png")
plt.clf()

# All licenses from the last 5 years - the gap contains leap years so there are 1827 days
till_5_years = pd.to_datetime(date.today() - datetime.timedelta(days=1827))

df_intermediary_license_5_years = pd.DataFrame(data = df_repos[['license.key', 'created_at']])
df_intermediary_license_5_years['created_at'] =  pd.to_datetime(df_intermediary_license_5_years['created_at'].str.slice(0,10),format='%Y-%m-%d')
df_intermediary_license_5_years = df_intermediary_license_5_years.sort_values(['created_at'])

df_intermediary_license_5_years = df_intermediary_license_5_years[df_intermediary_license_5_years['created_at']>=till_5_years]

df_license_5_years = df_intermediary_license_5_years['license.key'].value_counts().reset_index()
df_license_5_years.columns = ['License', 'Count']

license_5_years = df_license_5_years.plot(x='License',y='Count',kind='bar',legend=False,figsize=(15,10))

license_5_years.set(title='GitHub licenses used across repositories in the last five years')
license_5_years.set(xlabel='License')
license_5_years.set(ylabel='Repositories count')

plt.xticks(rotation=45, ha='right')
plt.savefig("Figures//licenses_last_5_years.png")
plt.clf()


###############################
########## REPO AGE ###########
###############################
plt.figure(figsize=(15,10))

df_age = pd.DataFrame(data = df_repos[['name','created_at','updated_at']])
df_age['created_at'] = pd.to_datetime(df_age['created_at'].str.slice(0,10),format='%Y-%m-%d')
df_age['updated_at'] = pd.to_datetime(df_age['updated_at'].str.slice(0,10),format='%Y-%m-%d')
df_age['days_age'] =  (df_age['updated_at'] - df_age['created_at']).dt.days

age = sns.violinplot(data=df_age, y=df_age['days_age'], palette='Blues_d')
sns.boxplot(y=df_age['days_age'], data=df_age, palette='Blues', width=0.3,boxprops={'zorder': 2})

age.set(title='Age expressed in days across repositories')
age.set(xlabel='Days')
age.set(ylabel='Repositories')

plt.savefig("Figures//age.png")
plt.clf()

#####################################
########## REPO FRESHNESS ###########
#####################################
plt.figure(figsize=(15,10))

df_freshness = pd.DataFrame(data = df_repos[['name','pushed_at']])
df_freshness['pushed_at'] = pd.to_datetime(df_freshness['pushed_at'].str.slice(0,10),format='%Y-%m-%d')
df_freshness['today_at'] = pd.to_datetime(date.today().strftime('%Y-%m-%d'))

df_freshness['freshness_days'] =  (df_freshness['today_at'] - df_freshness['pushed_at']).dt.days

freshness = sns.violinplot(data=df_freshness, y=df_freshness['freshness_days'], palette='Blues_d')
sns.boxplot(y=df_freshness['freshness_days'], data=df_freshness, palette='Blues', width=0.3,boxprops={'zorder': 2})

freshness.set(title='Freshness expressed in days across repositories')
freshness.set(xlabel='Repositories')
freshness.set(ylabel='Freshness as days')

plt.savefig("Figures//freshness.png")
plt.clf()


