---
chunk_id: discourse_topic_165922_post_3_00
source_url: https://discourse.onlinedegree.iitm.ac.in/t/165922/3
source_title: Best Practices for Virtual Environments and Dependency Management in Python
content_type: discourse
tokens: 302
username: 23f2003845
post_number: 3
topic_id: 165922
---

## Post #3 by 23f2003845

**Direct Link**: [Post #3](https://discourse.onlinedegree.iitm.ac.in/t/165922/3)

For some projects where there are many dependencies, like an ML project or flask app, it’s better you mantain a virtual environment since the dependencies are interconnected with their versions.

Whereas for some simple projects, with less dependencies, global installation is fine.

[Quote]: 
For project that is to be deployed, make sure you use the virtual environment, only then you can ensure what worked for you also works on the deployement

24f2006531:
[Quote]: 
Additionally, when managing dependencies, would it be better to install packages individually using pip or list them in a requirements.txt file?

Coming to your second question,

The first time you install a fresh dependency, use direct and latest version. But if you are cloning or thinking of sharing the repo or using someone’s project it’s better to use requirements.txt.

24f2006531:
[Quote]: 
My understanding is that if a version is not specified in the requirements.txt file, it installs the latest available version, whereas specifying a version ensures a specific installation

The creation of requirements.txt ensures that the current installation version is listed.

[Quote]: 
Never try to list requirements.txt. There is a command to do that, `pip3 freeze &gt; requirements.txt `. This does the hard work of listing the dependencies for you
