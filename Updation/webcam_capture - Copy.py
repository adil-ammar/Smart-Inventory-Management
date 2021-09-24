import numpy as np
import cv2
import pyzbar.pyzbar as pyzbar
import csv

def update(data):
    new_data = data.decode()
    list_data = new_data.split()
    csv_file = 'SIMOS - Copy.csv'
    with open(csv_file, "a", newline = '') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(list_data)

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
        cap.release()
        cv2.destroyAllWindows()
        update(decodedObject.data)
        break
        
    # Display the resulting frame
    cv2.imshow('frame',frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
