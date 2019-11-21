import smtplib
from email.mime.text import MIMEText
 
smtp = smtplib.SMTP('smtp.gmail.com', 587)
smtp.ehlo()      # say Hello
smtp.starttls()  # TLS 사용시 필요
smtp.login('jeonghun695@gmail.com','projectnum1!')
 
msg = MIMEText('본문 테스트 메시지')
msg['Subject'] = '테스트'
msg['To'] = 'jeonghun695@gmail.com'
smtp.sendmail('jeonghun695@gmail.com', 'jeonghun695@gmail.com', msg.as_string())
 
smtp.quit()
