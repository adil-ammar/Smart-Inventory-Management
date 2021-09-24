import warnings
warnings.filterwarnings("ignore")

import tkinter as tk
from member_scanning import webcam
from Item_scanning import webcam_item

def check_membership():
    webcam()

def item_scan():
    webcam_item()

root = tk.Tk()
root.title('Auto Shopper')
frame = tk.Frame(bg = 'black', height=400, width = 200)
frame.pack()

quit_button = tk.Button(frame, 
                   text="QUIT", 
                   fg="red",
                   command=exit)
quit_button.pack(side=tk.LEFT)

mem_check = tk.Button(frame,
                   text="Membership",
                   command=check_membership)
mem_check.pack(side=tk.LEFT)

item_scan = tk.Button(frame,
                   text="Scan Items",
                   command=item_scan)
item_scan.pack(side=tk.LEFT)

root.mainloop()
