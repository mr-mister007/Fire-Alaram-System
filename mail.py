from time import sleep
import board
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO_PIN=12
GPIO.setmode(GPIO.BCM) 
GPIO.setup(12, GPIO.OUT)
from imapclient import IMAPClient
from digitalio import DigitalInOut, Direction
HOSTNAME = 'imap.gmail.com'
MAILBOX = 'Inbox'
MAIL_CHECK_FREQ = 0.5     
 
USERNAME ='*****@gmail.com'
PASSWORD ='*****' 
NEWMAIL_OFFSET = 0         
 
green_led = DigitalInOut(board.D18)
green_led.direction = Direction.OUTPUT
def mail_check():
    server = IMAPClient(HOSTNAME, use_uid=True, ssl=True)
    server.login(USERNAME, PASSWORD)
 
    unseen = server.folder_status(MAILBOX, ['UNSEEN'])
 
   
    newmail_count = (unseen[b'UNSEEN'])
    print('%d unseen messages' % newmail_count)
 
    if newmail_count > NEWMAIL_OFFSET:
        green_led.value = True
        
    else:
        green_led.value = False
 
    sleep(MAIL_CHECK_FREQ)
 
while True:
    mail_check()