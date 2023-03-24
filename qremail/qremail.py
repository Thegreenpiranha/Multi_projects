import qrcode

# Set up the email address that will be added to the email list
email_address = "seanmcnamra812@gmail.com"

# Set up the URL that will be encoded in the QR code
url = "mailto:" + email_address

# Generate the QR code using the qrcode library
qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
qr.add_data(url)
qr.make(fit=True)

# Save the QR code as a PNG file
img = qr.make_image(fill_color="black", back_color="white")
img.save("email_list_qr_code.png")
