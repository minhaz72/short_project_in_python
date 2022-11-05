from rembg import remove 
from PTL import image 

input_path=  "img.jpg "
op_path= 'rm_img.jpg'
img= Image.open(input_path)
op =  remove(input_path)
op.save(op_path)
 