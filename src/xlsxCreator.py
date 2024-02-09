import random
from openpyxl import Workbook

# Define Headers and Data to be Inputted
HEADER = ['Employee Number', 'Name', 'Job Title', 'Department', 'Location', 'Salary (€)', 'Degree']
NAME = ['Mark Corrigan', 'Alan Johnson', 'Sophie Chapman']
LOCATION = ['London', 'Aberdeen', 'Frankfurt']
TITLE = ['CEO', 'CFO', 'CTO']

# Generate Rows of Pre-Defined Data
rows = []
for i in range(1, 4):
    # Select a random name, location, and job title
    name = random.choice(NAME)
    location = random.choice(LOCATION)
    title = random.choice(TITLE)
    # Append the data as a row
    rows.append([name, location, title])

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
