import qrtools
qr = qrtools.QR()
k=qr.decode("skb.png")
print (qr.data)
