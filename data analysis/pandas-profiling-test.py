import pandas as pd
import pandas_profiling as pd_p

# This if clause is used so that the following block is only executed when\
# this script is run (that is, if this script is imported the code block\
# will not be executed)
if __name__ == '__main__':
	# Load the target CSV file
	df = pd.read_csv("../internet_speeds.csv")

	# This is for Jupyter Notebooks only
	# pd_p.ProfileReport(df)

	# Create a `Profile` for the loaded CSV data
	test_profile = pd_p.ProfileReport(df)

	# Create an HTML file with web version of the report
	test_profile.to_file(outputfile="Internet Speeds Profile.html")