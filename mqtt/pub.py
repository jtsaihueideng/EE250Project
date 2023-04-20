'''
Source: 
https://highvoltages.co/iot-internet-of-things/mqtt/audio-files-using-mqtt/
'''
import time
from paho.mqtt import client as mqtt_client

broker = 'broker.hivemq.com'
port = 1883
topic = "audios"
client_id = 'xzcfghjt12'

def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Successfully connected to MQTT broker")
        else:
            print("Failed to connect, return code %d", rc)

    client = mqtt_client.Client(client_id)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client

def publish(client):
    with open("./sample1.mp3",'rb') as file:

        filecontent = file.read()
        byteArr = bytearray(filecontent)
        #print(byteArr)
        print("sent byte arr")
        result = client.publish(topic,byteArr,2)
    msg_status = result[0]
    if msg_status == 0:
        print(f"message sent to topic {topic}")
    else:
        print(f"Failed to send message to topic {topic}")

def main():
    client = connect_mqtt()
    client.loop_start()
    publish(client)
    time.sleep(5)
    client.loop_stop()
   # client.loop_forever()


if __name__ == '__main__':
    main()
