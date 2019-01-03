# Test my Internet speeds at the runtime of the script; then save the date and those speeds to a .txt file
# This script uses the speedtest package for the speed tests (against speedtest.net)

# https://github.com/sivel/speedtest-cli
import speedtest, datetime, time, os
import pandas as pd

# Start time of the script execution (after imports)
start_time = time.time()

# Obtain the current date and time (YYYY-MM-DD HH:MM:SS)
date_now = str(datetime.datetime.now())[:19]
# Create a 'SpeedTest' object to be able to connect to a speedtest server
speed_test = speedtest.Speedtest()

try:
	# Find the best server
	speed_test.get_best_server()

	# Get the ping results (convert it to miliseconds)
	ping = round(speed_test.results.ping / 10, 2)
	# Get the download speed results (convert it from bits/s to \
	# megabits/s, and round it to 3 decimal points)
	download = round(speed_test.download() / 1000000, 2)
	# Get the upload speed results (convert it from bits/s to \
	# megabits/s, and round it to 3 decimal points)
	upload = round(speed_test.upload() / 1000000, 2)

	# Create the string to contain the date and speeds that will be written to the .txt file
	write_string = f'Date: {date_now}\n\tPing: {ping}ms\n\tDownload: {download}mb/s\n\tUpload: {upload}mb/s\n\n'
	print(write_string)

	# Write the latest internet speeds to the .txt file
	with open('InternetSpeeds.txt', 'a') as f:
		f.write(write_string)
	print('The latest Internet speed values have been written to the file.')

	# Append the latest test to the .csv file
	# Load the .csv
	csv_file = pd.read_csv('internet_speeds.csv', index_col=0)
	# Create a DataFrame to hold the new test results (a single row)
	write_df = pd.DataFrame(
		[[ping, download, upload]],
		columns=['Ping (ms)', 'Download (mb/s)', 'Upload (mb/s)'],
		index=[str(date_now[:10])]
	)
	# Append the DataFrame to the loaded .csv and save the result over the\
	# already existing .csv file
	csv_file.append(write_df, sort=False).to_csv('internet_speeds.csv', index_label='Date')


# In case something goes wrong, catch the error to not raise exceptions
except:
	print('Couldn\'t find a test server')

# At the end, print a message with the execution time
print(f'Elapsed time: {int(time.time() - start_time)} seconds.')