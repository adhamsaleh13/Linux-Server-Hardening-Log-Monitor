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
- # logs monitoring
- in the script i made a basic log monitor script so it works?
- when runing the script if you trird to login and the password you entered is correct then it will print successful login and an email will be sent to you to show when the login happend? and by who? and of course the time the login occured
- on the other hand if you entered incorrect password for 3 times on row it will print suspicious activity detected: 3 failed login attempts, and send an email that there is a suspicious activity someone is trying to enter the account and entered an incorrect password for three times on row and for sure will also explain when this happend and by who and on which account
- i will keep learning so i can improve this script by also explain the ip of the one who is trying to enter the account and i will also add more info about this person so the code will be much effective
- you can as i said in how to run the script, make the code automatically whenever you open your device so you monitor the logs constantly, dont forget to take a look in the screen shots file to take an idea on how this process looks like
 
  











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

