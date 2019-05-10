from gpiozero import Button,PWMLED
from signal import pause
import subprocess
import time
red = PWMLED(18)
red.pulse()

def popticket():
    subprocess.run(["python3", "/home/pi/ticketbot/ticketsuccess.py"])
    subprocess.run(["python3", "/home/pi/ticketbot/ticketgen.py"])
button = Button(7)

button.when_pressed = popticket
red.pulse()
pause()
