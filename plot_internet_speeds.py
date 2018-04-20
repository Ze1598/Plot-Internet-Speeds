from os import system
#http://www.numpy.org/
import numpy as np
#https://matplotlib.org/
from matplotlib import pyplot as plt

def visualize_data(file_path):
    #Run the script that tests the current internet speeds and saves it to .txt file
    #system("python getInternetSpeeds.py")

    #Open the file with the dates and internet speeds in read mode
    with open(file_path, 'r') as f:
        #Create a list where each item is a line from the file
        lines = list(f.readlines())
        #Create a list to contain all the dates in the file
        dates = [lines[i][11:16].strip() for i in range(0, len(lines), 5)] #MM-DD
        #Create a list to contain all the ping speeds in the file (units not included)
        ping_speeds = [float(lines[i][6:-3].strip()) for i in range(1, len(lines), 5)] #ms
        #Create a list to contain all the download speeds in the file (units not included)
        download_speeds = [float(lines[i][10:-5].strip()) for i in range(2, len(lines), 5)] #mb/s
        #Create a list to contain all the upload speeds in the file (units not included)
        upload_speeds = [float(lines[i][8:-5].strip()) for i in range(3, len(lines), 5)] #mb/s

    # print('Speed_Type: Q1, Q3, IQ')
    #Calculate the percentiles needed to find the outlier ranges for the 3 speeds
    #Ping
    ping_Q1 = np.percentile(np.array(sorted(ping_speeds)), 25)
    ping_Q3 = np.percentile(np.array(sorted(ping_speeds)), 75)
    ping_IQ = ping_Q3 - ping_Q1
    # print('Ping:', ping_Q1, ping_Q3, ping_IQ)

    #Download
    download_Q1 = np.percentile(np.array(sorted(download_speeds)), 25)
    download_Q3 = np.percentile(np.array(sorted(download_speeds)), 75)
    download_IQ = download_Q3 - download_Q1
    # print('Download:', download_Q1, download_Q3, download_IQ)

    #Upload
    upload_Q1 = np.percentile(np.array(sorted(upload_speeds)), 25)
    upload_Q3 = np.percentile(np.array(sorted(upload_speeds)), 75)
    upload_IQ = upload_Q3 - upload_Q1
    # print('Upload:', upload_Q1, upload_Q3, upload_IQ)


    #Now trim the speeds' list so that the outliers are removed and the dates/speeds pairs remain the same
    #The trimmed_data list will contain tuples in the form (DATE, PING, DOWNLOAD, UPLOAD), where each\
    #tuple contains the four values for each recording in the file
    #A tupple will only be added if all 3 speeds are not outliers; if at least one speed for a given date\
    #is an outlier, then the records for that date will be ignored
    trimmed_data = []
    for i in range(len(dates)):
        if (ping_Q1-1.5*ping_IQ) <= ping_speeds[i] <= (ping_Q3+1.5*ping_IQ):
            if (download_Q1-1.5*download_IQ) <= download_speeds[i] <= (download_Q3+1.5*download_IQ):
                if (upload_Q1-1.5*upload_IQ) <= upload_speeds[i] <= (upload_Q3+1.5*upload_IQ):
                    trimmed_data.append((dates[i], ping_speeds[i], download_speeds[i], upload_speeds[i]))

    # Bucket sort the ping, download and upload values
    # Number of tested days (after trimming)
    num_days = len(trimmed_data)
    # The following bucket sorted-lists will hold repeated values in its buckets\
    # (if that's the case) since we are looking for absolute frequencies rather\
    # than the values themselves

    # Each ping bucket will hold values in the range of multiples of 3\
    # (each bucket holds values in the range\
    # i/3 - 3, where i is the index of the bucket)
    ping_max = max([int(i[1]) for i in trimmed_data])
    ping_buckets = [[] for x in range(ping_max//3+1)]
    for val in [i[1] for i in trimmed_data]:
        ping_buckets[int(val/3)].append(val)
    # ping_buckets = [sorted(bucket) for bucket in ping_buckets]
    ping_buckets = np.array([len(bucket) for bucket in ping_buckets])
    ping_buckets_ticks = [f'[{str(i)}, {str(i+3)}[' for i in range(0, ping_max+1, 3)]

    # Each download bucket will hold values in the range of multiples of 5\
    # (each bucket holds values in the range\
    # i/3 - 3, where i is the index of the bucket)
    download_max = max([int(i[2]) for i in trimmed_data])
    download_buckets = [[] for x in range(download_max//5+1)]
    for val in [i[2] for i in trimmed_data]:
        download_buckets[int(val/5)].append(val)
    # download_buckets = [sorted(bucket) for bucket in download_buckets]
    download_buckets = np.array([len(bucket) for bucket in download_buckets])
    download_buckets_ticks = [f'[{str(i)}, {str(i+5)}[' for i in range(0, download_max+1, 5)]

    # Each upload bucket will hold values in the range of multiples of 5\
    # (each bucket holds values in the range\
    # i/3 - 3, where i is the index of the bucket)
    upload_max = max([int(i[3]) for i in trimmed_data])
    upload_buckets = [[] for x in range(upload_max//5+1)]
    for val in [i[3] for i in trimmed_data]:
        upload_buckets[int(val/5)].append(val)
    # upload_buckets = [sorted(bucket) for bucket in upload_buckets]
    upload_buckets = np.array([len(bucket) for bucket in upload_buckets])
    upload_buckets_ticks = [f'[{str(i)}, {str(i+5)}[' for i in range(0, upload_max+1, 5)]

    '''Dates/Ping Graph'''
    '''
    # Plot a graph where the x-values are the dates extracted and the y-values are the ping values
    # Use a red line for the plotting
    plt.plot([i[0] for i in trimmed_data], [i[1] for i in trimmed_data], 'r')
    # Label the axis and the graph
    plt.xlabel('Dates')
    plt.ylabel('Ping values in ms')
    plt.title('Dates/Ping Values')
    # For better viewing, rotate the x labels
    # Start by creating an axis object
    ax = plt.subplot()
    # Then set the x-axis ticks (here we set them using a range of\
    # 0 to the number of dates in the trimmed data, exclusive)
    ax.set_xticks(range(len(trimmed_data)))
    # Finally, labels the x-axis ticks with the trimmed data dates,\
    # with a rotation of 90 degrees, so that they occupy less horizontal\
    # space
    ax.set_xticklabels([i[0] for i in trimmed_data], rotation=90)
    # Plot the graph in a new window
    plt.show()
    '''


    '''Dates/Download Graph'''
    '''
    # Plot a graph where the x-values are the dates extracted and the y-values are the download speeds
    # Use a green line for the plotting
    plt.plot([i[0] for i in trimmed_data], [i[2] for i in trimmed_data], 'g')
    # Label the axis and the graph
    plt.xlabel('Dates')
    plt.ylabel('Download speeds in mb/s')
    plt.title('Dates/Download Speeds')
    # For better viewing, rotate the x labels
    # Start by creating an axis object
    ax = plt.subplot()
    # Then set the x-axis ticks (here we set them using a range of\
    # 0 to the number of dates in the trimmed data, exclusive)
    ax.set_xticks(range(len(trimmed_data)))
    # Finally, labels the x-axis ticks with the trimmed data dates,\
    # with a rotation of 90 degrees, so that they occupy less horizontal\
    # space
    ax.set_xticklabels([i[0] for i in trimmed_data], rotation=90)
    # Plot the graph in a new window
    plt.show()
    '''

    '''Dates/Upload Graph'''
    '''
    # Plot a graph where the x-values are the dates extracted and the y-values are the upload speeds
    # Use a blue line for the plotting
    plt.plot([i[0] for i in trimmed_data], [i[3] for i in trimmed_data], 'b')
    # Label the axis and the graph
    plt.xlabel('Dates')
    plt.ylabel('Upload speeds in mb/s')
    plt.title('Dates/Upload Speeds')
    # For better viewing, rotate the x labels
    # Start by creating an axis object
    ax = plt.subplot()
    # Then set the x-axis ticks (here we set them using a range of\
    # 0 to the number of dates in the trimmed data, exclusive)
    ax.set_xticks(range(len(trimmed_data)))
    # Finally, labels the x-axis ticks with the trimmed data dates,\
    # with a rotation of 90 degrees, so that they occupy less horizontal\
    # space
    ax.set_xticklabels([i[0] for i in trimmed_data], rotation=90)
    # Plot the graph in a new window
    plt.show()
    '''

    '''Plot Dates/Ping, Dates/Download and Dates/Upload in a single graph'''
    # Plot the ping in red
    plt.plot([i[0] for i in trimmed_data], [i[1] for i in trimmed_data], 'r')
    # Plot the download in gree
    plt.plot([i[0] for i in trimmed_data], [i[2] for i in trimmed_data], 'g')
    # Plot the upload in blue
    plt.plot([i[0] for i in trimmed_data], [i[3] for i in trimmed_data], 'b')
    # For better viewing, rotate the x labels
    # Start by creating an axis object
    ax = plt.subplot()
    # Then set the x-axis ticks (here we set them using a range of\
    # 0 to the number of dates in the trimmed data, exclusive)
    ax.set_xticks(range(len(trimmed_data)))
    # Finally, labels the x-axis ticks with the trimmed data dates,\
    # with a rotation of 90 degrees, so that they occupy less horizontal\
    # space
    ax.set_xticklabels([i[0] for i in trimmed_data], rotation=90)

    plt.legend(['Ping', 'Download', 'Upload'], loc='upper left')
    plt.show()

    '''Ping Distribution Pie Chart'''
    plt.pie(ping_buckets, autopct='%0.2f%%')
    plt.title('Ping Values Intervals\' Relative Frequencies')
    plt.axis('equal')
    plt.legend(ping_buckets_ticks, loc='upper left')
    plt.show()

    '''Download Distribution Pie Chart'''
    plt.pie(download_buckets, autopct='%0.2f%%')
    plt.title('Download Speeds Intervals\' Relative Frequencies')
    plt.axis('equal')
    plt.legend(download_buckets_ticks, loc='upper left')
    plt.show()

    '''Upload Distribution Pie Chart'''
    plt.pie(upload_buckets, autopct='%0.2f%%')
    plt.title('Upload Speeds Intervals\' Relative Frequencies')
    plt.axis('equal')
    plt.legend(upload_buckets_ticks, loc='upper left')
    plt.show()

if __name__ == "__main__":
    visualize_data('InternetSpeeds.txt')