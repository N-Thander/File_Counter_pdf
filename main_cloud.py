import os
import pandas as pd

# Directory where the files are stored
directory = 'Cloud_Computing'

# Lists to hold the extracted data
ids = []
names = []

# Loop through all the files in the directory
for filename in os.listdir(directory):
    if filename.endswith(".pdf"):
        # Split the filename based on ' - ' (with spaces around the hyphen)
        parts = filename.split(' - ')
        
        # Ensure that the filename is in the expected format
        if len(parts) == 2:
            # Extract ID and Name
            student_id = parts[0]
            name = parts[1].replace('.pdf', '').strip()
            
            # Append the extracted data to the lists
            ids.append(student_id)
            names.append(name)

# Create a DataFrame from the lists
df = pd.DataFrame({'Student ID': ids, 'Name': names})

# Save the DataFrame to an Excel file
output_file = 'cloud_computing.xlsx'
df.to_excel(output_file, index=False)

print(f'Data saved to {output_file}')
