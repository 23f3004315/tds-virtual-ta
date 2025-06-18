---
chunk_id: course_bash_001
source_url: https://tds.s-anand.net/#/bash
source_title: bash
content_type: course
tokens: 453
---

grep "pattern" file # Search for pattern
sed 's/old/new/' f # Replace text
awk '{print $1}' f # Process text by columns
cat file | wc -l # Count lines

# Process Management
ps aux # List processes
kill -9 PID # Force kill process
top # Monitor processes
htop # Interactive process viewer

---

# Network
curl url # HTTP requests
wget url # Download files
nc -zv host port # Test connectivity
ssh user@host # Remote login

# Count unique values in CSV column
cut -d',' -f1 data.csv | sort | uniq -c

# Quick data analysis
awk -F',' '{sum+=$2} END {print sum/NR}' data.csv # Average
sort -t',' -k2 -n data.csv | head # Top 10

# Monitor log in real-time
tail -f log.txt | grep --color 'ERROR'
```

Bash Scripting Essentials:

```bash
#!/bin/bash

# Variables
NAME="value"
echo $NAME

# Loops
for i in {1..5}; do
 echo $i
done

# Conditionals
if [ -f "file.txt" ]; then
 echo "File exists"
fi

# Functions
process_data() {
 local input=$1
 echo "Processing $input"
}
```

Productivity Tips:

1. **Command History**

```bash
 history # Show command history
 Ctrl+R # Search history
 !! # Repeat last command
 !$ # Last argument
 ```

2. **Directory Navigation**

```bash
 pushd dir # Push directory to stack
 popd # Pop directory from stack
 cd - # Go to previous directory
 ```

3. **Job Control**

```bash
 command & # Run in background
 Ctrl+Z # Suspend process
 bg # Resume in background
 fg # Resume in foreground
 ```

4. **Useful Aliases** - typically added to `~/.bashrc`
 ```bash
 alias ll='ls -la'
 alias gs='git status'
 alias jupyter='jupyter notebook'
 alias activate='source venv/bin/activate'
 ```
