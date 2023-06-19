#mit hilfe von merlin und florian
import time
import nxt.locator
import nxt.motcont
import nxt.motor
import nxt.sensor
import nxt.sensor.generic
import numpy as np
import matplotlib.pyplot as plt
import nxt.sensor.hitechnic


with nxt.locator.find() as b:
    #alle motoren und sensoren einlesen
    motor_left = b.get_motor(nxt.motor.Port.A)
    motor_right = b.get_motor(nxt.motor.Port.B)
    motor_sensor = b.get_motor(nxt.motor.Port.C)
    color_sensor = b.get_sensor(nxt.sensor.Port.S1, nxt.sensor.hitechnic.Colorv2)
    motors = nxt.motor.SynchronizedMotors(motor_left, motor_right, 0)
   
    #farben festelgen und bennenen
    while True:
        green = color_sensor.get_active_color().green
        red = color_sensor.get_active_color().red
        blue = color_sensor.get_active_color().blue
        white = color_sensor.get_active_color().white
        motors = nxt.motor.SynchronizedMotors(motor_left, motor_right, 0)
        
        #aktuelle farben ausgeben
        print(f'green: {green}, red: {red}, blue: {blue}, white: {white}   1')
        
        
        if green < 0 and red < 225 and blue < 0:
            motors = nxt.motor.SynchronizedMotors(motor_left, motor_right, 0)
            motors.run(-70) 
            time.sleep(0.8)
            
        else:
            motors.brake()
            x = 1
            
            while True:
                if green < 0 and red < 225 and blue < 0:
                    print("die linie wurde gefunden!")
                    break
                
                motors = nxt.motor.SynchronizedMotors(motor_left, motor_right, 127)
                
                for i in range(x):
                    motors.run(-70)
                    time.sleep(0.1)
                    green = color_sensor.get_active_color().green
                    red = color_sensor.get_active_color().red
                    blue = color_sensor.get_active_color().blue
                    white = color_sensor.get_active_color().white
    
                    if green < 20 and red < 20 and blue < 20:
                        print("die linie wurde gefunden!")
                        break
                    
                motors = nxt.motor.SynchronizedMotors(motor_right, motor_left, 127)
                
                x *= 2
                for i in range(x):
                    motors.run(-70)
                    time.sleep(0.1)
                    green = color_sensor.get_active_color().green
                    red = color_sensor.get_active_color().red
                    blue = color_sensor.get_active_color().blue
                    white = color_sensor.get_active_color().white
        
                    if green < 0 and red < 225 and blue < 0:
                        print("die linie wurde gefunden!")
                        break
                    
                x += 1
                print(f'green: {green}, red: {red}, blue: {blue}, white: {white}  2')  