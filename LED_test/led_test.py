#!usr/bin/env/ python`
## enciende.py
#Importamos la libreria y le cambiamos el nombre a GPIO
GPIO로 RPi.GPIO 가져오기
#우리는 우리가 하고자 하는 번호 매기기 시스템 설정, 
#이 경우 BCM 시스템
GPIO.setmode(GPIO입니다. BCM)
#GPIO 핀 구성 4 출력으로
GPIO.setup(4, GPIO입니다. 밖으로)
#우리는 led 설정
GPIO.output(4, GPIO입니다. 높은)
