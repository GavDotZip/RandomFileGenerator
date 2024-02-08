import random
from openpyxl import Workbook

# Define Headers and Data to be Inputted
HEADER = ['Name', 'Location', 'Job Title']
NAME = ['Mark Corrigan', 'Alan Johnson', 'Sophie Chapman']
LOCATION = ['London', 'Aberdeen', 'Frankfurt']
TITLE = ['CEO', 'CFO', 'CTO']

# Generate Rows of Pre-Defined Data
rows = []
for i in range(1, 3):
    print(i)
    name = random.choice(NAME)
    location = random.choice(LOCATION)
    title = random.choice(TITLE)
    rows.append([i, name, location, title])

# Create, Fill and Save Excel
wb = Workbook()