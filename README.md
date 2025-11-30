# VLearn_python
Assignments related to VLearn Python

VLearn Python Assignment
========================

This repository contains solutions to the VLearn Python DevOps assignment.
All four questions are implemented in separate folders.

Folder Structure:

q1 → Password strength checker

q2 → CPU usage monitoring

q3 → Configuration file parser + JSON storage + GET API

q4 → File backup utility

=================================================

Question 1 – Password Checker
File: q1/q1_password_checker.py
Checks password for:

Minimum 8 characters

Uppercase and lowercase letters

At least one digit

At least one special character

Run:

python q1/q1_password_checker.py

=================================================

Question 2 – CPU Monitor
Files: q2/q2_cpu_monitor.py, q2/q2_requirements.txt
Monitors CPU usage continuously and alerts if usage exceeds 80%.

Install:

pip install -r q2/q2_requirements.txt


Run:

python q2/q2_cpu_monitor.py

=================================================

Question 3 – Config Parser & API
Files: q3/config.ini, q3/q3_config_parser_api.py, q3/q3_requirements.txt
Reads config file, stores values as JSON in a database, and provides a GET API.

Install:

pip install -r q3/q3_requirements.txt


Run:

python q3/q3_config_parser_api.py


API endpoint:

http://127.0.0.1:5000/config

=================================================

Question 4 – Backup Script
File: q4/q4_backup.py
Copies files from source to destination.
Adds timestamp if file already exists.

Run:

python q4/q4_backup.py <source_dir> <destination_dir>

=====================================================
++++++++++++++++++++++++++++++++++++++++++++++++++++