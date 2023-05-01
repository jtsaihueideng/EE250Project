import os
import time
from pydub import AudioSegment
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
    with open("./message.mp3",'rb') as file:

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
    
    #taking input message
    message = input('What is your input!\n')
   
    # stripping the white spaces
    stripped_message = message.replace(" ", "").replace("\t", "").replace("\n", "")
    stripped_message = stripped_message.lower()
    print(stripped_message)

    path = os.path.realpath(__file__)
    dir = os.path.dirname(path) + "/audio/testmerge/"
    print(dir)

    # Define the file names to be appended
    file_names = []
    for letter in stripped_message:
        print(letter)
        letterDir = dir + letter + ".mp3"
        file_names.append(letterDir)

    print(file_names)

    '''
        Convert the input message to audio segment
    '''

    # Create an empty audio segment object
    output_audio = AudioSegment.empty()

    # Iterate over the file names and append the audio segments to the output audio object
    for file_name in file_names:
        audio = AudioSegment.from_file(file_name, format='mp3')
        output_audio += audio

    # Export the output audio to a new mp3 file
    output_audio.export('message.mp3', format='mp3')

    '''
        Send audio file 
    '''
    time.sleep(2);
    client = connect_mqtt()
    print("loop_start")
    client.loop_start()
    print("client")
    publish(client)
    client.loop_stop()
    #client.loop_forever()



if __name__ == "__main__":

    main()
