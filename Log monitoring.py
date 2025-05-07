#python script to monitor logs

import time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime

Email_sender = "enter the email sender her @gmail.com"
Email_password = "enter the password of the email here (the app password)" # you need to put the app password from your google account settings and type it her
Email_receiver = "enter the email receiver her gmail.com"

Log_file = "/var/log/auth.log"
Failed_Keywords = ["authentication failure", "failed su to"]
Success_Keywords = ["session opened for"]

def send_email(subject, body):
msg = MIMEMultipart()
msg["From"] = Email_sender
msg["To"] = Email_receiver
msg["Subject"] = subject
msg.attach(MIMEText(body, "plain"))
try:
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(Email_sender, Email_password)
server.send_message(msg)
server.quit()
print("Email sent successfully.")
except Exception as e:
print(f"Failed to send email: {e}!")

def monitor_log():
print("Monitoring auth.log for login attempts...")
failed_count = 0
last_success_line = ""

with open(Log_file, "r") as file:  
    file.seek(0, 2)  
    while True:  
        line = file.readline()  
        if not line:  
            time.sleep(1)  
            continue  

        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  

        if any(keyword in line for keyword in Failed_Keywords):  
            failed_count += 1  
            if failed_count== 3:  
                print("Suspicious activity detected: 3 failed login attempts.")  
                send_email(  
                    "Suspicious Activity: 3 Failed Login Attempts",  
                    f"Detected 3 failed login attempts in a row at:\n{current_time}\n\nLast attempt details:\n{line.strip()}"  
                )  
                failed_count = 0  

        elif any(keyword in line for keyword in Success_Keywords):  
            print("Successful Login!")   
            if line.strip() != last_success_line:  
                send_email(  
                    "Successful Login Detected",  
                    f"A successful login occurred at:\n{current_time}\n\nDetails:\n{line.strip()}"  
                )  
                last_success_line = line.strip()  
            failed_count = 0

if name == "main":
monitor_log()
