import ssl
import paho.mqtt.client as mqtt
import time
import serial

ser = serial.Serial('COM7',9600)
time.sleep(2)

IoT_protocol_name = "x-amzn-mqtt-ca"
aws_iot_endpoint = "amwmnb948lrc8-ats.iot.ap-south-1.amazonaws.com"

ca = "D:/aws_certi/VeriSign-Class 3-Public-Primary-Certification-Authority-G5(3).pem" 
cert = "D:/aws_certi/c8f3d301c0-certificate.pem.crt.txt"
private = "D:/aws_certi/c8f3d301c0-private.pem.key"

ssl_context = ssl.create_default_context()
ssl_context.set_alpn_protocols([IoT_protocol_name])
ssl_context.load_verify_locations(cafile=ca)
ssl_context.load_cert_chain(certfile=cert, keyfile=private)

client = mqtt.Client()
client.tls_set_context(context=ssl_context)

client.connect(aws_iot_endpoint, port=443)
client.loop_start()

i = 0
while (i < 2):

     a = ser.readline()
     b = a.decode()
     c = b.rstrip()
     t = c.split(" ")[0]
     h = c.split(" ")[1]

     print("try to publish","Temperature:",t,"Humidity:",h)
     client.publish('iot/topic',
                    '{"Temperature": '+' "'+str(t)+'" '+' "Humidity": '+' "'+str(h)+'" }')
     time.sleep(2)
     i += 1
