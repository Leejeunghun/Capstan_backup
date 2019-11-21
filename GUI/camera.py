#!/usr/bin/env python
# -*- coding:utf-8 -*-
from picamera import PiCamera#camera 
from time import sleep
from datetime import datetime  #date
import smtplib    #mail
from email.mime.text import MIMEText


now = datetime.now()
print(now)
#camera
camera = PiCamera()
camera.start_preview()
camera.capture('camera/{}.jpg'.format(now))
camera.stop_preview()

#mail 
smtp = smtplib.SMTP('smtp.gmail.com', 587)
smtp.ehlo()      # say Hello
smtp.starttls() 
smtp.login('jeonghun695@gmail.com', 'projectnum1!')
msg = MIMEText("{}".format(now))
msg['Subject'] = '냉장고 사용'
msg['To'] = 'jeonghun695@gmail.com'
filename='{}.jpg'.format(now)
smtp.sendmail('jeonghun695@gmail.com', 'jeonghun695@gmail.com', msg.as_string())
smtp.quit()
