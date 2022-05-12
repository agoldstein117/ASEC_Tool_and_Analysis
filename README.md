# ASEC_Tool_and_Analysis


## Summary 

The goal of this project was to create a tool that others could use for future projects relating to the Census Bureau's Annual Social and Economic Supplements (ASEC). The ASEC provides survey answers from hundreds of thousands of individuals within the US. The ASEC collects information from 245k unique individuals on topics relating to their work, income, noncash benefits, migration, demographics, and other related topics. The ASEC contains over 900 different variables available to use for a wide variety of analyses. Until 2019, the Census Bureau provided this data in CSV form, making it more easily usable for python-based projects. The information is categorized into three distinct CSVs personal, family, and household.

The personal CSV relates to a singular respondent's personal information. This is the CSV where you would find individual income, an individual's demographic information, occupational history, or educational history. The family CSV contains information regarding an individual's family unit, such as the number of individuals in a family, family composition type, and total family income. The household information contains information regarding total household income, the number of individuals in the household, and the specific geographic data related to individuals and families.

Due to the size of the overall data, it is pretty challenging for some computers to run this data quickly. This tool not only merges the data from each CSV into useable pairs that make the data more comprehensive, but it also allows users to choose the specific variables they wish to work with for future analysis. This allows computers to work with the data faster, but more importantly, it ensures that an individual's computer does not crash as they are working with such large files.

The ASEC data does not allow for someone to merge all three CSV types into one data frame, so this tool has created three merged pairs that users can choose to work with for future projects. If a user wants to work with information from both the personal CSV and the household CSV, using script 'hh_to_pp.py' will allow the individual to merge the two CSVs into one workable data frame 'pp_hh_data'. The script will also convert the data frame into a CSV called 'pp_hh_data.csv'. This script also allows individuals to choose the specific information they wish to work with from both the personal CSV and the household CSV by enabling the individual to select the variables they want from both data sets. A similar process can be done for each subsequent pair between the families and household CSVs, and the families and personal CSVs. If users want to work with the families and household CSVs they can modify this information in the 'hh_to_ff.py' script. If users wish to work with the families and personal CSVs, they can use the 'ff_to_pp.py' script. Each script also produces a subsequent csv users can use for other projects outside of python.

## Where to Find the Data

There are two essential components a user must have before they can work with this data they need the actual CSVs from the ASEC, and they need the data dictionary. To find both of these components, please follow this link: [Please click this link to the ASEC data page.]( https://www.census.gov/data/datasets/time-series/demo/cps/cps-asec.2021.html) On this webpage, you can choose to work with data from a specific year; from 2019 to 2021 is where you will find the CSV information. This tool allows users to work with data from all three years. There are four sections on each page; however, the two most important sections to use for this tool are the section Technical Documentation, Data and Documents. Technical Documentation gives a rundown and explanation of the data itself. Data and Documents contain the Data Dictionary, which holds all the descriptive information of the variables within the CSV. This is important because otherwise, you will not be able to understand the information within the data frame. The following important section is the information itself which is located under CSV Data File. Click on CSV, and it will download a zip file you will then have to unpack for each of the CSVs.

Once you have completed that, you can place the CSV(s) you wish to work within this repository and start working with the data; happy coding!

## An Explanation on How to Use the Tool, an Analysis, and a Demonstration

### Overview
Since the data merging scripts are relatively similar, I will be using the script 'hh_to_pp.py' to demonstrate how to use the tool. Following that, I will be using the information created by this script in a following script 'quality_analysis.py' to show where there may be holes within the data provided by the ASEC and to show others how they can check to see if their data may be lacking if they wish to use it. Finally, I will go through a third script, 'state_unemployment.py', which is a demonstration of how to use the information; in this instance, it is to show unemployment by state and occupation and how unemployment by occupation differs from state to state.

### How to Use the Tool

Using the 'hh_to_pp.py' script, ensure you have downloaded the respective pppub and hhpub CSVs with the years you wish to use. The code has all three years, so it can be modified to work with any of the currently published years. It is heavily recommended that you run the code CELL BY CELL instead of all at once to make the process easier on your computer. Be sure when you read the information into a data frame using pd.read_csv that the dtype is str as the scripts will not work if it is in int or float format. If you wish to work with ints or floats I would suggest converting certain columns into that dtype. The variables pppub21,pppub20, and pppub19 contain the information from the respective personal CSV files, and hhpub21-hhpub19 do the same for the household information.

The dictionary hh_person_names is necessary because the H_SEQ variable and PH_SEQ are the same value in both the pppub and hhpub CSVs; this is how individuals are tied to specific households within the data. We have to rename H_SEQ to PH_SEQ because we will merge the household data with personal data. This way, we can now tie location data to individuals. I used a left join for this process because we want to work with personal data as it has the more descriptive information we are interested in. Additionally, personal data has more variables to work with than households or family. It is also easier to work with personal data when looking for a more robust analysis.  

I concatenated all of the years into one workable data frame, 'pp_hh_data' using the list' pp_hh_concact_list' and the pd.concact function. If a project only requires you to work with a set of information from one year, you can delete this section; if you do, be sure to rename the resulting merge data frame such as 'pp_hh_21merge' to 'pp_hh_data' so that you do not have to modify the rest of the script. I also dropped the merge indicator '_merge' from the new data frame because it is unnecessary to the rest of the script. The 'pp_hh_data_list' is where you can place the chosen variables you wish to work with. Be sure to copy the information directly from the dictionary and put them in the list. By placing these variables in the list, you can determine the number of columns in the data frame and by extension the csv. I suggest keeping variables 'PH_SEQ', 'PPPOS', 'GTCBSA', 'GESTFIPS', and 'GTCO' because these are used to identify an individual respondent and their specific location. If a project required any mapping, it would be handy to have this.

I used the dictionary 'pp_new_names' to rename the columns to something a bit more identifiable to work with. After choosing the data you wish to work with, the script drops and field with na as the value, which is a residual from the merge function performed earlier. For easier identification of individuals, I created the 'PSID' column, which is the concatenation of 'PH_SEQ' and 'PPPOS'; this will now show a specific individual within a particular household and forms an individual respondent's data-id number.

For the information involving 'County' since the information was not properly put into the CSV to ensure that the county code of an individual was intact, I had to use the .str.zfile(3) function to add in the extra zeros that were left out. Afterward, I concatenated the 'FIPS' and 'County' codes of individuals to make their 'GEOID' so that now an individual could be properly mapped in a program such as QGIS with other Census shapefiles.

I finally dropped any duplicate 'PSID' numbers from the data frame so that we can make sure individuals are not being included twice since this script is using the information from 2019 to 2021. If the project wants to look at specific individuals from year to year, you would have to modify this line of code.

Finally, I set the 'PSID' as the index for the data frame for ease of identification, and then the script turns the 'pp_hh_data' data frame into a CSV.

Most of these steps can be repeated for the other scripts' ff_to_pp.py', and 'hh_to_ff.py', with slight modifications. Since there is no geographic-related data in the families or personal CSVs, you cannot use variables relating to CBSA, FIPS, or County codes. In the script 'ff_to_pp.py' this was distinctly left out of the variable list. Since there are no personal ID numbers in the household or family CSVs, variables' PH_SEQ' and 'PPPOS' were left out. Instead, what is used for the merge in this script 'FH_SEQ' after the 'H_SEQ' was renamed to 'FH_SEQ', much like 'H_SEQ' was renamed to 'PH_SEQ'. Finally in the script 'ff_to_pp.py' since there is too much information to merge all at once there are two lists for variables to be chosen from the personal and family CSVs. By modifying these lists you can choose the specific variables you wish to work with from both data sets.

### An Analysis

Before any data should be used for analysis, it is good to know where the information is from, how best to use it, and if there are any holes. The script 'quality_analysis' was designed to assist individuals with this endeavor. The script allows individuals to know how many entries are in the chosen variables. Using the data from 'pp_hh_data' I demonstrate how this script can be used. While this script provides good insight into the data from the ASEC, the relative same process was used for each variable, so it is easy for others to use for other variables that may not have been included.

The first step that this script does is it groups the data by the variable in question and then counts the number of individuals who have the same values for each survey response. For example, in the first cell, a new series was created 'grouped_cbsa' where the data frame 'pp_hh_data' was grouped by the 'CBSA' variable. Then the functions .size().sort_values() was used to show which survey answer had the most amount of entries. 

Going to the Variable explorer and clicking on the data frame 'grouped_cbsa' will display how many individuals are located in each CBSA code. To let others know what percentage of the CBSA codes are missing from individuals, I created the variable miss_CBSA, which is equal to the value counts of 0 in the CBSA column. When an entry is missing, the ASEC typically puts 0 as an individual's response. To find the percentage, I divided 'miss_CBSA' by 'total_cbsa' which is the length of all the entries within the CSBA column, and then I multiplied the result by 100. I set this to the variable 'prct_miss' which I then rounded to the 2nd decimal place and printed the results. When the function runs, it will show what percent of all of the entries in the data frame have missing CBSA data which is about, 24.2%.

To show the percentages of how many respondents are from each CBSA, I turned the series' grouped_cbsa' into the data frame 'cbsa_df' using the to_frame() function. I then renamed the column with all of the value count numbers with the column name 'Count'. Then I created the column 'Percentage' in the 'cbsa_df' to show the individual percentage following the same formula for how I found the missing entries. If an individual were to wish to know how many entries are from each CBSA all they would have to do is click on the 'cbsa_df' in the Variable Explorer.

I repeated this step multiple times for various variables, finding the percentages for each one. However, I highlighted some of the results to understand where there may be bias in the ASEC data. The results of these findings show:

Regional Information:
* While 100% of the data has FIPS code information, 58.08% of the entries have no county code information. Including the 24.2% of missing CBSA data the information from the ASEC is not terribly suitable for mapping. Results from mapping the information may not be as informative as one would hope.
* Looking into the regions of where the respondents live about 18.29% of the entries are located in the South Atlantic Region, 16.08% located in the Pacific Region, and 12.73% are located in the Mountain Region.
* Looking into the FIPS codes  of where the respondents live about 9.5% of the entries have a Californian FIPS code, 6.18% of the FIPS codes are Texan, and 4.55% of the FIPS codes are Floridian.

Racial Information:
* Going into the demographic information of the about 76.63% of all of the responses are from White only individuals. 
* About 23.37% of all of the responses are from Non White individuals, about 11.71% of all responses are from Black only individuals, and about 6.51% of the responses are from Asian only individuals.

Employment Information:
* 42.78% of all of the responses are from employed individuals.
* Only 2.47% of all of the responses are unemployed individuals.

Occupation Type:
* 10.69% of the respondents have a job in the professional and related field.
* 7.91% have a management, business, or financial related occupation
* 7.88% have a service based career.

To find a more in-depth understanding if you were to go into any of the data frames in this script that are denoted by the variable name followed by _df it will give you a better glimpse at the data.

Near the end of the script, there are cells where someone can graph the percentages of each variable. This is to show a more visual representation of the data to show where there is a possibility of selection bias occurring within the data. These figures can be easily changed to suit the need of the user.

I will be going over the graph saved as 'fips_figure.png' as an example. The graph uses the fips_df with the y equal to the percentage column, a font size of 7, and with the legend set to false. This is to show the percentage of responses by state. One could easily change the source of information by changing fips_df to another data frame with descriptive details of another variable made previously in the script. The graph has a dpi of 300 and a tight layout to ensure easy visibility.

This script was used to show the descriptive information within the personal file, but it can be modeled in a way that works for any of the other information provided by the ASEC.

### A Demonstration

As seen above, the information from the ASEC is not the best for mapping. To best showcase the data of the ASEC, I would suggest analysis through other means, either through regression or graphs.

To demonstrate this, I will show Unemployment by Occupation and Unemployment by State; then, I will show how Unemployment by Occupation differs between States.  

Using the data from 'pp_hh_data' since we only need information from those who we unemployed, I set the variable 'state_um' equal to a query where "Unempoyment_Status ==' 2'". Then I grouped this information by 'FIPS' and sorted the values by the number of entries in each FIPS. I then created a data frame from this series and renamed the column with the necessary information to 'Number of Unemployed'. I then reset the index to make it easier to work with for future calculations. I then repeated these same actions, except I got the information from employed individuals by setting the query to "Unempoyment_Status ==' 1'". This new data frame with all the information of those who were employed by the state is denoted by the variable 'state_em'.

I then merged the data frames' state_em' and 'state_um' into the data frame 'unemploy_merge' because I will need to know the total number of employed for each state. I dropped the merge indicator for 'unemploy_merge', because I do not need it. I then created the 'Total' column within the data frame 'unemploy_merge', which concatenates 'Number of Employed' and the "Number of Unemployed'. I then found the percentages of unemployed for each state by dividing 'Number of Unemployed' by 'Total', multiplying it by 100, and rounding it to the second decimal place.

From the results I made the graph 'f1_state_unem.png' which shows the Unemployment Rate by State:

![alt text](https://github.com/agoldstein117/ASEC_Tool_and_Analysis/blob/main/f1_state_unem.png)

I then repeated the same steps for Occupation Type and produced the graph that shows Unemployment by Occupation type:

![alt text](https://github.com/agoldstein117/ASEC_Tool_and_Analysis/blob/main/f1_occ_unem.png)

Looking at the graph, we can see that the two states with the highest Unemployment were California and Texas. For Occupations, the two Occupation Types with the highest levels of Unemployment were transportation and material moving occupations and construction and extraction occupations. To determine the Unemployment Rate by Occupation Type within States, I first created a new data frame that only had unemployed individuals. I did this by setting data frame 'geo_um' to a query with "Unempoyment_Status ==' 2'". I then grouped the information within 'geo_um' by 'FIPS' and 'Occupation_Type'. 

I followed the same methods as I preciously did to make the data frame 'geo_um_df' which contains the unemployment information by occupation type. Then I followed the same steps, except I worked with information of employed individuals by using data frame 'geo_em' set to a query where "Unempoyment_Status ==' 1'". I then created another data frame, 'geo_em_df', which grouped the information by 'FIPS' and 'Occupation_Type'. 

Following this I then merged the data frames ‘geo_em_df’ and ‘geo_um_df’, using an inner merge and merged left on ['FIPS','Occupation_Type'] and right on ['FIPS','Occupation_Type'].From there I performed the same tasks I did to get the previous 'Total' and 'Percentage' columns from the earlier data frames. After calculating the Unemployment Rate by Occupation Type by State, I dropped columns' Number of Employed', 'Number of Unemployed', and 'Total' as I did not need them anymore. The final data frame with all of this information was 'um_occ_state'.

Since there is too much information to graph, I decided to choose two states to showcase the differences. I chose California and Texas as these two had some of the highest unemployment rates and have some of the most responses within the data itself, which is what we learned from the previous analysis. I created a new data frame using a query where "FIPS ==' 6' or FIPS ==' 48'" to get only California and Texas data. Then I renamed the FIPS codes for these states to their names using the dictionary 'um_state_dict' and using the replace function. I finally graphed the information using a seaborn bar plot where x was the Occupation Type, y was the Unemployment Rate, and FIPS was the Hue. I set the graph to a 300 dpi and a tight layout for the best visual quality and saved the figure as 'f1_compa.png'.

Here are the results of this analysis

Occupation Type:

1 = Management, business, and financial occupations          
2 = Professional and related occupations          
3 = Service occupations          
4 = Sales and related occupations          
5 = Office and administrative support occupations          
6 = Farming, fishing, and forestry occupations          
7 = Construction and extraction occupations          
8 = Installation, maintenance, and repair occupations          
9 = Production occupations         
10 = Transportation and material moving occupations         
11 = Armed Forces

![alt text](https://github.com/agoldstein117/ASEC_Tool_and_Analysis/blob/main/f1_compa.png)


We can see that California had higher instances of Unemployment for farming, fishing, forestry, and service occupations. In contrast, Texas had higher Unemployment Rates for construction, extraction, transportation, and material moving occupations.

## Final Remarks 

Now that you know where to find the ASEC data and use this tool to work with and analyze the ASEC data efficiently, you should be able to proceed with your own analysis projects more easily. Happy Coding!


