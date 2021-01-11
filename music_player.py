from pygame import mixer

mixer.init()
mixer.music.load("god.mp3")
mixer.music.set_volume(0.8)
mixer.music.play()

print("press 'p' for pause and press 'q' for resume")
print("press 'x' for exit the program or music")
while(True):
    # print("press 'p' for pause and press 'q' for resume")
    # print("press 'x' for exit the program or music")
    
    query = input("")
    if(query=='p'):
        mixer.music.pause()
    elif(query == 'q'):
        mixer.music.unpause()
    elif(query == 'x'):
        mixer.music.stop()
        break
    else:
        print("unnecessary command")

