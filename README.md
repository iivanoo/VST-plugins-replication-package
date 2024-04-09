# Thesis-VST-replication-package
Replication package of my thesis entitled "Characterising the Development Practices of Virtual Studio Technology (VST) Plugins"<br><br>

**Navigation:**<br>
- **"Repositories data folder"** includes the followings:
  - **"repo_demographic_mined_data" folder** contains the JSONs with all the queries results, basically everything that the GET Requests from the script mined.
  - **"repo_final_mined_data" folder** contains all JSONs from "repo_demographic_mined_data" but merged, the names of the files are suggestive and self-explanatory for what was merged inside that file.
    - **"raw_csv" folder** contains all JSONs from "repo_demographic_mined_data" but merged and converted to csv format, the names of the files are suggestive and self-explanatory for what was merged inside that file .
    - **"raw_uncurated_csv" folder** contains as csvs the following JSONs:
        - *final_data_uncurated.csv = all mined data gathered, merged by GitHub Repository URL and in one single csv file, with duplicates* . 
        - *contributors_and_commits_count_raw.csv =  mined_repo_contributors_count.json + mined_repo_commits_count.json*.
        - *issues_count_raw.csv = mined_repo_issues_count_closed.json + mined_repo_issues_count_opened.json*.
        - *prs_count_raw.csv = mined_repo_prs_count_closed.json + mined_repo_prs_count_opened.json*.
    - **"curated_csv" folder** contains all csvs from *raw_uncurated_csv* folder but without duplicates and only the fields of interest and the final csv for the final dataframe:
      - *final_data_curated.csv = final dataframe*.
      - *in_depth_selected_details.csv - from mined_repo_in_depth_details.json*.
      - *issues_final.csv from issues_count_raw.csv*.
      - *prs_final.csv from prs_count_raw.csv*.
- **"Quantitative analysis" folder** contains the Python script that does the quantitative analysis plots which outputs them under **"Figures" folder** and it is using the csvs files from **"CSVs Used" folder**.
- **"Qualitative analysis" folder** contains the **"Codes.docx"** and **"Themes.docx"** files which represents the thematic analysis codes and themes of the repositories' issues content, the CSV used for this particular analysis can be found at:  *Quantitative analysis/Output CSVs/Issues_content_until_27.09.2023.csv*.
<br><br>
