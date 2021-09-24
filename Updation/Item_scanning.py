import warnings
warnings.filterwarnings("ignore")
import numpy as np
import cv2
import pyzbar.pyzbar as pyzbar
import csv
import pandas as pd
import time

item = [0,0,0,0,0]

def update_items_local(data):
    global item
    if data == 'FUR-BO-10001798':
        item[0] = item[0]+1
    elif data == 'FUR-CH-10000454':
        item[1]=item[1]+1
    elif data == 'FUR-FU-10001487':
        item[2]=item[2]+1
    elif data == 'FUR-TA-10000577':
        item[3]=item[3]+1
    elif data == 'OFF-LA-10000240':
        item[4]=item[4]+1
    
    print(item)
    print('RECOGNIZED')
    time.sleep(2)
    

def webcam_item():
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
            with open(csv_file, "a", newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(item)
            break

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()

if __name__=='__main__':
    webcam_item()
