import warnings
warnings.filterwarnings("ignore")
import numpy as np
import cv2
import pyzbar.pyzbar as pyzbar
import csv
import pandas as pd

def update_sales_members(data):
    id_num = data
    df_ref = pd.read_csv('main_customer_database.csv')
    new = df_ref[df_ref['Customer ID']==id_num].reset_index(drop = True)
    csv_file = 'Sales.csv'
    with open(csv_file, "a", newline='') as csvfile:
        writer = csv.writer(csvfile)
        now = pd.datetime.now()
        f = list(new.iloc[0])
        f.append(now)
        writer.writerow(f)

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
            cap.release()
            cv2.destroyAllWindows()
            update_sales_members(data_decoded)
            break
            
        # Display the resulting frame
        cv2.imshow('frame',frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()

if __name__=='__main__':
    webcam()
