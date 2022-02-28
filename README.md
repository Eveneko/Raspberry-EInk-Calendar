# Raspberry EInk Calendar

基于树莓派的电子墨水日历

## Hardware

- Raspberry Pi Zero 2W
- Waveshare 7.5inch e-paper (B)
  - 170.2 * 111.2 * 1.25 mm
  - Red, Black, White
- PiSugar2 for Raspberry Pi Zero (Tindie)

## Build

### Waveshare 7.5inch e-paper (B)

#### 开启SPI接口

```
sudo raspi-config

```

选择Interfacing Options -> SPI -> Yes 开启SPI接口

```
sudo reboot
```

#### 安装库

- BCM2835

```
wget http://www.airspayce.com/mikem/bcm2835/bcm2835-1.68.tar.gz
tar zxvf bcm2835-1.68.tar.gz 
cd bcm2835-1.68/
sudo ./configure && sudo make && sudo make check && sudo make install
# 更多的可以参考官网：http://www.airspayce.com/mikem/bcm2835/
```

- 安装wiringPi

```
sudo apt-get install wiringpi
# 对于树莓派2019年5月之后的系统（早于之前的可不用执行），可能需要进行升级：
wget https://project-downloads.drogon.net/wiringpi-latest.deb
sudo dpkg -i wiringpi-latest.deb
gpio -v
# 运行gpio -v会出现2.52版本，如果没有出现说明安装出错
 
# Bullseye分支系统使用如下命令：
git clone https://github.com/WiringPi/WiringPi
cd WiringPi
./build
```

- 安装python函数库

```
python3 -m pip install -r requirements.txt
```

> selenium 安装3.x，4.x目前存在问题

- 安装chromium-chromedriver

```
sudo apt-get install chromium-chromedriver
```

### Web Server

#### Structure

#### Features

- [ ] 配置面板
- [ ] 文字屏显 API

## Reference

- wiki
  - https://www.waveshare.net/wiki/7.5inch_e-Paper_HAT_(B)
- project
  - https://github.com/speedyg0nz/MagInkCal
  - https://github.com/aceisace/Inkycal
  - https://github.com/zli117/EInk-Calendar
