# -*- coding: utf-8 -*-

from serial.tools import list_ports
import serial
import time
import speech_recognition as sr

#ports = list_ports.comports()

#print("\nSelect the comport to be used:\n")

#numb = 0
#for p in ports:
#    print(str(numb)+ " : " + str(p))
#    numb+=1

#c = input('\n')
#c = int(c)

#print(ports[c].device + "\n")

# 9600 8 None 1 None

#ser = serial.Serial(ports[c].device, 9600)

with serial.Serial() as ser:
    ser.baudrate = 9600
    ser.bytesize = serial.EIGHTBITS
    ser.parity = serial.PARITY_NONE
    ser.stopbits = serial.STOPBITS_ONE
    ser.timeout = 0.2

    #ser.port = 'COM7'#ports[c].device
    ser.port = '/dev/ttyUSB0'
    ser.open()

    homeWhiz = [51, 0, 26, 4, 174]
    Open = [51, 0, 34, 10, 160]
    close = [51, 0, 34, 20, 150]
    start = [51, 0, 34, 30, 140]
    control = [51, 0, 30, 50, 124]
    stop = [51, 0, 34, 40, 130]


    homeWhizValue = bytearray(homeWhiz)
    startValue = bytearray(start)
    openValue = bytearray(Open)
    closeValue = bytearray(close)
    controlValue = bytearray(control)
    stopValue = bytearray(stop)

    # homeWhiz ayar
    ser.write(homeWhizValue)
    time.sleep(0.2)
    read_val = ser.read(size=3)

    r = sr.Recognizer()
    with sr.Microphone() as source:  # use the default microphone as the audio source

        while True:

            # r.adjust_for_ambient_noise(source,duration=2)
            print("dinliyorum...")
            audio = r.listen(source, timeout=1, phrase_time_limit=3)  # listen for the first phrase and extract it into audio data
            x = ''
            try:
                print("Ses tanimlaniyor...")
                #print("Soylenen: " + r.recognize_google(audio,language="tr-TR"))  # recognize speech using Google Speech Recognition
                x = r.recognize_google(audio,language="tr-TR")
                print(x)
            except sr.UnknownValueError:
                print("Google Speech Recognition could not understand audio")
            except sr.RequestError as e:
                print("Could not request results from Google Speech Recognition service; {0}".format(e))
            except sr.WaitTimeoutError:
                print("Wait timeout error")
            except LookupError:  # speech is unintelligible
                print("Could not understand audio")





            if x == u"başlat":
                ser.write(startValue)
                time.sleep(0.2)
                read_val = ser.read(size=3)
                ser.write(controlValue)
                time.sleep(5)
            elif x == "dur":
                ser.write(stopValue)
                time.sleep(0.2)
                read_val = ser.read(size=3)
                ser.write(controlValue)
                time.sleep(5)
            elif x == u"açıl":
                ser.write(openValue)
                time.sleep(0.2)
                read_val = ser.read(size=3)
                ser.write(controlValue)
                time.sleep(5)
            elif x == "kapan":
                ser.write(closeValue)
                time.sleep(5)
                read_val = ser.read(size=3)
                ser.write(controlValue)
                time.sleep(0.2)


    #ser.write(values)


#ser.close()