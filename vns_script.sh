#!/bin/bash

# UPGRADE
sudo apt-get update && sudo apt-get -y upgrade && sudo apt-get -y autoremove && sudo apt-get -y dist-upgrade && sudo apt-get -y autoremove

# install VNC
sudo apt install xfce4 xfce4-goodies tightvncserver

# fix xstartup file
echo "#!/bin/bash" > ~/.vnc/xstartup
echo "xrdb $HOME/.Xresources" >> ~/.vnc/xstartup
echo "startxfce4 &" >> ~/.vnc/xstartup 

# iptables- allow only localhost and DENY all
sudo iptables -A INPUT -p tcp -s localhost --dport 5901 -j ACCEPT
sudo iptables -A INPUT -p tcp --dport 5901 -j DROP
