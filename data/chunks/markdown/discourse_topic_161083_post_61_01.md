---
chunk_id: discourse_topic_161083_post_61_01
source_url: https://discourse.onlinedegree.iitm.ac.in/t/161083/61
source_title: GA1 - Development Tools - Discussion Thread [TDS Jan 2025]
content_type: discourse
tokens: 480
username: 24f1002359
post_number: 61
topic_id: 161083
---

**[Discussion Image by 24f1002359]** This image shows a student's attempt to calculate the SHA256 hash of a file named "formatted.md" within a PowerShell terminal in VS Code, which is likely related to a Git assignment asking to ensure the file hasn't changed after formatting. The student initially uses `Get-FileHash` to compute the hash, then formats the file using `npx -y prettier@3.4.2 "F:\BS DATA SCIENCE\Diploma Level\TERM 2\TDS\README.md" > formatted.md`, redirecting the output to the same file. Afterwards, they rerun the `Get-FileHash` command, finding the hash value hasn't changed, which suggests the `prettier` operation didn't modify the file content despite reformatting it. To verify the hash result, the student uses `certutil -hashfile formatted.md SHA256` to calculate the hash via a different tool, confirming the previously obtained hash value. The student seems to be ensuring the formatting command doesn't alter the file's core content as part of a development task.s to use `Get-FileHash -Path formatted.md -Algorithm SHA256` and successfully retrieves the SHA256 hash. They then use `npx -y prettier@3.4.2 "F:\BS DATA SCIENCE\Diploma Level\TERM 2\TDS\README.md" > formatted.md` which overwrites the 'formatted.md' file with the formatted content of 'README.md'. After that, they attempt to calculate the SHA256 hash again using `Get-FileHash` with the same parameters, confirming the file has changed since the previous hash matches the last one, and finally uses `certutil -hashfile formatted.md SHA256` to achieve the same result, indicating they are exploring alternative tools for the task. The output confirms that CertUtil completed successfully and provides the same SHA256 hash value." alt="Screenshot 2025-01-18 154321" data-base62-sha1="aDG4vwY7tnu3GTLlAUt58Nl445u" width="690" height="330" data-dominant-color="071C2D">Screenshot 2025-01-18 1543211317×630 30.9 KB
