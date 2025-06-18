---
chunk_id: discourse_topic_167072_post_1_01
source_url: https://discourse.onlinedegree.iitm.ac.in/t/167072/1
source_title: Sudo permission needed to create data folder in root?
content_type: discourse
tokens: 935
username: vikramjncasr
post_number: 1
topic_id: 167072
---

/t/167072/1)

@Jivraj @carlton sir please help

When I am downloading the data folder after processing datagen.py , it is trying to download in root folder and it is facing permission error . how can we overcome this ?

needs sudo permission all the time…

---

**[Discussion Image by vikramjncasr]** The image depicts a student's terminal session while working within the `/mnt/c/IIT_Madras/TDS_Project_1` directory, indicating this is part of a class project. The student, `vikramjncasr`, is trying to list the contents of the root directory (`/`) after attempting to use `sudo rm /*.data`, which they probably intended to use to delete data files in root. They then execute `ls /`, revealing the standard root directory structure with folders like `bin`, `boot`, `etc`, `home`, `mnt`, `root`, `tmp`, and `usr`. The listing shows the contents of the root directory, implying a permission issue if they were trying to create a folder there; the user needs root permissions. This is a troubleshooting scenario where a student is likely facing problems creating or deleting files in the root directory due to lacking `sudo` privileges.o create or modify files in the root directory without elevated privileges." alt="image" data-base62-sha1="yXVNx8O1oDleUm0YAE5Z6ZAElJk" width="690" height="70" srcset="**[Discussion Image by vikramjncasr]** This image shows a student, vikramjncasr, in a terminal window, listing the contents of the root directory ("/"). The student is working within the directory "/mnt/c/IIT_Madras/TDS_Project_1" and has attempted to use the command "sudo rm -rf /*", but it is not completely executed in the snapshot shown; the command is present but could have potentially been interrupted before it actually deletes the entire root directory. The output of the "ls /" command displays standard directories like "bin", "boot", "etc", "home", "root", "tmp", and "usr", confirming the student successfully listed the root directory's contents using the list command. The purpose seems to be either exploration of the root directory's structure or some attempt to modify or delete files within it, although that could create critical system issues. The student seems to be working on a project named "TDS_Project_1" located under the IIT Madras directory and the current location is shown on the prompt., **[Discussion Image by vikramjncasr]** This image represents a student's question within a TDS (presumably a course) discussion forum, specifically about needing sudo permissions. The student, `vikramjncasr`, is in the `/mnt/c/IIT_Madras/TDS_Project_1` directory and attempts to list the contents of the root directory using `ls /`. Before this attempt they enter `sudo mkdir /data`, but the OCR is only partially readable. The output of `ls /` displays the standard root directory structure (bin, boot, etc, home, media, root, tmp, usr, var, etc.). The image suggests the student is likely trying to create a 'data' directory in the root directory and encountered a permissions issue, hence the need for sudo. The post illustrates a common troubleshooting scenario in a Linux environment where elevated privileges are necessary for certain operations. 1.5x, **[Discussion Image by vikramjncasr]** This image captures a student question on a TDS discussion forum about needing sudo permissions to create a data folder in the root directory. The student, vikramjncasr, is working in the directory `/mnt/c/IIT_Madras/TDS_Project_1`. They attempted to create a `/data` directory using `sudo mkdir /data`, but the outcome is not shown directly in this image. The output of the `ls /` command is shown, listing standard root directories like `bin`, `boot`, `etc`, `home`, `media`, and `tmp`, before the assumed attempt to create the `/data` directory. The image serves to show the context of the student's working directory and provides the initial troubleshooting step of listing the root directory's contents. The question seeks guidance on why sudo permissions are needed. 2x" data-dominant-color="1E2227">image2100×216 100 KB
