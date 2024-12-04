```bash
sudo apt-get -y install pppconfig
sudo pppconfig myppp
sudo pon myppp
ifconfig


ip route

sudo ip route del default via 10.34.36.1
sudo ip route add default via 10.64.64.64 dev ppp0
sudo ip route add default via 100.115.147.41 dev ppp0


sudo ifconfig ppp0 down
sudo ifconfig ppp0 up

sudo chmod 0777 /dev/ttyAMA0


```

https://qiita.com/CLCL/items/99acf6dd3bd9c251f1aa