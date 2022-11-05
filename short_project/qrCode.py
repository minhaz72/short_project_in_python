#  let'c create a qr code :  
import pyqrcode 
import png 
from pyqrcode import QRCode 


s= 'www.geekforgeeks.com'
url=  pyqrcode.create(s)

url.svg('myqr.svg',scale= 8 )
url.png('myqr.png', scale=6)
