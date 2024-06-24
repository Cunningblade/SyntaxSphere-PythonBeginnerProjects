import qrcode

def generate_qr(data):
    qr = qrcode.QRCode()
    qr.add_data(data)
    qr.make()

    image = qr.make_image(fill_color="white",back_color="black")
    image.show()
    

data = input("Generate QR code for : ")
generate_qr(data)