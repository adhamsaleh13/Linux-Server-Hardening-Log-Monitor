#  Linux Server Hardening & Log Monitoring

# Description

This project is designed to **secure a Linux server** and **monitor login activity** in real-time using a Python script. It provides:

- A hardening shell script to configure security tools like UFW and fail2ban
- A Python log monitoring script to detect login attempts and send email alerts

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
to run the hardening script do this
sudo bash hardening_script.sh

and to run the log monitor script do this
sudo python3 log_analyst.py
you can also type it without sudo it depenends on your settings 

# Clone the project

```bash
git clone https://github.com/adhamsaleh13/linux-server-hardening-log-monitor.git
cd linux-server-hardening-log-monitor
