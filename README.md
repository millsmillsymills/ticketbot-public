How do we track Walkup interactions for metrics and issue tracking in a Support Department? Maybe leverage the solution to build our brand as a fun, approachable Support Department? We’re going to wire a large arcade-style button to a Rasbperry Pi so the entire process for a User to log a Walkup ticket is a single button push.  

Requirements:

Raspberry Pi (most models are sufficient)

MicroSD Card (8GB or larger)

100mm Massive Arcade Button

3.5mm Speaker

Various jump wires, alligator clips

AWS SES

Set up your Raspberry Pi with your OS of choice. I booted into NOOBS and installed Raspbian Stretch Lite. 

Make sure to update your repositories and check for system upgrades:

sudo apt-get update && sudo apt-get upgrade -y

Preload the following scripts

We will be using the following python scripts:

buttonwatch.py runs on boot, pulses the button’s LED and waits for button press. Launches ticketgen.py and ticketsuccess.py on button press.

ticketgen.py uses Amazon SES to generate and send a canned email to a predetermined address (your ticketing system’s intake address). This is almost entirely copied and pasted from Amazon’s SES documentation. 

ticketsuccess.py is a simple script that plays a random audio file from the ~/ticketbot/audio directory as a confirmation that Ticketbot is functioning. In this simple execution, the launch of this script is not dependant on the successful execution of ticketgen.py. Adding a true check for successful send would be a good feature to add. 

Directory structure:
I've used ~/ticketbot to hold everything needed for Ticketbot for easy compartmentalization. Scripts reside in ~/ticketbot/ and audio files are dropped into ~/ticketbot/audio. 


