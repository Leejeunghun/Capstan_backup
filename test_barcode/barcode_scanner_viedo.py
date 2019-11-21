# USAGE
# python barcode_scanner_video.py

# import the necessary packages
from imutils.video import VideoStream
from pyzbar import pyzbar
#import argparse
import datetime
import imutils
import time
import cv2
import pymysql
import sys
import subprocess

# initialize the video stream and allow the camera sensor to warm up
print("[INFO] starting video stream...")
# vs = VideoStream(src=0).start()
vs = VideoStream(usePiCamera=True).start()
time.sleep(2.0)

# open the output CSV file for writing and initialize the set of
# barcodes found thus far
csv = open("test.csv", "w")
found = set()
key_1=0
# loop over the frames from the video stream
while True:
	# grab the frame from the threaded video stream and resize it to
	# have a maximum width of 400 pixels
	frame = vs.read()
	frame = imutils.resize(frame, width=400)

	# find the barcodes in the frame and decode each of the barcodes
	barcodes = pyzbar.decode(frame)

	# loop over the detected barcodes
	for barcode in barcodes:
		# extract the bounding box location of the barcode and draw
		# the bounding box surrounding the barcode on the image
		(x, y, w, h) = barcode.rect
		cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

		# the barcode data is a bytes object so if we want to draw it
		# on our output image we need to convert it to a string first
		barcodeData = barcode.data.decode("utf-8")
		barcodeType = barcode.type


                conn=pymysql.connect(host='localhost',user='root',password='qwer123',db='esebird',charset='utf8')
                # cursur
                curs =conn.cursor()
                sql ="select * from member"
                curs.execute(sql)
                rows=curs.fetchall()
                for row in rows:
                    if row[5] =='{}'.format(sys.argv[1]):
                        conn_item=pymysql.connect(host='localhost',user='root',password='qwer123',db='esebird',charset='utf8')
                        curs_item=conn_item.cursor()
                        sql_item ="insert into item(User,Door_status,time) values(%s,%s,%s)"
                        curs_item.execute(sql_item,(row[1],barcodeData,datetime.datetime.now()))
                        conn_item.commit()
                        conn_item.close()
                        key_1=1
                conn.close()
                
                
		# draw the barcode data and barcode type on the image
		text = "{} ({})".format(barcodeData, barcodeType)
		cv2.putText(frame, text, (x, y - 10),
			cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

		# if the barcode text is currently not in our CSV file, write
		# the timestamp + barcode to disk and update the set
		if barcodeData not in found:
			csv.write("{},{}\n".format(datetime.datetime.now(),
				barcodeData))
			csv.flush()
			found.add(barcodeData)

	# show the output frame
	
        cv2.imshow("Barcode Scanner", frame)
	key = cv2.waitKey(1) & 0xFF
        
	# if the `q` key was pressed, break from the loop
        if key_1 == 1:
            break
	if key == ord("q"):
		break
      

# close the output CSV file do a bit of cleanup
print("[INFO] cleaning up...")
csv.close()
cv2.destroyAllWindows()
vs.stop()
