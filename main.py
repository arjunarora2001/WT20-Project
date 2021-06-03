import pandas

# Setting up tables
pandas.set_option('display.max_rows', None)
pandas.set_option('display.max_columns', None)
pandas.set_option('display.expand_frame_repr', False)
pandas.set_option('display.max_colwidth', None)

# Reading CSV files into program
rohit_df = pandas.read_csv(r'https://raw.githubusercontent.com/arjunarora2001/Cricket-Analytics-Project/main/Rohit_Sharma_data.csv')
sehwag_df = pandas.read_csv(r'https://raw.githubusercontent.com/arjunarora2001/Cricket-Analytics-Project/main/Sehwag_data.csv')
