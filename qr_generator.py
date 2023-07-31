import qrcode

def gerador_qr(text):

    qr =qrcode.QRCode(
        version = 1,
        error_correction = qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", bg_color="white")
    img.save("qrimg.img")


gerador_qr("https://github.com/gigi-dev")

