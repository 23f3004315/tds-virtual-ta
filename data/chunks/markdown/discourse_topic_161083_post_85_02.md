---
chunk_id: discourse_topic_161083_post_85_02
source_url: https://discourse.onlinedegree.iitm.ac.in/t/161083/85
source_title: GA1 - Development Tools - Discussion Thread [TDS Jan 2025]
content_type: discourse
tokens: 206
username: 23f3002537
post_number: 85
topic_id: 161083
---

18b7816808b7d *", but the system indicates "Incorrect. Try again." suggesting the response did not match the expected output, indicating a need for debugging. 2x" data-dominant-color="282C30">image1641×356 26.7 KB

---

Sir I’m facing issue in this question even though i have done every thing as it mentioned. Can I get hint of the mistake for my code snippet.

My code: -

`mkdir all_files
find parent/ -type f -exec mv {} all_files/ \;
for file in all_files/*; do
 new_name=$(echo "$file" | sed 's/[0-9]/\n&amp;\n/g' | awk '
 { 
 if ($0 ~ /^[0-9]$/) print ($0 == "9") ? 0 : $0+1; 
 else print $0 
 }' | tr -d "\n")
 mv "$file" "$new_name"
done
`
