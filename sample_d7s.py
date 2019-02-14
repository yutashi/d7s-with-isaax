# coding: utf-8
# Sample that outputs the value acquired by D7S.

from __future__ import print_function

import time
import datetime

import grove_d7s

sensor = grove_d7s.GroveD7s()


def main():
    if sensor.isReady() == False:
        print('.')
        time.sleep(1.0)

    print("start")

    i = 0
    while True:
        time.sleep(1)
        si = sensor.getInstantaneusSI()
        pga = sensor.getInstantaneusPGA()
        now = datetime.datetime.today()
        eq = sensor.isEarthquakeOccuring()

        # センサーの初期化中は値がNoneになるので処理をスキップ
        if si == None and pga == None:
            continue

        i += 1
        print(now.strftime("[%Y/%m/%d %H:%M:%S]"),
                "SI={}[Kine]".format(si), 
                "PGA={}[gal]".format(pga),
                "EQ=%s" % eq)
        # 地震を検知して10回値を取得したらリセットを行う
        if i > 10:
            # センサーを初期化
            sensor.writeByte(sensor.REG_MODE, 0x02)
            i = 0


if __name__ == '__main__':
    main()
