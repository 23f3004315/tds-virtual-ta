---
chunk_id: discourse_topic_161083_post_39_01
source_url: https://discourse.onlinedegree.iitm.ac.in/t/161083/39
source_title: GA1 - Development Tools - Discussion Thread [TDS Jan 2025]
content_type: discourse
tokens: 331
username: roy2003
post_number: 39
topic_id: 161083
---

 mode
 rawdata = f.read()
 encoding = chardet.detect(rawdata)['encoding'] # Detect encoding
 with open(csv_file_1_path, 'r', encoding=encoding) as csv_file_1: # Use detected encoding
 csv_data_1 = csv_file_1.read()

---

# Repeat for csv_file_2_path using the same pattern
 with open(csv_file_2_path, 'rb') as f:
 rawdata = f.read()
 encoding = chardet.detect(rawdata)['encoding']
 with open(csv_file_2_path, 'r', encoding=encoding) as csv_file_2:
 csv_data_2 = csv_file_2.read()

except FileNotFoundError:
 print("Error: One or both of the CSV files could not be found.")
 return None
 except UnicodeDecodeError:
 print("Error: Could not decode one or both of the CSV files.")
 return None

# Read the TXT file.
 try:
 with open(txt_file_path, 'rb') as f: # Open in binary mode to detect encoding
 rawdata = f.read()
 encoding = chardet.detect(rawdata)['encoding'] # Detect encoding
 with open(txt_file_path, 'r', encoding=encoding) as txt_file: # Open in text mode with detected encoding
 txt_data = txt_file.read() # Read the content of the file
 except FileNotFoundError:
 print("Error: The TXT file could not be found.")
 return None
 except UnicodeDecodeError:
 print("Error: Could not decode the TXT file.")
 return None

# Return the contents of the files.
 return csv_data_1, csv_data_2, txt_data
