#  Linux Server Hardening & Log Monitoring

# Description

This project is designed to **secure a Linux server** and **monitor login activity** in real-time using a Python script. It provides:

- A hardening shell script to configure security tools like UFW and fail2ban
- A Python log monitoring script to detect login attempts and send email alerts
- updating and upgrading the system is very important as it updates often include security patches that fix vulnerabilities. If you don't update your system, it may be susceptible to attacks that target known weaknesses and to fix bugs, etc
- so i installed them then enabled them then just checked the status to see if they are working or not
- in the ufw (firewall) i blocked any incoming and allowed any outgoing its a default policy that makes your system more secure by blocking unauthorized access but still allowing your system to initiate outgoing connections
- Fail2ban is a security tool that protects your system from brute force attacks by monitoring log files for suspicious activity. When it detects multiple failed login attempts or other malicious patterns, it automatically blocks the offending IP addresses using firewall rules. This helps prevent unauthorized access and make you device secure
- and systemctl stop [service name ] is used to stop a servie that is not necessary and can be used to attack the sever or your device for example > apache2 if you dont use web server
- there is alot of more options to secure your device or server but i only used these as a start for me!
  











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

