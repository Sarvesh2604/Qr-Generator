import qrcode
import image
qr = qrcode.QRCode(
    version = 15,   #15 means the version of the qr code high the number bigger the code image and complex picture
    box_size = 10,  #size of the box of qrcode
    border = 5      #border of the qrcode
)
data = "https://www.instagram.com/sarvesh_sawant26?igsh=MWRxY2s4ZHluamo0aw=="
                    #data of the qrcode
qr.add_data(data)
qr.make(fit = True)
img = qr.make_image(fill = "black", back_color = "white")
img.save("QR.png")