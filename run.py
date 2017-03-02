# -*- coding: utf-8 -*-

from serial.tools import list_ports
#import serial
from arserial import ArSerial
import speech_recognition as sr
#import serial
import time

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

#ars = ArSerial(port="COM4")
#ars = ArSerial()

#ars = ArSerial()

#with ArSerial() as ars:
    #ars.baudrate = 9600
    #ars.bytesize = 8 #serial.EIGHTBITS
    #ars.parity = 'N' #serial.PARITY_NONE
    #ars.stopbits = 1 #serial.STOPBITS_ONE
    #ars.timeout = 0.2

    #ars.port = 'COM4'#ports[c].device

    #ser.port = '/dev/ttyUSB0'
    #ars.open()

    #print(ars.wifiArrayRead(25))

    #ars.wifiArrayWrite(34,10)
    #print(ars.wifiArrayWrite(30,50))

    #time.sleep(5)

    #ars.wifiArrayWrite(34,20)
    #ars.wifiArrayWrite(30,50)
    #print(ars.getID())
    #print(ars.publicArrayRead(5))
#print(ars.wifiArrayFullRead())

#ars.string2command("başlat")
#time.sleep(5)
#ars.string2command("durdur")
#time.sleep(5)
#ars.string2command("bahadır")
    #print(ars.publicArrayFullRead())
    #print(ars.wifiArrayPartialRead())
    #print(ars.mercekArrayFullRead())

r = sr.Recognizer()
with sr.Microphone() as source:                # use the default microphone as the audio source

    while True:
        print("dinliyorum...")
        audio = r.listen(source, timeout=1, phrase_time_limit=3)                   # listen for the first phrase and extract it into audio data

        try:
            print("Ses taniniyor...")
            print("You said " + r.recognize_google(audio, language="tr-TR"))  # recognize speech using Google Speech Recognition
            #ars.string2command(r.recognize_google(audio, language="tr-TR"))
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
        except sr.WaitTimeoutError:
            print("Wait timeout error")
        except LookupError:  # speech is unintelligible
            print("Could not understand audio")

    #command1 =
    #command11 =
    #command12 =
    #command2 =
    #command3 =
    #values1 = bytearray([51, 0, 26, 4, 174])
    #values11 = bytearray([51, 0, 30, 50, 153])
    #values12 = bytearray([51, 0, 34, 40, 130])
    #values2 = bytearray([51, 0, 30, 50, 124])
    #values3 = bytearray([53, 0, 0, 0, 202])

    #ser.write(values1)

    #time.sleep(0.4)

    #read_val = ser.read(size=3)

    #print(read_val)

    #ser.write(values11)

    #time.sleep(0.2)

    #read_val = ser.read(size=3)

    #print(read_val)

    #time.sleep(5)

    #ser.write(values12)

    #time.sleep(0.2)

    #read_val = ser.read(size=3)

    #print(read_val)

    #ser.write(values2)

    #time.sleep(0.2)

    #read_val = ser.read(size=2)

    #print(read_val)

    #ser.write(values3)

    #time.sleep(0.2)

    #read_val = ser.read(size=61)
    #print(read_val[43])

    #numb = 0
    #for a in read_val:
    #    print(str(numb)+": "+str(a)+" ")
    #    numb +=1

    #ser.write(values)


#ser.close()