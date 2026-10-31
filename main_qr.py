def generate_qr_code(url,file_path):
    import qrcode
    qr = qrcode.QRCode()
    qr.add_data(url)

    img=qr.make_image()
    img.save(file_path)

    print("QR CODE WAS GENERATED!!!")
