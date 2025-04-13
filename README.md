# LogSift
Webster Hackathon 2025 Project - Rob McCormick

Thank you for viewing my project. My intention when creating this was to make something that was related to the Cybersecurity or IT field. It's commmon for Security Analyst's to automate their work when looking through thousands upon thousands of logs, so I thought a basic parsing app with a GUI would help make the job a little bit easier! I am not an experienced programmer, so a lot of the tools I used were quite new to me and I learned a lot in this process such as working with a python GUI (tkinter) or using regular expressions to check log syntax. 

# Description
LogSift is a simple Python-based GUI tool for reading, filtering, and exporting Apache error logs. Built with tkinter, it helps users visually analyze and extract key insights from their logs with ease.

# What Can This App Do?
- Open '.log' and '.txt' files
- Display logs in a scrollable GUI
- Filter logs by keyword
- Show number of matches for searched terms
- Export filtered results to a '.csv' for analysis

# Files  
- main.py -> contains GUI application logic
- parser.py -> functions for reading, filters, exporting logs, etc..
- example.log -> sample log file containing Apache error logs
 
# Acknowledgments
- Logs used in example file are from github Apache/Apache_2k.log https://github.com/logpai/loghub/blob/master/Apache/Apache_2k.log
- ChatGPT/YouTube used to learn new tools and coding inspiration/guidance + generating the regular expression
  
