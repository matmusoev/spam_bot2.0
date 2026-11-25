import smtplib
import time
from email.message import EmailMessage

# --- CONFIGURATION ---
SENDER_NAME = "Todd Ambridge (Computer Science)"
SENDER_EMAIL = "t.waughambridge@gmail.com"
APP_PASSWORD = "[PASSWORD]"  # 16-char Gmail App Password
EMAIL_LIST_FILE = "emails.txt"

SUBJECT = "Update on upcoming assignment deadlines"
BODY = """Hi everyone,

I hope you are having a good week so far. I just wanted to write to you to quickly let you know about a change to the upcoming assignment deadlines.

Due to a recent incident involving Gandalf the Grey's fight with Solomon the White, we have decided to push all upcoming assignment deadlines back by **one week**. Updated submission dates will be reflected on your Canvas course pages shortly.

We recognise that unexpected magical skirmishes can be disruptive to your studies, so we want to ensure everyone has sufficient time to complete their work without additional stress. If you have been particularly affected by the incident or need further support, please do reach out to your personal tutor or visit a member of academic staff during their office hours (listed in the Student Handbook).

*Note: While we are aiming for a one-week delay across all modules, please keep an eye on Canvas for any module-specific updates from your lecturers.*

All the best, and let me know if there are any questions,

Dr Todd Waugh Ambridge
Associate Professor
University of Birmingham
School of Computer Science
"""

def send_bulk_emails():
    # 1. Read and clean the email addresses from the file
    try:
        with open(EMAIL_LIST_FILE, "r", encoding="utf-8") as file:
            # Strip whitespace and skip empty lines
            recipients = [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        print(f"Error: Could not find '{EMAIL_LIST_FILE}'.")
        return

    if not recipients:
        print("The email list is empty.")
        return

    print(f"Loaded {len(recipients)} email addresses. Connecting to server...")

    # 2. Connect to the SMTP server once and loop through recipients
    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(SENDER_EMAIL, APP_PASSWORD)

            for recipient in recipients:
                msg = EmailMessage()
                msg["From"] = SENDER_NAME
                msg["To"] = recipient
                msg["Subject"] = SUBJECT
                msg.set_content(BODY)

                try:
                    smtp.send_message(msg)
                    print(f"[SUCCESS] Sent to {recipient}")
                except Exception as e:
                    print(f"[FAILED] Could not send to {recipient}: {e}")

                # Pause 3 seconds between emails to avoid spam triggers
                time.sleep(3)

    except smtplib.SMTPAuthenticationError:
        print("Authentication failed. Check your email and 16-character App Password.")
    except Exception as e:
        print(f"Server connection error: {e}")

if __name__ == "__main__":
    send_bulk_emails()