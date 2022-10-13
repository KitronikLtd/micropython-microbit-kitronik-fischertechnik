# microbit-module: KitronikInterfaceForFischertechnik@1.0.0
# Copyright (c) Kitronik Ltd 2022. 
#
# The MIT License (MIT)
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
from microbit import *
import math

class KitronikInterfaceForFischertechnik:
    
    def motorOn(self, motor, direction, speed):
        
        if speed > 100:
            speed = 100
        elif speed < 0:
            speed = 0
        speed = speed * 10
        if motor == "Motor1":
            if direction == "forward":
                pin8.write_analog(speed)
                pin12.write_digital(0)
            elif direction == "reverse":
                pin12.write_analog(speed)
                pin8.write_digital(0)
        elif motor == "Motor2":
            if direction == "forward":
                pin16.write_analog(speed)
                pin2.write_digital(0)
            elif direction == "reverse":
                pin2.write_analog(speed)
                pin16.write_digital(0)

    def motorOff(self, motor):
        if motor == "Motor1":
            pin12.write_digital(0)
            pin8.write_digital(0)
        elif motor == "Motor2":
            pin2.write_digital(0)
            pin16.write_digital(0)
    
    def led(self, pinSelection, illumination):
        if pinSelection == "P0":
            if illumination == "on":
                pin0.write_digital(1)
            elif illumination == "off":
                pin0.write_digital(0)
        elif pinSelection == "P1":
            if illumination == "on":
                pin1.write_digital(1)
            elif illumination == "off":
                pin1.write_digital(0)
    
    def phototransistor(self, pinSelection):
        if pinSelection == "P0":
            reading = pin0.read_analog()
        elif pinSelection == "P1":
            reading = pin1.read_analog()
        return reading
            
    def ntc(self, pinSelection):
        if pinSelection == "P0":
            reading = pin0.read_analog()
        elif pinSelection == "P1":
            reading = pin1.read_analog()
        convertReading = reading * (3.3/1024)       # convert reading to voltage reading x (supply divide ADC resoluction)
        ntcResistor = 3.3/((3.3-convertReading)/4700)  # calculate resistance
        temperatureC = (3880/math.log(ntcResistor/0.13)) - 273.15
        return temperatureC
        
kiff = KitronikInterfaceForFischertechnik

while True:
    kiff.motorOn(kiff, "Motor1", "forward", 100)
    sleep(2000)
    kiff.motorOff(kiff, "Motor1")
    sleep(2000)
    display.show(kiff.ntc(kiff,"P0"))
