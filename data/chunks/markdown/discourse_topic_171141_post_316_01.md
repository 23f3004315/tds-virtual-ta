---
chunk_id: discourse_topic_171141_post_316_01
source_url: https://discourse.onlinedegree.iitm.ac.in/t/171141/316
source_title: Tds-official-Project1-discrepencies
content_type: discourse
tokens: 359
username: carlton
post_number: 316
topic_id: 171141
---

github/'"
)
parser.add_argument (
 "--extract",
 type=str,
 default="../github/",
 help="Path to extract the zip file. Default='../github/'"
)

args = parser.parse_args ()
owner = args.owner
repo = args.repo
save_path = args.save
extract_path = args.extract

---

deadline = dt.datetime (2025, 2, 18, tzinfo=zoneinfo.ZoneInfo("Asia/Kolkata"))
deadline_str = deadline.isoformat ()

github_headers = {
 "Accept": "application/vnd.github.v3+json",
 "X-GitHub-Api-Version": "2022-11-28",
 "User-Agent": "fetch_git_before",
}

url = f"https://api.github.com/repos/{owner}/{repo}/commits?until={deadline_str}&amp;per_page=1&amp;page=1"

try:
 response = requests.get (url, headers=github_headers, timeout=60)
 response.raise_for_status () # Raise an error for bad responses

# Get the sha
 commits = response.json ()
 if commits:
 latest_sha = commits[0]["sha"]
 print (f"Latest commit before {deadline_str}: {latest_sha}")

# Get the zip of the commit
 zip_url = f"https://api.github.com/repos/{owner}/{repo}/zipball/{latest_sha}"
 zip_response = requests.get (zip_url, headers=github_headers, timeout=60)
 zip_response.raise_for_status ()
 zip_filename = f"{latest_sha}.zip"

# Create the directory if it doesn't exist
 os.makedirs (save_path, exist_ok=True)

with open (save_path + zip_filename, "wb") as f:
 f.write (zip_response.content)
 print (f"Downloaded zip file: {zip_filename}")
