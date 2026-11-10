# TASK 3: Task Automation with Python Scripts
# Intern: FAISUL HAMEER AFANA | ID: CA/DF1/434642
import re
def extract_emails():
    sample = "Contact us at support@codealpha.tech and hr@codealpha.com and faisul778@gmail.com"
    with open("input.txt", "w") as f: f.write(sample)
    with open("input.txt", "r") as f:
        emails = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', f.read())
    with open("extracted_emails.txt", "w") as f:
        for e in emails: f.write(e+"\n")
    print(f"Extracted {len(emails)} emails: {emails}")
extract_emails()
