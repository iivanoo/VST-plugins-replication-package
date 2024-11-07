# VST Plugins – Replication package

## Overview of the replication package
This replication package is structured as follows:

    |--- Quantitative analysis/         The scripts utilized and the data extracted during the analysis.
    |--- Repositories data/   	    The scripts utilized and the data extracted during the mining process of VST Plugins repositories on GitHub.

    
Each of the folders listed above are described in details in the remaining of this readme.

## Quantitative analysis

    |--- CSVs Used                                     Contains the CSVs files utilized for quantitative analysis.   
    |--- Figures                                       Contains the figures outputted from the "quantitative_analysis_script.py" Python script.
    |--- Output CSVs                                   Contains additional CSVs files outputted from the "quantitative_analysis_script.py" Python script, that were utilized at a later stage for this study.
    |--- Descriptive Statistics.csv                    The descriptive statistics of the mined repositories.
    |--- rq1.ipynb                                     The Jupyter Notebook in Python utilized for generating the plots and the descriptive statistics that are required for answering RQ1.
    |--- rq2.ipynb                                     The Jupyter Notebook in Python utilized for generating the plots and the descriptive statistics that are required for answering RQ2.
    |--- rq3.ipynb                                     The Jupyter Notebook in Python utilized for generating the plots and the descriptive statistics that are required for answering RQ3.


## Repositories data
  
	|--- Cloned repositories                  	Contains the SonarQube reports alongside the Python script responsible for cloning the repositories mentioned in the CSVs Used subfolder. 
        |--- CSVs Used                       	Contains the final repositories dataset as a CSV file, which was utilized only for the sole purpose of gathering the repositories' names by the "mine_repo_data.py" Python script.
        |--- SonarQube reports               	Contains the SonarQube compressed reports of all repositories. 
        |--- mine_repo_data.py               	The Python script responsible for cloning the repositories
	|--- repo_final_mined_data              	Contains the original repositories demographic data, after applying the inclusion and exclusion protocol.
        |--- contributors                   	Contains the details about each contributor.
        |--- curated_csv                     	Contains the final CSVs files utilized for the quantitative analysis.
        |--- issue                           	Contains the issue's contents per repositories.
        |--- languages                       	Contains all the programming languages utilized across repositories, not just the primary one.
        |--- raw_csv                         	Contains the merged JSON files as CSV files. Those CSV files also contain out-of-scope fields but without duplicates.
        |--- raw_uncurated_csv               	Contains the merged JSON files as CSV files. Those CSV files also contain out-of-scope fields but with duplicates + empty rows.
        |--- users                           	Contains the details about each user.
        |--- *.json                          	Contains the JSON files that are merged from the folder "repo_demographic_mined_data".
	|--- repo_demographic_mined_data         	Contains the demographic repositories data utilized for the quantitative analysis, not merged, as JSON files.
        |--- more_data                       	Contains data that was additionally mined.
             |--- commit_count               	Contains the commit count as JSON files for each repository.
             |--- contributor_count          	Contains the contributors count as JSON files for each repository.
             |--- in_depth_details           	Contains the in-depth details as JSON files for each repository.
             |--- issue_count                	Contains the issues count as JSON files for each repository.
             |--- pr_count                   	Contains the pull requests count as JSON files for each repository.
        |--- *.json                          	The JSON files that represent the topics utilized across repositories.
	|--- mine_repo_data.py                   	The Python script responsible for mining the repositories demographic data through Git REST API.analysis of the contents of the repositories
