# QR CODE GENERATIOR IN PYTHON

# import qrcode as qr
# img = qr.make("https://www.youtube.com/watch?v=XZfoSEVscgU")
# img.save('wscube_youtube.png')

import qrcode

from PIL import Image

qr= qrcode.QRCode(version= 1, error_correction= qrcode.constants.ERROR_CORRECT_H, box_size=10, border=4,)

qr. add_data('https://www.wscube.com/')
qr.make(fit=True)
img = qr.make_image(fill_color='green', back_color= 'black')
img.save('wscubex.png')


