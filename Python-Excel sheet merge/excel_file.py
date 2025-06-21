import pandas as pd

# Specify the Excel file name
excel_file = 'Mp_election_seat_wise_part_2.xlsx'

# Read all sheets into a dictionary of dataframes
xls = pd.ExcelFile(excel_file)
sheet_names = xls.sheet_names

# Create an empty dataframe to store the merged data
merged_data = pd.DataFrame()

# Loop through each sheet and append it to the merged_data dataframe
for sheet_name in sheet_names:
    df = pd.read_excel(excel_file, sheet_name)
    merged_data = merged_data.append(df, ignore_index=True)