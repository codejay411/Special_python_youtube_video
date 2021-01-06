import pyqrcode 
import png 
from pyqrcode import QRCode 
  
  
# String which represents the QR code 
data = "Create custom QR Codes with Logo, Color and Design for free. This QR Code Maker offers free vector formats for best print quality.'"
  
# Generate QR code 
jay = pyqrcode.create(data)
  
# Create and save the png file naming "myqr.png" 
jay.png('qrcode.png', scale=6)











