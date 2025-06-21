import pandas as pd

def merge_worksheets(input_file, output_file):
    # Read all sheets from the input Excel file into a dictionary of DataFrames
    all_sheets = pd.read_excel(input_file, sheet_name=None)

    # Concatenate all DataFrames into a single DataFrame
    merged_data = pd.concat(all_sheets.values(), ignore_index=True)

    # Write the merged DataFrame to a new Excel file
    merged_data.to_excel(output_file, index=False)

# Provide the path to your input and output Excel files
input_excel_path = 'C:/Users/cheta/Desktop/Mp_election_seat_wise_part_2.xlsx'
output_excel_path = 'C:/Users/cheta/Desktop/MP_Election_seat_wise_data part_2_merge.xlsx'

# Call the function to merge worksheets
merge_worksheets(input_excel_path, output_excel_path)

print(output_excel_path)