#twillo api
from twilio.rest import Client
#speech recognition api
import speech_recognition as sr
#operating system dependent functionality
import os
import re
#webbrowser
import webbrowser
#HTTP requests
import requests
#computer vision
import cv2
#face_recognition A.I
import face_recognition
import numpy as np
import time

#twilioAccount Sid and Auth Token from 
account_sid = '' #enter account sid here
auth_token = '' #enter account token here
client = Client(account_sid, auth_token)

# Camera 0 is the integrated web cam on my netbook
camera_port = 0
 
#Number of frames to throw away while the camera adjusts to light levels
ramp_frames = 30

#loads known image of user
##paste path to a pic of your face
User_image = face_recognition.load_image_file("file path")
User_face_encoding = face_recognition.face_encodings(User_image)[0]


# Now we can initialize the camera capture object with the cv2.VideoCapture class.
# All it needs is the index to a camera port.
camera = cv2.VideoCapture(camera_port)
 
# Captures a single image from the camera and returns it in PIL format
def get_image():
 # read is the easiest way to get a full image out of a VideoCapture object.
 retval, im = camera.read()
 return im

def talk(audio):
  #voice agent 
    print(audio)
    for line in audio.splitlines():
        os.system("say " + audio)


def myCommand():
    #"listens for commands"
    
    # create recognizer instance
    r = sr.Recognizer()  

    #using default mic 
    with sr.Microphone() as source:
        print('Ready...')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1) 
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio)
        talk('You said: ' + command + '\n')

    #loop back to continue to listen for commands if unrecognizable speech is received
    except sr.UnknownValueError:
        print('Your last command couldn\'t be heard')
        command = myCommand();

    return command


def assistant(command):
    #"if statements for executing commands"

    #play relaxing music 
    if 'play music' in command:
        
        reg_ex = re.search('play music(.*)', command)
        url = 'https://www.youtube.com/watch?v=ivNIpLdzh7M&t=1160s'
        webbrowser.open(url)
        print('Done!')

    #open a website
    elif 'open website' in command:
        reg_ex = re.search('open website (.+)', command)
        if reg_ex:
            domain = reg_ex.group(1)
            url = 'https://www.' + domain + ".com"
            webbrowser.open(url)
            print('Done!')
        else:
            pass

    #tell a joke
    elif 'tell me a joke' in command:
        res = requests.get(
                'https://icanhazdadjoke.com/',
                headers={"Accept":"application/json"}
                )
        if res.status_code == requests.codes.ok:
            talk(str(res.json()['joke']))
        else:
            talk('oops!I ran out of jokes')

     #tell a fact       
    elif 'fact of the day' in command:
        res = requests.get(
                'https://uselessfacts.jsph.pl//random.json?language=en',
                headers={"Accept":"application/json"}
                )
        if res.status_code == requests.codes.ok:
            talk(str(res.json()['text']))
        else:
            talk('oops!I ran out offacts')

    #send text
   

# Take the actual image we want to keep
camera_capture = get_image()
#Paste path where you would like the pic taken with your web cam to be stored so it can compare 
file = ""

# A nice feature of the imwrite method is that it will automatically choose the
# correct format based on the file extension you provide. Convenient!
cv2.imwrite(file, camera_capture)

#compares loaded image to new image from web cam
unknown_picture = face_recognition.load_image_file(file)
unknown_face_encoding = face_recognition.face_encodings(unknown_picture)[0]
results = face_recognition.compare_faces([User_face_encoding], unknown_face_encoding)

#loop to continue executing multiple commands
if results[0] == True:
    talk('Hello, what would you like to do?')

    

    while results[0] == True:
      assistant(myCommand())
      
        
      
