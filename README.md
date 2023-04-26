# EE250 Project: Cryptic Waves

## Team Members

Lab Partner: Julie Deng

Lab Partner: Tyler Chen

## Description
Implementation of substitution cipher. User's messages are converted into an .mp3 file by using a freqency to letter mapping table and sent over MQTT protocol. Client subscribers can receive the audio file and decode the message with signal processing. Another subscriber acts as a database to store these mp3 files.

## Compile/Execution Instructions

1. Use the following command to execute the main file

```
python3 main.py
```

2. If the user chooses to send data, the console will prompt the user to enter a string. After the user finishes entering the input, the console will produce a mp3 file called 'message.mp3', which will be published using the MQTT protocol. If the user chooses to read data, the program will subscribe using MQTT to get 'message.mp3', and then the console will print the decoded output. 

## External Libraries
- AudioSegment from pydub
- os
- Iterable from typing
- matplotlib
- NumPy
- PyDub
- Sys
- Argparse
- Pathlib
- Paho.mqtt.client
- Time
- Datetime
- Socket
