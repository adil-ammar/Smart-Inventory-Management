import pyqrcode
big_code = pyqrcode.create('12000221')
big_code.png('skb.png', scale=6, module_color=[0, 0, 0, 128], background=[0xff, 0xff, 0xcd])
