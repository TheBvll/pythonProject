import cv2 as cv

im = cv.imread("BasedTed.png")
det = cv.QRCodeDetector()

retval, points, straight_qrcode = det.detectAndDecode(im)

print(retval, points, straight_qrcode)