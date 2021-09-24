import pyqrcode
big_code = pyqrcode.create('FUR-BO-1000179')
big_code.png('CG-12520.png', scale=6, module_color=[0, 0, 0, 128], background=[0xff, 0xff, 0xcd])
