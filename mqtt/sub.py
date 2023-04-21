'''
Source: 
https://highvoltages.co/iot-internet-of-things/mqtt/audio-files-using-mqtt/
'''

from paho.mqtt import client as mqtt_client

broker = 'broker.hivemq.com'
port = 1883
topic = "photos"
topic_sub = "audios"
client_id = 'xzcfghjt123'

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

def subscribe(client: mqtt_client):
    def on_message(client, userdata, msg):
        f = open('receive.mp3', 'wb')
        f.write(msg.payload)
        f.close()
        print ('Audio received')

    client.subscribe(topic_sub)
    client.on_message = on_message

def main():
    client = connect_mqtt()
    subscribe(client)
    client.loop_forever()
    
if __name__ == '__main__':
    main()
