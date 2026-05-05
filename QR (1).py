#qrcode generator
# import qrcode
# img=qrcode.make(input("enter a URL : "))
# img.save("qrcode.png")
# print("saved successfully")

#qrcode with more styling
import qrcode
from PIL import Image, ImageDraw
qr = qrcode.QRCode(box_size=20, border=5)
a="Hello World"
qr.add_data(a)
qr.make(fit=True)
img = qr.make_image(fill_color="white", back_color="black")
img.save("qrcode.png")
print("saved successfully")