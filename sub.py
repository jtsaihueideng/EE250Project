from typing import Iterable
import matplotlib.pyplot as plt
import numpy as np
from pydub import AudioSegment
from paho.mqtt import client as mqtt_client
import os
import sys

MAX_FRQ = 2000
SLICE_SIZE = 0.75 #seconds
WINDOW_SIZE = 1 #seconds

broker = 'broker.hivemq.com'
port = 1883
topic = "photos"
topic_sub = "audios"
client_id = 'xzcfghjt123'

# TODO: implement this dictionary
'''
NUMBER_DIC = {
    (100, 1653): "a",
    (200, 1653): "b",
    (300, 1653): "c",
    (400, 1653): "d",
    (500, 1653): "e",
    (600, 1653): "f",
    (700, 1653): "g",
    (800, 1653): "h",
    (900, 1653): "i",
    (1000,1653): "j",
    (1100, 1653): "k",
    (1200, 1653): "l",
    (1300, 1653): "m",
    (100, 1987): "n",
    (200, 1987): "o",
    (300, 1987): "p",
    (400, 1987): "q",
    (500, 1987): "r",
    (600, 1987): "s",
    (700, 1987): "t",
    (800, 1987): "u",
    (900,1987): "v",
    (1000,1987): "w",
    (1100,1987): "x",
    (1200,1987): "y",
    (1300,1987): "z"}
LOWER_FRQS = [100,200,300,400,500,600,700,800,900,1000,1100,1200,1300]
'''
NUMBER_DIC = {
    (100, 1653): "a",
    (150, 1653): "b",
    (200, 1653): "c",
    (250, 1653): "d",
    (300, 1653): "e",
    (350, 1653): "f",
    (400, 1653): "g",
    (450, 1653): "h",
    (500, 1653): "i",
    (550, 1653): "j",
    (600, 1653): "k",
    (650, 1653): "l",
    (700, 1653): "m",
    (100, 1987): "n",
    (150, 1987): "o",
    (200, 1987): "p",
    (250, 1987): "q",
    (300, 1987): "r",
    (350, 1987): "s",
    (400, 1987): "t",
    (450, 1987): "u",
    (500, 1987): "v",
    (550, 1987): "w",
    (600, 1987): "x",
    (650, 1987): "y",
    (700, 1987): "z"}
LOWER_FRQS = [100,150,200,250,300,350,400,450,500,550,600,650,700]
HIGHER_FRQS = [1653,1987]
FRQ_THRES = 20

'''
sub
'''
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
'''
'''

def get_max_frq(frq: Iterable[float], fft: Iterable[float]) -> float:
    """Returns the frequency with the highest amplitude in the given FFT array.

    Works by iterating through the FFT array and comparing the current amplitude
    to the maximum amplitude. If the current amplitude is greater than the
    maximum amplitude, the current frequency is saved as the maximum frequency
    and the current amplitude is saved as the maximum amplitude.
    
    Args:
        frq (Iterable[float]): The frequency array (x-axis in plots)
        fft (Iterable[float]): The FFT array (y-axis in plots)

    Returns:
        float: The frequency with the highest amplitude in the given FFT array
    """
    max_frq = 0
    max_fft = 0
    for idx in range(len(fft)):
        if abs(fft[idx]) > max_fft:
            max_fft = abs(fft[idx])
            max_frq = frq[idx]
    return max_frq

def get_peak_frqs(frq, fft):
    """Returns the two frequencies with the highest amplitudes in the given FFT array.
    
    Works by splitting the FFT array into two arrays, one for the lower frequencies
    and one for the higher frequencies. Then, it finds the frequency with the
    highest amplitude in each array and returns them as a tuple.

    Args:
        frq (Iterable[float]): The frequency array (x-axis in plots)
        fft (Iterable[float]): The FFT array (y-axis in plots)

    Returns:
        tuple: A tuple containing the two frequencies with the highest amplitudes in the given FFT array
    """
    #TODO: implement an algorithm to find the two maximum values in a given array

    #get the high and low frequency by splitting it in the middle (1000Hz)

    #spliting the FFT to high and low frequencies
    split_idx = len(frq) // 2
    low_frq = frq[:split_idx]
    low_frq_fft = fft[:split_idx]
    high_frq = frq[split_idx:]
    high_frq_fft = fft[split_idx:]

    return (get_max_frq(low_frq, low_frq_fft), get_max_frq(high_frq, high_frq_fft))

def get_number_from_frq(lower_frq: float, higher_frq: float) -> str:
    """Returns the number that corresponds to the given frequencies.
    
    Works by finding the closest frequency in the LOWER_FRQS and HIGHER_FRQS
    arrays and then using that index to find the corresponding number in the
    NUMBER_DIC dictionary.

    Args:
        lower_frq (float): The lower frequency
        higher_frq (float): The higher frequency

    Returns:
        str: The number that corresponds to the given frequencies
    """
    idx_lo = np.argmin(np.abs(np.array(LOWER_FRQS) - lower_frq))
    idx_hi = np.argmin(np.abs(np.array(HIGHER_FRQS) - higher_frq))

    return NUMBER_DIC[(LOWER_FRQS[idx_lo], HIGHER_FRQS[idx_hi])]

def main(file):

    client = connect_mqtt()
    subscribe(client)
    client.loop_forever()
    time.sleep(20)
    client.disconnect()

    print("Importing {}".format(file))
    audio = AudioSegment.from_mp3(file)

    sample_count = audio.frame_count()
    sample_rate = audio.frame_rate
    samples = audio.get_array_of_samples()

    #print("Number of channels: " + str(audio.channels))
    #print("Sample count: " + str(sample_count))
    #print("Sample rate: " + str(sample_rate))
    #print("Sample width: " + str(audio.sample_width))

    slice_sample_size = int(SLICE_SIZE*sample_rate)   #get the number of elements expected for [SLICE_SIZE] seconds

    n = slice_sample_size                            #n is the number of elements in the slice

    #generating the frequency spectrum
    k = np.arange(n)                                #k is an array from 0 to [n] with a step of 1
    slice_duration = n/sample_rate                   #slice_duration is the length of time the sample slice is (seconds)
    frq = k/slice_duration                          #generate the frequencies by dividing every element of k by slice_duration

    max_frq_idx = int(MAX_FRQ*slice_duration)       #get the index of the maximum frequency (2000)
    frq = frq[range(max_frq_idx)]                   #truncate the frequency array so it goes from 0 to 2000 Hz

    start_index = 0                                 #set the starting index at 0
    end_index = start_index + slice_sample_size      #find the ending index for the slice
    output = ''

    print()
    i = 1
    while end_index < len(samples):
        #print("Sample {}:".format(i), end=' ')
        i += 1

        sample_slice = samples[start_index:end_index] # get the sample slice

        #TODO: grab the sample slice and perform FFT on it
        fft = np.fft.fft(sample_slice)
        #TODO: truncate the FFT to 0 to 2000 Hz
        fft = fft[range(max_frq_idx)]        
        #TODO: calculate the locations of the upper and lower FFT peak using get_peak_frqs()

        low_frq = frq[range(int(len(frq)/2))]
        high_frq = frq[range(int(len(frq)/2), len(frq))]

        low_frq_fft = fft[range(int(len(fft)/2))]
        high_frq_fft = fft[range(int(len(fft)/2), len(fft))]
        peak_frqs = get_peak_frqs(frq, fft)
        #TODO: print the values and find the number that corresponds to the numbers

        #print(f"Low Frequency: {peak_frqs[0]:.2f}Hz High Frequency: {peak_frqs[1]:.2f}Hz ", end="")
        number = get_number_from_frq(peak_frqs[0], peak_frqs[1])
        output += number

        # print(f"Number: {number}")

        #Incrementing the start and end window for FFT analysis
        start_index += int(WINDOW_SIZE*sample_rate)
        end_index = start_index + slice_sample_size

    print("Program completed")
    print("Secret input: " + str(output))

if __name__ == '__main__':
    if len(sys.argv) != 2 or not os.path.isfile(sys.argv[1]):
        print("Usage: decode.py [file]")
        exit(1)
    main(sys.argv[1])
