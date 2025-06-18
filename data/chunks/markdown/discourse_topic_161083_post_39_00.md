---
chunk_id: discourse_topic_161083_post_39_00
source_url: https://discourse.onlinedegree.iitm.ac.in/t/161083/39
source_title: GA1 - Development Tools - Discussion Thread [TDS Jan 2025]
content_type: discourse
tokens: 256
username: roy2003
post_number: 39
topic_id: 161083
---

## Post #39 by roy2003

**Direct Link**: [Post #39](https://discourse.onlinedegree.iitm.ac.in/t/161083/39)

`!pip install chardet==5.1.0 # Install the chardet library
`
`import chardet
def read_files():
 """Gets two CSV files and one TXT file from the user and reads them.

Returns:
 A tuple containing the contents of the three files.
 """
 # Get the file paths from the user.
 csv_file_1_path = input("Enter the path to the first CSV file: ")
 csv_file_2_path = input("Enter the path to the second CSV file: ")
 txt_file_path = input("Enter the path to the TXT file: ")

# ... (Get file paths from user - same as before)

# Read the CSV files.
 try:
 with open(csv_file_1_path, 'rb') as f: # Open in binary mode
 rawdata = f.read()
 encoding = chardet.detect(rawdata)['encoding'] # Detect encoding
 with open(csv_file_1_path, 'r', encoding=encoding) as csv_file_1: # Use detected encoding
 csv_data_1 = csv_file_1.read()
