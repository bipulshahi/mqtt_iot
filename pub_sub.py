import ssl
import time
import datetime
import paho.mqtt.client as mqtt

IoT_protocol_name = "x-amzn-mqtt-ca"
aws_iot_endpoint = "amwmnb948lrc8-ats.iot.ap-south-1.amazonaws.com"

ca = "D:/aws_certi/VeriSign-Class 3-Public-Primary-Certification-Authority-G5(3).pem" 
cert = "D:/aws_certi/c8f3d301c0-certificate.pem.crt.txt"
private = "D:/aws_certi/c8f3d301c0-private.pem.key"

ssl_context = ssl.create_default_context()
ssl_context.set_alpn_protocols([IoT_protocol_name])
ssl_context.load_verify_locations(cafile=ca)
ssl_context.load_cert_chain(certfile=cert, keyfile=private)

def on_connect(client, userdata, flags, rc):
     print('Connected with code:' , rc)
     client.subscribe("test/a")
              
def on_message(client,userdata,msg):
     m = msg.payload
     m = m.decode()
     m = m.strip()
     print(m)
     print(type(m))

client = mqtt.Client()

client.on_connect = on_connect
client.on_message = on_message

client.tls_set_context(context=ssl_context)
client.connect(aws_iot_endpoint, port=443)

client.loop_start()

time.sleep(2)
'''
while True:
              client.publish("test/b","Hello Everyone")
              print('Message Published')
              time.sleep(3)
'''
