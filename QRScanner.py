import qrcode

qr = qrcode.QRCode(version = 1,
                   error_correction = qrcode.constants.ERROR_CODE_L,
                   box_size = 7,
                   border = 2)

qr.add_data("aqui vá la direccion web del código qr")
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save("nombre_de_la_imagen.png")