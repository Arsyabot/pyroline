
ALBY="\n°ALBY PYROBOT Install•"
ALBY+="\n "
ALBY+="\nMenjalankan ALBY PYROBOT di Termux"
ALBY+="\n⚡ Sebelumnya Joinn Grup/Channel ⚡"
ALBY+="\n "
ALBY+="\n📣 Channel: @ruangprojects"
ALBY+="\n📢 GrupSupport: @ruangdiskusikami"
ALBY+="\n "
LUQ="\n "
echo -e $ALBY
echo -e $LUQ
echo "Waiting..."
echo -e $LUQ
pkg update -y && pkg upgrade
clear
echo -e $ALBY
echo -e $LUQ
echo "Menginstal python3"
echo -e $LUQ
pkg install python3
pkg install screen
pip3 install --upgrade pip
apt install postgresql
apt install neofetch
apt install ffmpeg
apt install curl
apt install megatools
apt install unzip
apt install wget
apt install liblapack-dev
apt install aria2
apt install zip
apt install sudo
apt install python3-wand
apt install python3-lxml
apt install postgresql-client
clear
echo -e $ALBY
echo -e $LUQ
echo "⚙️ Github Installer"
echo -e $LUQ
pkg install git -y
rm -rf pyroline
clear
echo -e $ALBY
echo -e $LUQ
echo "Cloning ALBY PYROBOT"
echo -e $LUQ
git clone https://github.com/PunyaAlby/pyroline
clear
echo -e $ALBY
echo -e $LUQ
echo "Menginstall Pakages"
echo -e $LUQ
cd pyroline
pip3 install --no-cache-dir -r requirements.txt
python3 installer/termux.py
