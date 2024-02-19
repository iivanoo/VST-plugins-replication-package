# library & dataset
import seaborn as sns
import pandas as pd 
import matplotlib.pyplot as plt
import scipy
import numpy as np
from datetime import date
import datetime
import matplotlib.ticker as mtick
import ast



# dataframe for repos data
df_repos = pd.read_csv('CSVs Used//VSTs_Qualitative_Metrics.csv')
df_scp = pd.read_csv('CSVs Used//scp_tangled.csv')
df_libraries = pd.read_csv('CSVs Used//libraries.csv')


#########################################
########## REPO FUNCTIONALITY ###########
#########################################

plt.figure(figsize=(100,10))

functionality = sns.histplot(df_repos['functionality'], discrete=True, color='blue', kde=False)

functionality.set(xlabel='Functionality')
functionality.set(ylabel='Repositories count')

plt.xticks(rotation=45, ha='right')
plt.savefig("Figures//functionality.png")
plt.clf()

plt.figure(figsize=(15,10))

core_functionality = sns.histplot(df_repos['core functionality'].str.strip(), discrete=True, color='blue', kde=False)

core_functionality.set(xlabel='VST plugin type (VSTfx = effect or VSTi = virtual instrument)')
core_functionality.set(ylabel='Repositories count')

plt.xticks(rotation=45, ha='right')
plt.savefig("Figures//core_functionality.png")
plt.clf()


#########################################
########## FRAMEWORKS != JUCE ###########
#########################################

plt.figure(figsize=(15,10))

frameworks = sns.histplot(df_repos['frameworks (others than JUCE)'].str.strip(), discrete=True, color='blue', kde=False)

frameworks.set(xlabel='Other frameworks than JUCE used')
frameworks.set(ylabel='Repositories count')

plt.xticks(rotation=45, ha='right')
plt.savefig("Figures//other_frameworks.png")
plt.clf()


##############################
########## TESTING ###########
##############################

plt.figure(figsize=(15,10))

testing = sns.histplot(df_repos['testing'].str.strip(), discrete=True, color='blue', kde=False)

testing.set(xlabel='Did the developers tested their repositories\ code?')
testing.set(ylabel='Repositories count')

plt.xticks(rotation=45, ha='right')
plt.savefig("Figures//tested_repositories.png")
plt.clf()


##################################
########## SCP TANGLED ###########
##################################

plt.figure(figsize=(20,20))

scp = sns.histplot(df_scp['SonarQube violations (SCP)'].str.strip(), discrete=True, color='blue', kde=False)

scp.set(xlabel='Standard code practices tangled')
scp.set(ylabel='Repositories count')

plt.xticks(rotation=45, ha='right')
plt.savefig("Figures//scp_tangled.png")
plt.clf()

#########################
########## QG ###########
#########################

plt.figure(figsize=(15,10))

qc = sns.histplot(df_repos['SonarQube quality gate status (passed,failed)'].str.strip(), discrete=True, color='blue', kde=False)

qc.set(xlabel='SonarQube quality gate status')
qc.set(ylabel='Repositories count')

plt.xticks(rotation=45, ha='right')
plt.savefig("Figures//qgs.png")
plt.clf()


###############################
########## COMMENTS ###########
###############################

plt.figure(figsize=(15,10))

comments = sns.histplot(df_repos['Comments'].str.strip(), discrete=True, color='blue', kde=False)

comments.set(xlabel='The presence of explanatory comments across the repositories\' code')
comments.set(ylabel='Repositories count')

plt.xticks(rotation=45, ha='right')
plt.savefig("Figures//comments.png")
plt.clf()

#######################################
########## TYPE OF C++ LIBS ###########
#######################################

plt.figure(figsize=(15,10))

hf_compiled = sns.histplot(df_repos['Header files or compiled library files'].str.strip(), discrete=True, color='blue', kde=False)

hf_compiled.set(xlabel='The library type used for repositories written in C/C++ (header files or/and compiled library files)')
hf_compiled.set(ylabel='Repositories count')

plt.xticks(rotation=45, ha='right')
plt.savefig("Figures//header_or_compiled_library.png")
plt.clf()

################################
########## LIBRARIES ###########
################################

plt.figure(figsize=(30,30))

hf_compiled = sns.histplot(df_libraries['Libraries'].str.strip(), discrete=True, color='blue', kde=False)

hf_compiled.set(xlabel='Libraries used across repositories')
hf_compiled.set(ylabel='Repositories count')

plt.xticks(rotation=45, ha='right')
plt.savefig("Figures//library.png")
plt.clf()