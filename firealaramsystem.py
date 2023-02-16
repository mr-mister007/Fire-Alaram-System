from twilio.rest import Client
from pushbullet import Pushbullet
import sys
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.IN) 
import smtplib
pb = Pushbullet("replace with your private token")

def send_email1(user, pwd, recipient, subject, body):
    gmail_user = '*****@gmail.com'
    gmail_pwd = '*******'
    FROM = user
    TO = 'firealertpi@gmail.com'
    SUBJECT = 'Fire'
    TEXT = body

    message = """\From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
    try:
        print "trying to send email"
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(gmail_user, gmail_pwd)
        server.sendmail(FROM, TO, message)
        server.close()
        print 'successfully sent the mail'
	
    except:
        print "failed to send mail"

def send1():
    	send_email1('********@gmail.com', '******', 'firealertpi@gmail.com', 'Fire!!!', 'Building On Fire!!!')
    	
#twilio_auth_token
	account_sid = '*****'
	auth_token = '*****'
	client = Client(account_sid, auth_token)

	call = client.calls.create(
                        	url='http://demo.twilio.com/docs/voice.xml',
                        	to='your number',
                        	from_='+12052369265'
                    	)

	
while 1:
    if not GPIO.input(11):
	send1()   
        sys.exit()
