#!/usr/bin/env python
# -*- coding:utf-8 -*-
from picamera import PiCamera#camera 
from time import sleep
from datetime import datetime  #date
import smtplib    #mail
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import mimetypes
from email.mime.base import MIMEBase

now = datetime.now()
print(now)
#camera
camera = PiCamera()
camera.start_preview()
camera.capture('{}.jpg'.format(now))
camera.stop_preview()

#mail 
smtp = smtplib.SMTP('smtp.gmail.com', 587)
smtp.ehlo()      # say Hello
smtp.starttls() 
smtp.login('jeonghun695@gmail.com', 'projectnum1!')
msg=MIMEBase("multipart","mixed")
msg['subject']= "냉장고 사용 {}".format(now)
imageFD=open("{}.jpg".format(now),'rb')
ImagePart=MIMEImage(imageFD.read())
imageFD.close()
msg.attach(ImagePart)
# 헤더에 첨부 파일에 대한 정보 추가
msg.add_header('Content-Disposition', 'attachment', filename='test')
smtp.sendmail('jeonghun695@gmail.com', 'jeonghun695@gmail.com', msg.as_string())
smtp.quit()
