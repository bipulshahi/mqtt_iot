import time
import serial

import urllib3

http = urllib3.PoolManager()
ser = serial.Serial('COM7',9600)
time.sleep(2)

for i in range(5):
     a = ser.readline()
     b = a.decode()
     c = b.rstrip()
     t = c.split(" ")[0]
     h = c.split(" ")[1]
     
     URL = 'https://api.thingspeak.com/update?api_key=57JYXAWTXH13QKJT'
     F_URL = URL + '&field1=%s&field2=%s'%(t,h)
     s = http.request('GET',F_URL)
     print('Message Published')
     print(F_URL)
     s.close()
     time.sleep(30)
