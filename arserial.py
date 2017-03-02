# -*- coding: utf-8 -*-

import serial
import time

class ArSerial(serial.Serial):

    def __init__(self, baudrate = 9600, bytesize = 8, parity = 'N', stopbits = 1, timeout = 0.2, port='/dev/ttyUSB0', *args, **kwargs):
        print("Initialized")
        super(ArSerial, self).__init__(baudrate = baudrate, bytesize = bytesize, parity = parity, stopbits = stopbits, timeout = timeout, port=port, *args, **kwargs)
        self.baudrate = baudrate
        self.bytesize = bytesize
        self.parity = parity
        self.stopbits = stopbits
        self.timeout = timeout
        self.port = port
        #self.port = '/dev/ttyUSB0'
        self.stringDict = {"başlat": 34030, "bekle": 34040, "dur": 34040, "makineyi başlat": 34030, "veryansın": 34030,
                           "durdur": 34040, "programı durdur": 34040, "açıl": 34010, "programı başlat": 34030, "kapan":34020,
                           "bitir":34040}

    def checkSum(self, command, byte=0, value=0):
        cS = 255-(command+byte+value)%255
        return cS

    def createData(self, command, byte=0, value=0):
        data = bytearray([command, 0, byte, value, self.checkSum(command, byte, value)])
        return data

    def commandSequence(self, data, sleepTime=0.2, readSize=2):

        #for a in data:
        #    print("C"+str(a))
        self.write(data)
        time.sleep(sleepTime)
        answer = (self.read(readSize)).hex()
        #print(answer[0:2])
        #print(answer)
        return answer

    def wifiArrayRead(self, byte):
        """Function for 50 Wifi Array Read command for Arcelik HomeWhiz Appliances"""

        data = self.createData(command=50, byte=byte)
        answer = self.commandSequence(data)
        return answer

    def getID(self):

        data = self.createData(command=1)
        answer = self.commandSequence(data)
        return answer

    def publicArrayRead(self, byte):

        data = self.createData(command=2, byte=byte)
        answer = self.commandSequence(data)
        return answer

    def wifiArrayWrite(self, byte, value):
        """Function for 51 Wifi Array Write command for Arcelik HomeWhiz Appliances"""

        data = self.createData(command=51, byte=byte, value=value)
        answer = self.commandSequence(data)
        return answer

    def publicArrayWrite(self, byte, value):

        data = self.createData(command=3, byte=byte, value=value)
        answer = self.commandSequence(data)
        return answer

    def wifiArrayPartialRead(self):
        """Function for 52 Wifi Array Partially Write command for Arcelik HomeWhiz Appliances"""

        data = self.createData(command=52)
        # 26'dan sonrasini okuyor
        readSize = int(self.wifiArrayRead(25)[0:2],16)-26
        answer = self.commandSequence(data=data, readSize=readSize)
        return answer

    def wifiArrayFullRead(self):
        """Function for 53 Wifi Array Full Read command for Arcelik HomeWhiz Appliances"""

        readSize = int(self.wifiArrayRead(25)[0:2],16)
        data = self.createData(command=53)
        answer = self.commandSequence(data=data, readSize=readSize)
        return answer

    def publicArrayFullRead(self):

        #readSize = int(self.wifiArrayRead(25)[0:2],16)
        readSize = 100 # boyutu nasil bilebiliriz?
        data = self.createData(command=4)
        answer = self.commandSequence(data=data, readSize=readSize)
        return answer

    def mercekArrayFullRead(self):
        """Function for 54 Mercek Array Full Read command for Arcelik HomeWhiz Appliances"""

        readSize = int(self.wifiArrayRead(24)[0:2],16)
        data = self.createData(command=54)
        answer = self.commandSequence(data=data, readSize=readSize)
        return answer

    def string2command(self,string):

        if string is not None:
            if string in self.stringDict:
                if self.stringDict[string] == 34030:
                    self.wifiArrayWrite(34,30)
                    self.wifiArrayWrite(30,50)
                    print("start")
                elif self.stringDict[string] == 34040:
                    self.wifiArrayWrite(34, 40)
                    self.wifiArrayWrite(30, 50)
                    print("stop")
                elif self.stringDict[string] == 34010:
                    self.wifiArrayWrite(34, 10)
                    self.wifiArrayWrite(30, 50)
                    print("open")
                elif self.stringDict[string] == 34020:
                    self.wifiArrayWrite(34, 20)
                    self.wifiArrayWrite(30, 50)
                    print("close")
                else:
                    print("Could not recognize")
            else:
                print("Not a word we know")
        else:
            print("Not even a string")
