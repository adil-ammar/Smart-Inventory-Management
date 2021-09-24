import pyzbar
import qrtools
from pyzbar.pyzbar import decode
from PIL import Image
dat = decode(Image.open('code.png'))[0]
print(dat[0].decode())
