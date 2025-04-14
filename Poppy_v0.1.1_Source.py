# -*- coding: utf-8 -*-

"""
###PACKAGES TO INSTALL###

    PyAudio
    SpeechRecognition
    pydub
    gtts
    pyjokes
    
    also install:
    flac utility: https://xiph.org/flac/download.html
    FFMpeg: https://phoenixnap.com/kb/ffmpeg-windows
        
        

"""


#Import libraries

import speech_recognition as sr
import winsound
import pyjokes
import webbrowser
import time
import textwrap
from gtts import gTTS
from pydub import AudioSegment as aSegment
from datetime import datetime


#Input function
def askQ(question):
    
    #Assign speech recognizer and microphone as variables
    r = sr.Recognizer()
    m = sr.Microphone()
    
    with m as source:
        r.adjust_for_ambient_noise(source)
        sayLine(str(question))
        audio = r.listen(source)
        
    try:
        speech = str(r.recognize_google(audio))
        print("")
        print("User: "+speech)
        speech = " "+speech.lower()+" "
        return speech
    
    except sr.UnknownValueError:
        stop = False
        while stop == False:
        
            with m as source:
                sayLine("Sorry, I didn't catch that, what did you say?")
                audio = r.listen(source)
            try:
                speech = str(r.recognize_google(audio))
                print("")
                print("User: "+speech)
                speech = " "+speech.lower()+" "
                return speech
        
            except sr.UnknownValueError:
                print("Unknown response")
                
            except sr.RequestError:
                sayLine("Sorry, I couldn't connect to Googles speech recognition API.")
                return None
        
    except sr.RequestError:
        sayLine("Sorry, I couldn't connect to Googles speech recognition API.")
        return None


def silentListen():
    #Assign speech recognizer and microphone as variables
    r = sr.Recognizer()
    m = sr.Microphone()
    
    stop = False
    while stop == False:
        with m as source:
            print("Adjusting for background noise...")
            r.adjust_for_ambient_noise(source)
            print("Listening...")
            audio = r.listen(source)
    
        try:
            speech = str(r.recognize_google(audio))
            print("User: "+speech)
            speech = " "+speech.lower()+" "
            return speech
            stop = True
    
        except sr.UnknownValueError:
            print("Unrecognized response")
    
        except sr.RequestError:
            return None
            stop = True


#Response function
def sayLine(response):
    
    print("Preparing TTS line...")
    #Convert text to speech
    responseTTS = gTTS(text=str(response), lang="en")
    responseTTS.save("responseTTS.mp3")
    
    #Convert .mp3 to .wav because winsound doesn't support .mp3
    responseWav = aSegment.from_mp3("responseTTS.mp3")
    responseWav.export("responseTTS.wav", format="wav")
    
    #Give response
    print("")
    print("Poppy: "+textwrap.dedent(str(response)))
    winsound.PlaySound("responseTTS.wav", winsound.SND_FILENAME)

#Timer function
def timer(seconds):
    while seconds > 0:
        mins = seconds // 60
        hrs = mins // 60
        secs = seconds % 60
        mins = mins % 60
        timer = f'{hrs:02}:{mins:02}:{secs:02}'
        print(timer, end="\r")
        time.sleep(1)
        seconds -= 1
    sayLine("Your timer is going off!")


print("Building intro message...")
#Intro Message
sayLine("""
        Hi! My name's Poppy! I'm happy to be your virtual assistant!
        I'll just be here listening in the background. 
        If you need me, you can call me by saying "Hey Poppy"
        """)



###MAIN LOOP###
shutdown = False

while shutdown == False:
    
    command = silentListen()
    
    if " hey poppy " in command or " hey papi " in command or " hey puppy " in command:
        
        #Initial phrase and stop signal
        qPhrase = "What do you need?"
        stop = False
        
        ###QUESTION LOOP###
        while stop == False:
            
            #Ask question
            command = askQ(qPhrase)
            
            #Ignore empty commands
            if command:
                #
                #
                ###Help command
                if " list commands " in command or " help " in command:
                    sayLine("""
                        I've got a few commands so far. 
                        You can say "what time is it" for me to give you the current date and time. 
                        You can say "timer" to have me set a timer. 
                        Make sure to specify the number of seconds, minutes, and hours to set it for!
                        You can say "tell me a joke" for me to tell you a random computer tech joke. 
                        You can say "search for" followed by a search term for me to search the web for you. 
                        You can also say "show me" followed by a search term for me to look for images online. 
                        
                        Finally, you can say "shut down" for me to stop listening entirely. 
                        You will need to restart me from your computer in order for me to listen again if you do though. 
                        
                        Maddy is sure to give me some more functionality soon! 
                        If you have any ideas, feel free to send them over to her, and maybe she'll add it! 
                        
                        """)
                        
                    qPhrase = "What would you like me to do?"
                #
                #
##############################################################################
############################### WRITE ADDITIONAL COMMANDS HERE ###############
                #
                #
                ###Time command
                elif " time " in command:
                    
                    #Prepare time string
                    currentTime = str(datetime.now().time()).split(".")
                    currentTime = currentTime[0].split(":")
                    if int(currentTime[0]) > 12:
                        currentTime = str( int(currentTime[0]) -12 ) + ":" + currentTime[1] + " PM"
                    else:
                        currentTime = currentTime[0] + ":" + currentTime[1] + " AM"
                        
                    #Prepare date string
                    date = str(datetime.now().date())
                        
                    #Give response    
                    line = "The current time is "+currentTime+". Today is "+date
                    sayLine(line)
                    qPhrase = "Do you need anything else?"
                #        
                #
                ###Say hello
                elif " hello " in command or " hi " in command:
                    sayLine("Oh, hello! Hope you're having a great day!... What... were you expecting me to say, hello world?")
                    qPhrase = "Anyway, did you need anything?"
                #        
                #        
                ###Joke command
                elif " joke " in command:
                    
                    #Joke loop init
                    stopJokes = False
                    anotherJoke = "Do you want to hear another?"
                    while stopJokes == False:
                        
                        #Tell joke
                        sayLine(str(pyjokes.get_joke()))
                        
                        #Ask if they want another
                        command = askQ(anotherJoke)
                        
                        if " yes " in command or " yeah " in command or " yep " in command or " yup " in command or " sure " in command:
                            anotherJoke = "Another one?"
                        
                        elif " no " in command or " nope " in command or " nah " in command:
                            qPhrase = "K then, need anything else?"
                            stopJokes = True
                            
                        else:
                            qPhrase = "I'm not sure what you said... Did you need anything else?"
                            stopJokes = True
                #            
                #        
                ###Search command    
                elif command.startswith(" search for "):
                    
                    #Build Google search URL
                    searchURL = "https://www.google.com/search?client=firefox-b-1-d&q="
                    search = command.replace(" search for ","")
                    search = search.strip(" ")
                    search = search.replace(" ", "+")
                    search = searchURL+search
                    
                    #Open browser tab with search
                    webbrowser.open_new_tab(search)
                    
                    #Give response
                    sayLine("Here's what I found on Google.")
                    qPhrase = "Anything else you need?"
                #
                #
                ###Image search command    
                elif command.startswith(" show me "):
                    
                    #Build Google search URL
                    searchURL = "https://www.google.com/search?client=firefox-b-1-d&q="
                    search = command.replace(" show me ","")
                    search = search.replace("pictures of", "")
                    search = search.strip(" ")
                    search = search.replace(" ", "+")
                    search = searchURL+"pictures+of+"+search
                    
                    #Open browser tab with search
                    webbrowser.open_new_tab(search)
                    
                    #Give response
                    sayLine("Here's what I found on Google images.")
                    qPhrase = "Anything else I can do for you?"
                #
                #
                ###Timer command
                elif " timer " in command:
                    hours = 0
                    minutes = 0
                    seconds = 0
                    command = command.split(" ")
                    
                    #Get Hours
                    if "hours" in command:
                        hours = command[command.index("hours")-1]
                    elif "hour" in command:
                        hours = command[command.index("hour")-1]
                    
                    #Check for "a" or "an"
                    if hours == "a" or hours == "an":
                        hours = 1
                    
                    #Get Minutes
                    if "minutes" in command:
                        minutes = command[command.index("minutes")-1]
                    elif "minute" in command:
                        minutes = command[command.index("minute")-1]
                    
                    #Check for "a" or "an"
                    if minutes == "a" or minutes == "an":
                        minutes = 1
                            
                    #Get Seconds
                    if "seconds" in command:
                        seconds = command[command.index("seconds")-1]
                    elif "second" in command:
                        seconds = command[command.index("second")-1]
                    
                    #Check for "a" or "an"
                    if seconds == "a" or seconds == "an":
                        seconds = 1
                    
                    if hours != 0 or minutes != 0 or seconds != 0:
                        #Try to convert strings to integers        
                        try:
                            hours = int(hours)
                            minutes = int(minutes)
                            seconds = int(seconds)
                            print(hours, minutes, seconds)
                        
                            line = "Okay, setting a timer for "+str(hours)+" hours "+str(minutes)+" minutes and "+str(seconds)+" seconds! Bear in mind, I won't be able to hear you until the timer has finished."
                            sayLine(line)
                        
                            minutes = minutes+(hours*60)
                            seconds = seconds+(minutes*60)
                            print(seconds)
                        
                            #Set timer
                            timer(seconds)
                            qPhrase = "Do you need anything else now that the timer is done?"
                        
                        #Give error if can't convert strings
                        except:
                            sayLine("""Sorry... I couldn't tell what you wanted me to set the timer for... Unfortunately, I can't understand if you say something like "Set a timer for two and a half hours" yet... You would need to say "Set a timer for 2 hours and 30 minutes".""")      
                    
                    else:
                        sayLine("Sorry... I couldn't tell what you wanted me to set a timer for... Be sure to specify the number of hours, minutes, and seconds you'd like me to set the timer for.")
                #
                #
                ###Next Command
                
                
                
                
                
                        
##############################################################################
                #
                #    
                ###Never mind command
                elif " never mind " in command or " nothing " in command or " no " in command:
                    sayLine("No problem! Call me if you need anything!")
                    stop = True #Set "stop" to true to go back to main loop.
                #
                #
                ###Shut down command
                elif " shut down " in command:
                    sayLine("K, shutting down now. Take care!")
                    stop = True
                    shutdown = True
                #
                #
                ###Contingency to make speaking to assistant sound more normal
                ###(Just in case people say "yes" to being asked if they need something else)
                elif " yes " in command or " yeah " in command:
                    qPhrase = "Okay, what else do you need?"
                #
                #
                ###Command not recognized
                #####END OF COMMANDS#####
                else:
                    sayLine("""
                            Sorry, that wasn't in my list of commands... Maybe Maddy will get to that one soon! 
                            If you'd like me to list commands you can give me, say, list commands, or, help.
                            """)
                    qPhrase = "Need anything else?"
                
                
    
    