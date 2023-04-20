from pydub import AudioSegment
 # enter the path of your audio file
sound1 = AudioSegment.from_mp3("/home/tytionex/Documents/project/audio/sample1.mp3")
sound2 = AudioSegment.from_mp3("/home/tytionex/Documents/project/audio/sample2.mp3")
  
def choose_option():
    print("Audio file editing by pydub Package\n")
    print("1. Audio Cut ") ;
    print("2. Sound Increase and Decrease") ;
    print("3. Merge Two Songs") ;
    choose = int(input("Choose Option = "))
    if choose == 1:
        audio_cut()
    elif choose == 2:
        sound_Increase() 
    elif choose == 3:
        merge_two_songs()
    elif choose >3:
        print("You Choose Wrong Input") ;
  
def audio_cut():
    
    StrtMin = int(input("Enter the Start Min " ))
    StrtSec = int(input("Enter the Start Sec ")) 

    EndMin = int(input("Enter the End Min "))
    EndSec = int(input("Enter the End Sec "))

    sound2 = int(input("Sound Increase or Sound Decrease example 5 or -5 "))

    StrtTime = StrtMin*60*1000+StrtSec*1000
    EndTime = StrtMin*60*1000+EndSec*1000
  
    print("Extracting Sound from your audio file")
    extract = sound[StrtTime:EndTime]
  
# Saving file in required location
def sound_Increase():
    if sound2>=0:
        loudmusic = extract + sound2 
        loudmusic.export("/home/dachman/Desktop/walker2.mp3", format="mp3")
    else:
        lowmusic = extract - sound2 
        lowmusic.export("/home/dachman/Desktop/walker2.mp3",format="mp3")
  
# merge two audio
def merge_two_songs():
    print("Sound Overlay")
    sound3 = sound1.append(sound2)
    sound3.export("/home/tytionex/Documents/project/audio/sample_merge_audio",format="mp3")
    
choose_option()
