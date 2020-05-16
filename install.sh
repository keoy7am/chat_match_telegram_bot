sudo apt update -y && apt-get upgrade -y && apt-get autoremove -y
sudo apt install python3-pip
sudo pip3 install -r requirements.txt
sudo timedatectl set-timezone Asia/Taipei
sudo timedatectl # Show timezone