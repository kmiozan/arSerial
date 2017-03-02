#!/usr/bin/env python3

# NOTE: this example requires PyAudio because it uses the Microphone class

import speech_recognition as sr

# this is called from the background thread
def callback(recognizer, audio):
    # received audio data, now we'll recognize it using Google Speech Recognition
    try:
        print("Recognizing")
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`
        print("Google Speech Recognition thinks you said " + recognizer.recognize_google(audio, language="tr-TR"))
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

r = sr.Recognizer()
m = sr.Microphone()
with m as source:
    print("Calibrating")
    #r.adjust_for_ambient_noise(source) # we only need to calibrate once, before we start listening
    print("Listening")
# start listening in the background (note that we don't have to do this inside a `with` statement)
stop_listening = r.listen_in_background(m, callback, phrase_time_limit=5)
# `stop_listening` is now a function that, when called, stops background listening

# do some other computation for 5 seconds, then stop listening and keep doing other computations
import time
for _ in range(50): time.sleep(0.1) # we're still listening even though the main thread is doing other things
stop_listening() # calling this function requests that the background listener stop listening
while True: time.sleep(0.1)

def callback(recognizer, audio):
    # received audio data, now we'll recognize it using Google Speech Recognition
    try:
        print("Recognizing")
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`
        print("Google Speech Recognition thinks you said " + recognizer.recognize_google(audio, key="AIzaSyBv_c6hXAIFhKBTxfYbWine04aUkRvSOXA", language="tr-TR"))

        #ars.string2command(recognizer.recognize_google(audio, language="tr-TR"))
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

r = sr.Recognizer()
m = sr.Microphone()
with m as source:
    print("Calibrating")
    #r.adjust_for_ambient_noise(source) # we only need to calibrate once, before we start listening
    print("Listening")
# start listening in the background (note that we don't have to do this inside a `with` statement)
stop_listening = r.listen_in_background(m, callback, phrase_time_limit=4)
# `stop_listening` is now a function that, when called, stops background listening

# do some other computation for 5 seconds, then stop listening and keep doing other computations
#import time
for _ in range(50): time.sleep(0.1) # we're still listening even though the main thread is doing other things
stop_listening() # calling this function requests that the background listener stop listening
while True: time.sleep(0.1)


# !/usr/bin/env python3
# Requires PyAudio and PySpeech.

#import speech_recognition as sr

# Record Audio
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source,timeout=1,phrase_time_limit=4)

# Speech recognition using Google Speech Recognition
try:
    print("Anliyor")
    # for testing purposes, we're just using the default API key
    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
    # instead of `r.recognize_google(audio)`
    #print("You said: " + r.recognize_google(audio, language="tr-TR"))
    ars.string2command(r.recognize_google(audio, language="tr-TR"))
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))