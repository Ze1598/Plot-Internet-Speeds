# Plot-Internet-Speeds
Test internet speeds; save results to a .txt and .csv file; plot graphs with the data

This repository contains 2 scripts: the first one, getInternetSpeeds.py tests the current internet speeds and writes the results to a .txt file; the second script, plot_internet_speeds.py, reads the data from the .txt file and plots a graph for each type of speed

Note: I stopped collecting data in March 31st 2019.

### Structure
* root
  * getInternetSpeeds2.py -> script to scrape my internet speeds and save the results to a .txt and a .csv file
  * InternetSpeeds.txt -> file to store the test results (this one includes the time of each test)
  * internet_speeds.csv -> dataset with all the daily internet speeds scraped so far
* data analysis -> contains a script to analyze the data using matplotlib, pandas and numpy (contains sample output graphs)
  * Internet_Speeds_Data_Analysis2.py -> script to analyze the data

### Update log:
* (mar. 28th 2018) Updated the main script to take outliers into consideration; also added more recent graph screenshots
* (jan. 3rd 2019) Reuploaded all files in the repo to clean up and organize folders. These are the latest files which I am currently using to scrape my internet speeds once per day at home
* (feb. 26th 2019) Updated the repo with the most recent dataset
* (june 16th 2019) Updated with the latest dataset
* (july 12th 2019) Added a new CSV called "internet_speeds_days" that contains three extra columns, one to represent each date component for each row (i.e., added a "Year", "Month" and "Day" columns)

### External references:
* pyspeedtest: https://github.com/fopina/pyspeedtest (Not using this module anymore)
* Matplotlib: https://matplotlib.org/
* speedtest-cli https://github.com/sivel/speedtest-cli
