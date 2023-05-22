import qrcode as qr
from pyzbar.pyzbar import decode
from PIL import Image

# img=qr.make("https://wa.me/+919004713782")
# img.save("whatsapp.png")

# to decode any QR code
text=decode(Image.open('ss.png'))
# print(text[0].data.decode('utf-8'))
print(text)