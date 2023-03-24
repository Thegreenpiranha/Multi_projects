import qrcode

# Set up the base URL for the QR code
base_url = "mailto:seanmcnamara3006@gmail.com?subject=Add me to the email list&body=Please add my email address to the list: %s"

# Generate the QR code using the qrcode library
qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)

# Define a function to generate a new QR code with a specific email address
def generate_qr_code(email_address):
    # Create a URL for the email address by replacing the placeholder in the base URL
    url = base_url % email_address

    # Add the URL to the QR code
    qr.add_data(url)
    qr.make(fit=True)

    # Save the QR code as a PNG file
    img = qr.make_image(fill_color="black", back_color="white")
    img.save("email_list_qr_code.png")

# Call the function with a specific email address to generate a QR code for that address
generate_qr_code("seanmcnamara812@gmail.com")



# Set API key and secret
api_key = 'tj00lqyVBVMnElDe'
api_secret = 'RhGBXyDBWcvmDlAkjJif4pkNSqTJhyqp'