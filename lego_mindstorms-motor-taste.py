import time
import nxt.locator
import nxt.motor
import nxt.sensor
import nxt.sensor.generic

with nxt.locator.find() as b:
    # Get the sensor connected to port 1, not a digital sensor, must give the sensor
    # class.
    mysensor = b.get_sensor(nxt.sensor.Port.S1, nxt.sensor.generic.Touch)
    mymotor = b.get_motor(nxt.motor.Port.A)
    # Read the sensor in a loop (until interrupted).
    print("Use Ctrl-C to interrupt")
    while True:
        try:
            value = mysensor.get_sample()
            print(value)
            if value == True:
                mymotor.turn(5, 10)
                mymotor.turn(-5, 10)
            time.sleep(0.5)

        except:
            pass
