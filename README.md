https://codelic.co/BlogDetail/WMgrb5Ko4twSTOrICuX7

```bash
sudo raspi-config
sudo nano /boot/firmware/config.txt

sudo nano /etc/ppp/peers/sim7080g
sudo nano /etc/chatscripts/sim7080g.chat

sudo chat -v -f /etc/chatscripts/sim7080g.chat

sudo nano /etc/ppp/chap-secrets

sudo usermod -a -G dialout $USER

sudo reboot

sudo pppd call sim7080g

ifconfig
```



https://www.youtube.com/watch?v=lXpFUUHDWGU

Would you like a login shell to be accessible over serial? に対して No を選択
Would you like the serial port hardware to be enabled? に対して Yes を選択

# UART を有効化
enable_uart=1