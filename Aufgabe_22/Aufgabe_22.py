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

        l1 = []
        l2 = []

        # drehrt den motor stückweise um 180° und scannt mit jedem tick dies wird dann in eine liste eingefügt
        if state == True:
            for i in range(20):
                motor.turn(5, 9)
                data1 = ultra_sonic.sampels()
                l1.append(data1)
            for x in range(20):
                motor.turn(-5, 9)
                data2 = ultra_sonic.sampels()
                l2.append(data2)
            break

        # Nun sollte das programm geschrieben werden das man benutzt um den durchschnitt auszurechnen von l1 und l2 dieser sollte dann geplotet werden mit pyplot(Halb polar diagramm)
        # das hat aber keinen sinn da der motor nicht anständig funktioniert 
        durchschnitt = []