import pandas as pd

# Read the CSV file into a pandas DataFrame
csv_file = "C:/Users/gavin/Downloads/arsenal1723/players.csv"
df = pd.read_csv(csv_file)

# Define the output Excel file name
xlsx_file = './conCSV/players.xlsx'

# Write the DataFrame to an Excel file
df.to_excel(xlsx_file, index=False)

print(f"CSV file '{csv_file}' has been converted to Excel file '{xlsx_file}'.")
