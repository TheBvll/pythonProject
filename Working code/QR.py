import qrcode
data = "https://www.4chan.org"
QRcodefile = "He_actually_posted_this_shit.png"

QRimage = qrcode.make(data)
QRimage.save(QRcodefile)