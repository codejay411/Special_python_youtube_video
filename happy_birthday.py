import pyttsx3

engine = pyttsx3.init('sapi5')
voices= engine.getProperty('voices') #getting details of current voice
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait() #Without this command, speech will not be audible to us.



if __name__=="__main__" :
    speak("Hapy Birthday Shubham Chaudhari, Many many happy returns of the day. And i want to say few words for you that 
    Hope your special day brings you all that your heart desires! Here’s wishing you a day full of pleasant surprises! 
    On your birthday we wish for you that whatever you want most in life it comes to you just the way you imagined it or better.")
