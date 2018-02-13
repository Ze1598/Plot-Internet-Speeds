#Test my Internet speeds at the runtime of the script; then save the date and those speeds to a .txt file

#https://github.com/fopina/pyspeedtest
import pyspeedtest, datetime

#Obtain the current date and time from the 'datetime' module (YYYY-MM-DD HH:MM:SS)
date_now = str(datetime.datetime.now())[:19]
#Create a 'SpeedTest' object to be able to connect to speedtest server
speeds = pyspeedtest.SpeedTest()

#try/except clause in case an exception is raised for when there are no test servers available
try:
    #Obtain the ping, download and upload speeds
    #Convert ping to miliseconds (ms); download and upload to megabytes per second (mb/s)
    ping, dwld, upld = round(speeds.ping(),2), round(speeds.download()/1000000,2), round(speeds.upload()/1000000,2)
    
    #Create the string to contain the date and speeds that will be written to the .txt file
    write_string = f'Date: {date_now}\n\tPing: {ping}ms\n\tDownload: {dwld}mb/s\n\tUpload: {upld}mb/s'
    print(write_string)
    
    #Finally, append (write) 'write_string' to the 'InternetSpeeds.txt' file
    with open('InternetSpeeds.txt', 'a') as f:
        f.write(write_string + '\n\n')
    print('Your Internet speed values have been written to the file.')

except:
    print('Couldn\'t find a test server.')