def generate_qr_code(url, file_path):
    import qrcode
    from inputs import inputs

    qr = qrcode.QRCode()
    qr.add_data(url)

    img=qr.make_image()
    img.save(file_path)
    for img in file_path:
        if img in file_path:
            break
        else:
            print("QR CODE WAS GENERATED!!!")

    return file_path

    


