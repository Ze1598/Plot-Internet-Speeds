# Imports
# -------------------------------------------------------------

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import scipy.stats as stats
# import os, pathlib

# -------------------------------------------------------------



# Get the data
# -------------------------------------------------------------

# Get the .csv with the data (which is in the parent directory of this script)
dataset = pd.read_csv('../internet_speeds.csv')
# Get the .csv the hard way
# dataset = pd.read_csv(os.path.join(pathlib.Path(os.getcwd()).parent, 'internet_speeds.csv'))

# -------------------------------------------------------------


# Calculate metrics for each column
# -------------------------------------------------------------

# Analyze each column of the dataset statistically\
# (except the dates)
# Ping
ping_mean = dataset['Ping (ms)'].mean()
ping_std = dataset['Ping (ms)'].std()
# Download
download_mean = dataset['Download (mb/s)'].mean()
download_std = dataset['Download (mb/s)'].std()
# Upload
upload_mean = dataset['Upload (mb/s)'].mean()
upload_std = dataset['Upload (mb/s)'].std()

# -------------------------------------------------------------


# Plot normal distributions for each column
# -------------------------------------------------------------

# Get the number of rows in the DataFrame
data_size = len(dataset.index)

# Plot normal distributions for each column, all three graphs in one window
plt.figure(1)
# Set the range for the y axis
y = np.linspace(ping_mean - 3*ping_std, ping_mean + 3*ping_std, data_size)
# In a grid with 3 rows and 1 column this is the first graph
plt.subplot(311)
plt.plot(sorted(dataset['Ping (ms)']), stats.norm.pdf(y, ping_mean, ping_std), color='r')
plt.title('Ping Normal Distribution')

y = np.linspace(download_mean - 3*download_std, download_mean + 3*download_std, data_size)
# In a grid with 3 rows and 1 column this is the second graph
plt.subplot(312)
plt.plot(sorted(dataset['Download (mb/s)']), stats.norm.pdf(y, download_mean, download_std), color='g')
plt.title('Download Normal Distribution')

y = np.linspace(upload_mean - 3*upload_std, upload_mean + 3*upload_std, data_size)
# In a grid with 3 rows and 1 column this is the third graph
plt.subplot(313)
plt.plot(sorted(dataset['Upload (mb/s)']), stats.norm.pdf(y, upload_mean, upload_std), color='b')
plt.title('Upload Normal Distribution')

# Before showing the graphs, adjust the spacing between the subplots
plt.tight_layout()
# Save a .png version of the plotted graph
plt.savefig('speeds_normal_dist.png', format='png')
plt.show()

# -------------------------------------------------------------



# Plot line plots for each column
# -------------------------------------------------------------

# Plot line plots for each column, all three grahps in one window
plt.figure(2)

# Ping
plt.subplot(311)
plt.title('Ping Speeds')
plt.plot(dataset['Date'], dataset['Ping (ms)'], color='r')
# An object for the axis of the current (sub)plot
frame = plt.gca()
# Set the x-axis ticks to an empty list so that the graph doesn't\
# show ticks for the x-axis
frame.axes.get_xaxis().set_ticks([])

# Download
plt.subplot(312)
plt.title('Download Speeds')
plt.plot(dataset['Date'], dataset['Download (mb/s)'], color='g')
# An object for the axis of the current (sub)plot
frame = plt.gca()
# Set the x-axis ticks to an empty list so that the graph doesn't\
# show ticks for the x-axis
frame.axes.get_xaxis().set_ticks([])

# Upload
plt.subplot(313)
plt.title('Upload Speeds')
plt.plot(dataset['Date'], dataset['Upload (mb/s)'], color='b')
# Before showing the graphs, adjust the spacing between the subplots
plt.tight_layout()
# An object for the axis of the current (sub)plot
frame = plt.gca()
# Set the x-axis ticks to an empty list so that the graph doesn't\
# show ticks for the x-axis
frame.axes.get_xaxis().set_ticks([])

# Save a .png version of the plotted graph
plt.savefig('speeds_line_plot.png', format='png')
plt.show()

# -------------------------------------------------------------