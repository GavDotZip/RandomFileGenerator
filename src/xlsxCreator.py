import random
import requests
from openpyxl import Workbook


# Function to fetch random names from an API
def fetch_random_name():
    response = requests.get("https://api.namefake.com/")
    data = response.json()
    return data['name']


# Define Headers and Data to be Inputted
HEADER = ['Employee Number', 'Name', 'Job Title', 'Department', 'Location', 'Salary (€)', 'Degree']
# NAME = ['Mark Corrigan', 'Alan Johnson', 'Sophie Chapman']
# LOCATION = ['London', 'Aberdeen', 'Frankfurt']
# TITLE = ['CEO', 'CFO', 'CTO']

# Generate Rows of Pre-Defined Data
rows = []
for i in range(1, 151):
    # Fetch a random name from the API
    name = fetch_random_name()
    # Append the data as a row
    rows.append([i, name])

# Create, Fill, and Save Excel
wb = Workbook()
ws = wb.active
# Append the header row
ws.append(HEADER)

# Append each row of data
for row in rows:
    ws.append(row)

# Save the Excel file
wb.save('ConsultioConsultious.xlsx')
