---
chunk_id: discourse_topic_161083_post_39_02
source_url: https://discourse.onlinedegree.iitm.ac.in/t/161083/39
source_title: GA1 - Development Tools - Discussion Thread [TDS Jan 2025]
content_type: discourse
tokens: 357
username: roy2003
post_number: 39
topic_id: 161083
---

 file
 except FileNotFoundError:
 print("Error: The TXT file could not be found.")
 return None
 except UnicodeDecodeError:
 print("Error: Could not decode the TXT file.")
 return None

# Return the contents of the files.
 return csv_data_1, csv_data_2, txt_data

---

# Call the function to read the files.
file_contents = read_files()
if file_contents:
 csv_data_1, csv_data_2, txt_data = file_contents
 #print("Content of the first CSV file:\n", csv_data_1)
 #print("\nContent of the second CSV file:\n", csv_data_2)
 #print("\nContent of the TXT file:\n", txt_data)

# Combine the content of all files into a single string
 all_content = csv_data_1 + csv_data_2 + txt_data

# Split the content into lines
 lines = all_content.split('\n')

# Initialize the total sum
 total_sum = 0

# Iterate through each line
 for line in lines:
 # Split the line into symbol and value, handling potential extra spaces
 try:
 parts = line.strip().split(',')
 symbol = parts[0].strip() # Remove leading/trailing spaces from symbol
 value = parts[1].strip() # Remove leading/trailing spaces from value

# Check if the symbol matches the criteria (using a more robust check)
 if symbol in ['€', 'ˆ', '’' # Euro symbol variations
 # Add any other known variations of the target symbols
 ]:
 # Convert the value to a number and add it to the total sum
 total_sum += float(value)

except (IndexError, ValueError):
 # Ignore lines with incorrect formatting or non-numeric values
 pass
