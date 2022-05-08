# ASEC_Tool_and_Analysis
<<<<<<< HEAD

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

Using the 'hh_to_pp.py' script, ensure you have downloaded the respective pppub and hhpub CSVs with the years you wish to use. The code has all three years, so it can be modified to work with any of the currently published years. It is heavily recommended that you run the code CELL BY CELL instead of all at once to make the process easier on your computer. The variables pppub21,pppub20, and pppub19 contain the information from the respective personal CSV files, and hhpub21-hhpub19 do the same for the household information.

The dictionary hh_person_names is necessary because the H_SEQ variable and PH_SEQ are the same value in both the pppub and hhpub CSVs; this is how individuals are tied to specific households within the data. We have to rename H_SEQ to PH_SEQ because we will merge the household data with personal data. This way, we can now tie location data to individuals. I used a left join for this process because we want to work with personal data as it has the more descriptive information we are interested in. Additionally, personal data has more variables to work with than households or family. It is also easier to work with personal data when looking for a more robust analysis.  

I concatenated all of the years into one workable data frame, 'pp_hh_data' using the list' pp_hh_concact_list' and the pd.concact function. If a project only requires you to work with a set of information from one year, you can delete this section; if you do, be sure to rename the resulting merge data frame such as 'pp_hh_21merge' to 'pp_hh_data' so that you do not have to modify the rest of the script. I also dropped the merge indicator '_merge' from the new data frame because it is unnecessary to the rest of the script. The 'pp_hh_data_list' is where you can place the chosen variables you wish to work with. Be sure to copy the information directly from the dictionary and put them in the list. By placing these variables in the list, you can determine the number of columns in the data frame and by extension the csv. I suggest keeping variables 'PH_SEQ', 'PPPOS', 'GTCBSA', 'GESTFIPS', and 'GTCO' because these are used to identify an individual respondent and their specific location. If a project required any mapping, it would be handy to have this.

I used the dictionary 'pp_new_names' to rename the columns to something a bit more identifiable to work with. After choosing the data you wish to work with, the script drops and field with na as the value, which is a residual from the merge function performed earlier. For easier identification of individuals, I created the 'PSID' column, which is the concatenation of 'PH_SEQ' and 'PPPOS'; this will now show a specific individual within a particular household and forms an individual respondent's data-id number.

For the information involving 'County' since the information was not properly put into the CSV to ensure that the county code of an individual was intact, I had to use the .str.zfile(3) function to add in the extra zeros that were left out. Afterward, I concatenated the 'FIPS' and 'County' codes of individuals to make their 'GEOID' so that now an individual could be properly mapped in a program such as QGIS with other Census shapefiles.

I finally dropped any duplicate 'PSID' numbers from the data frame so that we can make sure individuals are not being included twice since this script is using the information from 2019 to 2021. If the project wants to look at specific individuals from year to year, you would have to modify this line of code.

Finally, I set the 'PSID' as the index for the data frame for ease of identification, and then the script turns the 'pp_hh_data' data frame into a CSV.

Most of these steps can be repeated for the other scripts' ff_to_pp.py', and 'hh_to_ff.py', with slight modifications. Since there is no geographic-related data in the families or personal CSVs, you cannot use variables relating to CBSA, FIPS, or County codes. In the script 'ff_to_pp.py' this was distinctly left out of the variable list. Since there are no personal ID numbers in the household or family CSVs, variables' PH_SEQ' and 'PPPOS' were left out. Instead, what is used for the merge in this script 'FH_SEQ' after the 'H_SEQ' was renamed to 'FH_SEQ', much like 'H_SEQ' was renamed to 'PH_SEQ'.

### An Analysis



=======
A tool created to work with the ASEC information from 2019 onward, and an analysis of the quality of data itself.
>>>>>>> faf7acbd224d596d57ecf526f41ec0c607b4af5e
