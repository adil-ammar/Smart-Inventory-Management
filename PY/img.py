import cv2
import numpy as np

def main():
    im = cv2.imread('qrcode.png',0)
    cv2.imshow("uhihui",im)
    cv2.waitKey(0)
    print(im)

if __name__=='__main__':
    main()
    print('return')
