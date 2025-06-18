---
chunk_id: discourse_topic_171141_post_157_01
source_url: https://discourse.onlinedegree.iitm.ac.in/t/171141/157
source_title: Tds-official-Project1-discrepencies
content_type: discourse
tokens: 1071
username: 23f2005702
post_number: 157
topic_id: 171141
---

5702

**Direct Link**: [Post #157](https://discourse.onlinedegree.iitm.ac.in/t/171141/157)

@carlton

Pls look into this evaluation.py contains two result

Can u confirm that u guys will use 10/20 one ?

---

**[Discussion Image by 23f2005702]** This image shows an instructor's instructions for a student on a project, specifically addressing discrepancies. The instructions include how to count rows with SQL using curl, providing a specific command: `bash curl "http://localhost:8001/ticket-sales.csv?sql=SELECT COUNT(*) FROM tickets WHERE type=%22Bronze%22" -o /data/b10.csv`. The instructions also detail how to stop the Datasette server, either by bringing the server process to the foreground with `fg` or killing the process using `kill $(jobs -p)`. The summary of commands includes starting the server with `bash uvx datasette /data/ticket-sales.db --port 8001 &` and the curl command from above. The student is receiving an error: "HTTP/1.1 404 Not Found" when trying to read `/data/b10.csv`, indicating that the file is not found, leading to a "B10 failed: Cannot read /data/b10.csv" error, resulting in a score of 10/20. The instructor's notes emphasize ensuring `uvx` and `datasette` are installed and configured correctly, and that the `/data` directory is writable.g the datasette server with `datasette /data/ticket-sales.db --port 8001`, as well as a reminder to ensure `uvx` and `datasette` are properly installed and configured, and that the `/data` directory is writable. At the end of the post, the error messages `HTTP/1.1 404 Not Found`, and `B10 failed: Cannot read /data/b10.csv` and student score indicate a failure to retrieve the b10 data." alt="Screenshot_2025-04-01-08-51-03-781_com.google.android.apps.docs" data-base62-sha1="rt4RWLXkL84tt2DQxU3WClYumFi" width="230" height="500" srcset="**[Discussion Image by 23f2005702]** This image shows instructor guidance within the "Tds-official-Project1-discrepencies" discussion, specifically addressing Step 2 (counting rows with SQL) and Step 3 (stopping the Datasette server). The instructions detail using `curl` to make a request to a URL, including a command to fetch a CSV output of an SQL query and save it to `/data/b10.csv`. Additionally, it provides instructions to stop the Datasette server, including methods to kill background jobs or using the PID. The bottom of the image shows error messages: "HTTP/1.1 404 Not Found" for a GET request to read `/data/b10.csv`, and "B10 failed: Cannot read /data/b10.csv," indicating a problem accessing the created file, likely due to permissions or incorrect path, also the project scored 10/20 at the time of capture., **[Discussion Image by 23f2005702]** This image shows the output from a student attempting to complete project step 2, counting rows with SQL using `curl`. It details the instructions for starting the server, making a curl request to a specified URL (`http://localhost:8001/ticket-sales.csv`), and saving the output to `/data/b10.csv`. An error message "HTTP/1.1 404 Not Found" and "B10 failed: Cannot read /data/b10.csv" indicates that the `curl` request failed, likely because the file `/data/b10.csv` was not found at the specified path, or there was a directory permissions issue. The output also contains commands for stopping the Datasette server, including using `kill $(jobs -p)` or `kill `. Finally, a score of 10/20 is shown, indicating the student's progress on the project. 1.5x, **[Discussion Image by 23f2005702]** This image captures an instructor's guide and a student's terminal output in the context of a project task about counting rows with SQL using `curl`. The instructions detail how to start the server, use `curl` to fetch CSV data from a Datasette server, and save it to `/data/b10.csv`. It also includes commands to stop the Datasette server. The student's terminal output shows an HTTP 404 error "Not Found" when trying to read `/data/b10.csv`, suggesting the file wasn't created or the path is incorrect and the B10 test failed, resulting in a score of 10/20. The successful POST request at the end indicates that the embedding service is working correctly, but doesn't resolve the `curl` related issue. 2x" data-dominant-color="171717">Screenshot_2025-04-01-08-51-03-781_com.google.android.apps.docs1080×2340 253 KB
