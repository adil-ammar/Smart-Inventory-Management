# -*- coding: utf-8 -*-
"""
Created on Sat Aug 18 05:06:34 2018

@author: USER
"""

import cv2
import matplotlib.pyplot as plt

def main():
    windowName = 'Live_Video_Feed'
    cv2.namedWindow(windowName)
    
    cap=cv2.VideoCapture(0)
    print("Width:",cap.get(3))
    print("Height:",cap.get(4))
    
    cap.set(3,1600)
    cap.set(4,900)
    print("Width:",cap.get(3))
    print("Height:",cap.get(4))
    
    if cap.isOpened():
        ret, frame = cap.read()
        print(ret)
    else:
        ret = False
        
    while ret:
        ret, frame = cap.read()
        output = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow(windowName, output)
        
        if cv2.waitKey(1) == 27:
            break
            
    cv2.destroyWindow(windowName)
    cap.release()
        
if __name__=='__main__':
    main()