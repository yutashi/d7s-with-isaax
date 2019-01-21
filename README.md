# d7s-grove-raspberrypi

Send Ambient Sensored data.

## Sensor Documentation
- [English](https://github.com/omron-devhub/d7s-grove-raspberrypi/blob/master/README.md)
- [Japanase](https://github.com/omron-devhub/d7s-grove-raspberrypi/blob/master/README_ja.md)

## Installation

Install GrovePi+ Driver

```bash
$ sudo curl -kL dexterindustries.com/update_grovepi | bash
$ sudo raspi-config
I2CとSPIを有効にする
$ sudo reboot
```

Install Python3 modules

```bash
pip3 install matplotlib
pip3 install smbus2
pip3 install git+https://github.com/AmbientDataInc/ambient-python-lib.git
```

## Usage

```bash
$ AMBIENT_CHANNEL_ID=*** AMBIENT_WRITE_KEY=***** python3 main.py
```

## Licence

Licensed under the MIT License.
