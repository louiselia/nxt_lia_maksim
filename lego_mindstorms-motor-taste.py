# unser motor hat die ganze zeit eine exception ausgerufen die blocked heißt und wir finden auch im internet nix dazu
# sascha hat versucht uns zu helfen
# wir vermuten das es eventuell an den kabeln liegt
import time
import nxt.locator
import nxt.motor
import nxt.sensor
import nxt.sensor.generic

# dies dient dazu das der brick erkannt wird
with nxt.locator.find() as b:

# hier weden die aktoren und sensoren erkant und ihnen variablen zugewiesen
    ultra_sonic = b.get_sensor(nxt.sensor.Port.S4, nxt.sensor.generic.Ultrasonic)
    touch_sensor = b.get_sensor(nxt.sensor.Port.S1, nxt.sensor.generic.Touch)
    motor = b.get_motor(nxt.motor.Port.A)

# hier wird alles abgespielt
    while True:
        # erkennt ob der taster gedrückt wird oder nicht
        state = touch_sensor.get_sample()

        # drehrt den motor stückweise um 180° und scannt mit jedem tick dies wird dann in eine liste eingefügt
        if state == True:
        
            for y in range(10):
                
                for i in range(1):
                    motor.turn(30, 20)
                    distance_cm = ultra_sonic.get_sample()
                    print("Weg 1:", distance_cm)
                    time.sleep(0.5)
                for x in range(1):
                    motor.turn(-30, 15)
                    distance_cm = ultra_sonic.get_sample()
                    print("Weg 2:", distance_cm)
                    time.sleep(0.5)

        # Nun sollte das programm geschrieben werden das man benutzt um den durchschnitt auszurechnen von l1 und l2 dieser sollte dann geplotet werden mit pyplot
        # das hat aber keinen sinn da der motor nicht anständig funktioniert 
        durchschnitt = []
        
        
