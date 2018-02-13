from os import system

#Run the script that tests the current internet speeds and saves it to .txt file
system("python getInternetSpeeds.py")

#Open the file with the dates and internet speeds in read mode
with open('InternetSpeeds.txt', 'r') as f:
    #Create a list where each item is a line from the file
    lines = list(f.readlines())
    #Create a list to contain all the dates in the file
    dates = [lines[i][11:16].strip() for i in range(0, len(lines), 5)] #MM-DD
    #Create a list to contain all the ping speeds in the file (units not included)
    ping_speeds = [lines[i][6:-3].strip() for i in range(1, len(lines), 5)] #ms
    #Create a list to contain all the download speeds in the file (units not included)
    download_speeds = [lines[i][10:-5].strip() for i in range(2, len(lines), 5)] #mb/s
    #Create a list to contain all the upload speeds in the file (units not included)
    upload_speeds = [lines[i][8:-5].strip() for i in range(3, len(lines), 5)] #mb/s

#https://matplotlib.org/
from matplotlib import pyplot
'''Dates/Ping Graph'''
#Plot a graph where the x-values are the dates extracted and the y-values are the ping values
#Use a red line for the plotting
pyplot.plot(dates, ping_speeds, 'r')
#Label the axis
pyplot.xlabel('Dates')
pyplot.ylabel('Ping values in ms')
#Plot the graph in a new window
pyplot.show()

'''Dates/Download_Speeds Graph'''
#Plot a graph where the x-values are the dates extracted and the y-values are the download speeds
#Use a green line for the plotting
pyplot.plot(dates, download_speeds, 'g')
#Label the axis
pyplot.xlabel('Dates')
pyplot.ylabel('Download speeds in mb/s')
#Plot the graph in a new window
pyplot.show()

'''Dates/Upload_Speeds Graph'''
#Plot a graph where the x-values are the dates extracted and the y-values are the upload speeds
#Use a blue line for the plotting
pyplot.plot(dates, upload_speeds, 'b')
#Label the axis
pyplot.xlabel('Dates')
pyplot.ylabel('Upload speeds in mb/s')
#Plot the graph in a new window
pyplot.show()
