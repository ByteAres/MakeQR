import qrcode
import time
from colorama import Fore, Back, Style

red = Fore.RED
white = Fore.WHITE

# Prompt the user to enter the link
ByteAres = input(red + '#~ Ares | ' + white + ' Enter the link you want to convert into a QR Code: ')

# Generate the QR code
qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=10, border=4)
qr.add_data(ByteAres)
qr.make(fit=True)

# Save the QR code as an image
qr_image = qr.make_image(fill_color='black', back_color='white')
qr_image.save('qrcode.png')

# Prompt the user that the link has been converted into a QR code
print(red + '#~ Ares | ' + white + 'Generated QR code successfully! ')
time.sleep(5)

# Closes the program
quit()
