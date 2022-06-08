# Bikeshare Data Analysis

## Project Overview:
Bicycle-sharing systems allow users to rent bicycles on a very short-term basis for a price. This allows people to borrow a bike from point A and return it at point B, though they can also return it to the same location if they'd like to just go for a ride. Regardless, each bike can serve several users per day.

## Task:
Using Python, The purpose of this project is to use data provided by [Motivate](https://www.motivateco.com/), a bike share system provider for many major cities in the United States, to uncover bike share usage patterns. We will compare the system usage between three large cities: Chicago, New York City, and Washington, DC.

## Criteria:
#### A- Interactive program
1- User can choose which data set to display analysis for.<br>
2- User can choose the month and day of week to display analysis for.<br>


#### B- Statistics to be displayes
1- Popular times of travel:
- Most common month
- Most common day of week.
- Most common hour of day.<br>

2- Popular stations and trip:
- Most common start station.
- Most common end station.
- Most frequent combination of start station and end station.<br>

3- Trip duration:
- Total travel time.
- Average travel time.<br>

4- User info:
- Counts of each user type.
- Counts of each gender (only available for NYC and Chicago).
- Earliest, most recent, most common year of birth (only available for NYC and Chicago).
    
    
#### C- Exceptions handling
- The program should handle any input from the user without crashing.


## Files:
1- bikeshare_data_analysis.py
- Source Code.<br>

2- datasets.rar:
- chicago.csv (Data base file).
- new_york_city.csv (Data base file).
- washington.csv (Data base file).


## Datasets Desribrtion:
Randomly selected data for the first six months of 2017 are provided for all three cities. All three of the data files contain the same core six (6) columns:
- Start Time (e.g., 2017-01-01 00:07:57)
- End Time (e.g., 2017-01-01 00:20:53)
- Trip Duration (in seconds - e.g., 776)
- Start Station (e.g., Broadway & Barry Ave)
- End Station (e.g., Sedgwick St & North Ave)
- User Type (Subscriber or Customer)<br><br>
*The Chicago and New York City files also have the following two columns:*
- Gender
- Birth Year

![image](https://user-images.githubusercontent.com/100201370/172537744-def795fd-be22-47ed-84e3-bc0b47af4072.png)


## Libraries used in the code:
- pandas
- numpy
- time
- datetime
  
  
## Run locally:
1- Download all files (bikeshare_data_analysis, chicago.csv, new_york_city.csv, washington.csv)<br>
2- Make sure that all files are in the same folder.<br>
3- From the command line<br>
python bikeshare_data_analysis.py
