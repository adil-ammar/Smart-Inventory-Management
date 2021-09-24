import pyzbar.pyzbar as pyzbar
import numpy as np
import cv2

def decode(im) :
    # Find barcodes and QR codes
    decodedObjects = pyzbar.decode(im)
    print(decodedObjects)
 
    # Print results
    for obj in decodedObjects:
        print(obj)
        print('Type : ', obj.type)
        print('Data : ', obj.data,'\n')
     
    return decodedObjects

# Display barcode and QR code location  
def display(im, decodedObjects):
    # Loop over all decoded objects
    for decodedObject in decodedObjects:
        points = decodedObject.polygon
        print(points)

    hull=points
    # Number of points in the convex hull
    n = len(hull)
    print("The length of hull:",n)
 
    # Draw the convext hull
    for j in range(0,n):
        cv2.line(im, hull[j], hull[ (j+1) % n], (255,0,0), 3)
 
    # Display results 
    cv2.imshow("Results", im);
    cv2.waitKey(0);

# Main 
if __name__ == '__main__':
 
    # Read image
    im = cv2.imread('qrcode_9.png')
    #gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
 
    decodedObjects = decode(im)
    display(im, decodedObjects)
