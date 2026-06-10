import qrcode

url = input("Enter a URL: ")
file_path = "C:\\Users\\Aarush\\OneDrive\\Desktop\\GitHubQRcode.png"

qr = qrcode.QRCode()
qr.add_data(url)

img = qr.make_image()
img.save(file_path)

print("QR Code was generated!")