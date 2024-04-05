from hollosmodule import QRcode

qr = QRcode()

qr.make_qr_code("Hello, World!")

qr.save_qr("qr_code.png")

qr.visualize() # show the QR
