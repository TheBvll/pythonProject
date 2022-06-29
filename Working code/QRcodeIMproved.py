import qrcode
data = "https://ibb.co/w6Nc0pQ"

QRcodefile = "FuckSerbianNiggers.png"
qrObject = qrcode.QRCode()

qrObject.add_data(data)
qrObject.make()

image = qrObject.make_image(fill_color="green")
image.save(QRcodefile)