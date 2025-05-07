#  Linux Server Hardening & Log Monitoring

# Description

This project is designed to **secure a Linux server** and **monitor login activity** in real-time using a Python script. It provides:

Hardening Shell Script:
Configures security tools like UFW (firewall) and Fail2ban for better protection
UFW: Blocks incoming connections by default, allowing outgoing ones to secure the system
Fail2ban: Prevents brute-force attacks by blocking IPs after multiple failed login attempts
System Updates: Always update your system to patch vulnerabilities and fix bugs and improve the system
Disabling Unnecessary Services: Use systemctl stop [service_name] to stop services like Apache2 if not in use, reducing attack vectors, etc


- # logs monitoring
- in the script i made a basic log monitor script so how it works?
- when runing the script if you trird to login and the password you entered is correct then it will print successful login and an email will be sent to you to show when the login happend? and by who? and of course the time the login occured
- on the other hand if you entered incorrect password for 3 times on row it will print suspicious activity detected: 3 failed login attempts, and send an email that there is a suspicious activity someone is trying to enter the account and entered an incorrect password for three times on row and for sure will also explain when this happend and by who and on which account
- i will keep learning so i can improve this script by also explain the ip of the one who is trying to enter the account and i will also add more info about this person so the code will be much effective
- you can as i said in how to run the script, make the code automatically whenever you open your device so you monitor the logs constantly, dont forget to take a look in the screen shots file to take an idea on how this process looks like

---

# Requirements (Python Libraries Used)
Here's a list of the Python standard libraries used in the project:

time
Used to introduce delays and control the interval of log file checks.

smtplib
Used to send email alerts through the SMTP protocol.

email.mime.text.MIMEText
Used to create the text content of the email message.

email.mime.multipart.MIMEMultipart
Used to build a structured email with headers and body (e.g., subject, from, to, content).

datetime
Used to retrieve and format the current date and time of login attempts or suspicious activities 

---

# Features

* Enable and configure UFW (firewall)  
* Install and run fail2ban to block brute-force attacks  
* Set up unattended security updates  
* Disable unnecessary services (like apache2)  
* Monitor `/var/log/auth.log` in real-time  
 Send email when:
* A successful login occurs
* Three consecutive failed logins happen

---

# How to Run
to run the hardening script do this: 
sudo bash hardening_script.sh

and to run the log monitor script do this: 
sudo python3 log_analyst.py
you can also type it without sudo it depenends on your settings

*you can auto run both of them on Boot if you need to monitor logs constantly using systemctl and systemd settings*


# Clone the project

```bash
git clone https://github.com/adhamsaleh13/Linux-Server-Hardening-Log-Monitor.git
cd Linux-Server-Hardening-Log-Monitor

