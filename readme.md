# Email Automation Script

## Overview
This is a Python script for automating the process of sending personalized emails to multiple recipients using Gmail SMTP. The script reads recipient data from a CSV file, customizes the email body with variables, and sends emails with attachments.

## Features
- Sends personalized emails to multiple recipients
- Customizes email body with recipient-specific variables
- Attaches files to the email

## Setup
1. Clone the repository to your local machine.
2. Install the required dependencies by running `pip install -r requirements.txt`.
3. Prepare your CSV file containing recipient data. Make sure it includes columns for recipient name, email address, and any other relevant variables.
4. Place your PDF files in the designated directory (`pdf_directory` variable in the script).

## Usage
1. Update the script (`email_script.py`) with your Gmail credentials, SMTP server details, and file paths.
2. Run the script using `python email_script.py`.
