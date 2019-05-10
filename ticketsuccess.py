import os,random
#import gpiozero
import subprocess
#from gpiozero import PWMLED
#red = PWMLED(18)

def randomp3():
    randomfile = random.choice(os.listdir("/home/pi/ticketbot/audio/"))
    file = '/home/pi/ticketbot/audio/' + randomfile
    subprocess.Popen(['mpg123', '-q', file]).wait()
#    red.blink()
    
    
randomp3()
import sys
sys.exit()
