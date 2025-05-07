# Update the system
echo "Updating the system please wait..."

sudo apt update && sudo apt upgrade -y
sudo apt install unattended-upgrades

# Enable UFW (firewall)
echo "Configuring Firewall..."

sudo ufw enable
sudo ufw deny incoming
sudo ufw allow outgoing
sudo ufw status

# Disable unnecessary services
echo "Disabling unnecessary services..."

sudo systemctl list-units --type=service
sudo systemctl stop apache2
sudo systemctl disable apache2

# Enable fail2ban for brute-force protection
echo "Configuring Fail2Ban..."

sudo apt install -y fail2ban
sudo systemctl enable fail2ban
sudo systemctl start fail2ban
sudo systemctl status fail2ban

# there is alot of options i just used a few but you can add on this for sure!

echo "System hardening completed!"
