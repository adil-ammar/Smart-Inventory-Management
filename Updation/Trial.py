import numpy as np
import cv2
import pyzbar.pyzbar as pyzbar
import csv
import pandas as pd
import time
import tkinter as tk

item = [0,0,0,0,0,0,0,0,0,0]

def update_items_local(data):
    global item
    if data == 'Item:1':
        item[0] = item[0]+1
    elif data == 'Item:2':
        item[1]=item[1]+1
    elif data == 'Item:3':
        item[2]=item[2]+1
    elif data == 'Item:4':
        item[3]=item[3]+1
    elif data == 'Item:5':
        item[4]=item[4]+1
    elif data == 'Item:6':
        item[5]=item[5]+1
    elif data == 'Item:7':
        item[6]=item[6]+1
    elif data == 'Item:8':
        item[7]=item[7]+1
    elif data == 'Item:9':
        item[8]=item[8]+1
    elif data == 'Item:10':
        item[9]=item[9]+1
    
    print(item)
    print('RECOGNIZED')
    time.sleep(3)
    

def webcam():
    cap = cv2.VideoCapture(0)
    ret =True
    while(ret):
        # Capture frame-by-frame
        ret, frame = cap.read()

        #Capture the barcode
        decodedObjects = pyzbar.decode(frame)
        
        if len(decodedObjects)!=0:
            for decodedObject in decodedObjects:
                hull = decodedObject.polygon
            n = len(hull)   
            for j in range(0,n):
                cv2.line(frame, hull[j], hull[ (j+1) % n], (0,0,255), 3)
            print((decodedObject.data).decode())
            data_decoded = decodedObject.data.decode()
            update_items_local(data_decoded)
            
        # Display the resulting frame
        cv2.imshow('frame',frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            csv_file = 'Items.csv'
            with open(csv_file, "a") as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(item)
            break

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()

if __name__=='__main__':
    webcam()
