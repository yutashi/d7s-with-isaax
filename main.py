# coding: utf-8
# Sample that outputs the value acquired by D7S.

from __future__ import print_function

import os
import time
import datetime

import grove_d7s
import ambient

# sensor instance
sensor = grove_d7s.GroveD7s()

# ambient instance
try:
    AMBIENT_CHANNEL_ID = int(os.environ['AMBIENT_CHANNEL_ID'])
    AMBIENT_WRITE_KEY = os.environ['AMBIENT_WRITE_KEY']
    CHECK_SPAN = int(os.environ.get('CHECK_SPAN', '30'))
    am = ambient.Ambient(AMBIENT_CHANNEL_ID, AMBIENT_WRITE_KEY)
except KeyError:
    print(KeyError)
    exit(1)

def main():
    while sensor.isReady() == False:
        print('.')
        time.sleep(1.0)
    
    print ("start")
    
    while True:
          time.sleep(1.0)
          if sensor.isEarthquakeOccuring() == True:
              eq = sensor.isEarthquakeOccuring()
              si = sensor.getInstantaneusSI()
              pga = sensor.getInstantaneusPGA()
              now = datetime.datetime.today()
              
              if si == None and pga == None:
                  continue
              payload = {
                  "d5": eq,
                  "d1": si,
                  "d2": pga,
                  "created": now.strftime("%Y/%m/%d %H:%M:%S")
              }
              try:
                  am.send(payload)
              except Exception as e:
                  print(e)

              print(now.strftime("[%Y/%m/%d %H:%M:%S]")
                        ,"SI=%.1f[Kine]" %si,"PGA=%d[gal]" %pga)

if __name__ == '__main__':
  main()
