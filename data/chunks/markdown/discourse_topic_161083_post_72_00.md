---
chunk_id: discourse_topic_161083_post_72_00
source_url: https://discourse.onlinedegree.iitm.ac.in/t/161083/72
source_title: GA1 - Development Tools - Discussion Thread [TDS Jan 2025]
content_type: discourse
tokens: 174
username: carlton
post_number: 72
topic_id: 161083
---

## Post #72 by carlton

**Direct Link**: [Post #72](https://discourse.onlinedegree.iitm.ac.in/t/161083/72)

@Rohitkumar7463 @23f2003845

If you are on Windows Powershell

Then instead of `sha256sum` you can simply use `Get-FileHash`

Send the output of the `npx -y prettier@3.4.2 README.md` to a text file eg. `output.txt` and then use `Get-FileHash` on powershell with the `output.txt` and it will use sha256 by default and give you the exact same output.

You might be able to pipe the data directly to `Get-FileHash` but I have not tried direct piping. The above method works guaranteed.

Kind regards
