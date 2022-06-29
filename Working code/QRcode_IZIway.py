import qrcode

qr = qrcode.QRCode(
    version=2,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=25,
    border=6,
)

qr.add_data("https://www.washingtonpost.com/wp-srv/national/longterm/unabomber/manifesto.text.htm")
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white").convert("RGB")
img.save("BasedTed.png")