---
chunk_id: discourse_topic_169029_post_123_02
source_url: https://discourse.onlinedegree.iitm.ac.in/t/169029/123
source_title: Project 2 - TDS Solver - Discussion Thread
content_type: discourse
tokens: 400
username: carlton
post_number: 123
topic_id: 169029
---

 Send the JSON data
response = requests.post (url, json=response_to_send_to_tds_evaluator)

# Check the response
print (response.status_code)
print (response.json ())
print (response.text)

# Do other checks as necessary... 
`
See what happens when I print the result

---

`print (json.loads (response.text)['json']['answer'])
`
**[Discussion Image by carlton]** This image depicts a terminal output from a student's execution of a Python script named `test.py` within the `tds` directory. The script prints a multiline string containing spaces, newlines, and a tab character to the console. The prompt `venvcarlant@Carlton-MacBook-Pro tds %` indicates the user's location in the file system, and the command `/User/tds/test.py` attempts to directly execute the python script (likely with the python shebang line). The output demonstrates the successful printing of the multiline string as intended within the test script. No errors are shown, indicating successful execution.t. The student `venvcarland` from Carlton-MacBook-Pro executes the script, and the script outputs a multiline string containing spaces, newlines, and tabs. The multiline string printed to the terminal confirms the script can handle and render these special characters. The prompt `venvcarland@Carlton-MacBook-Pro tds %` before and after the script execution indicates the user's current directory in the terminal is the `tds` directory. This is likely an example output provided to the students." alt="Screenshot 2025-03-27 at 1.09.56 pm" data-base62-sha1="oH1VnNagrJMWv1kL9vEZ36eOUoU" width="323" height="120">Screenshot 2025-03-27 at 1.09.56 pm323×120 3.61 KB
