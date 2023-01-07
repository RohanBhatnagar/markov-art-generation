from PIL import Image 
import base64

path = "/Users/rohanbhatnagar/Desktop/markov-art-generation/src/sample.JPG"
image = Image.open(path)
image = Image.eval(image, (lambda x: x-50))
# image.show()
# colors = image.getcolors(1000000000) #num colors in image 

[im1, im2, im3] = image.split() 
# im1.show()
# im2.show()
# im3.show()

# with open(path, "rb") as image2string:
#     image_str = base64.b64encode(image2string.read())
# print(image_str)

