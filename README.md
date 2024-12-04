https://codelic.co/BlogDetail/WMgrb5Ko4twSTOrICuX7

```bash
sudo raspi-config
sudo nano /boot/firmware/config.txt

sudo rm /etc/ppp/peers/sim7080g
sudo rm /etc/chatscripts/sim7080g.chat
sudo nano /etc/ppp/peers/sim7080g
sudo nano /etc/chatscripts/sim7080g.chat

sudo chat -v -f /etc/chatscripts/sim7080g.chat

sudo nano /etc/ppp/chap-secrets
sudo nano /etc/ppp/pap-secrets

sudo usermod -a -G dialout $USER

sudo reboot

sudo pppd call sim7080g

sudo journalctl -ex

ifconfig
```

```bash
cd ~/Documents/SIM7080G_Cat_M_NB_IoT_HAT_Code/RaspberryPi/python/mqtt/
sudo python mqtt.py
```

```bash
sudo pppd /dev/ttyAMA0 115200 connect '/usr/sbin/chat -v -f /etc/chatscripts/sim7080g.chat'
```




https://www.youtube.com/watch?v=lXpFUUHDWGU

Would you like a login shell to be accessible over serial? に対して No を選択
Would you like the serial port hardware to be enabled? に対して Yes を選択

# UART を有効化
enable_uart=1


一かい公式のやつをやると起動できるようになる。

https://www.waveshare.com/wiki/SIM7080G_Cat-M/NB-IoT_HAT#Test_MQTT



先にLTEとかの設定が必要だ