from PIL import Image 

path = "/Users/rohanbhatnagar/Desktop/markov-art-generation/src/sample.JPG"
image = Image.open(path)

class generative_art(object):
    def __init__(self, image, path):
        self.image = Image.open(path) 
        num_pixels = self.image.height * self.image.width

    def convertHex(self, image):
        hexString = ""
        pix = self.image.load()
        imageWidth = self.image.width
        imageHeight = self.image.height 

        for i in range(0, imageWidth, 1):
            for j in range(0, imageHeight, 1):
                r = pix[i, j][0]
                g = pix[i, j][1]
                b = pix[i, j][2]

                hexString += generative_art.reHex(r) + generative_art.reHex(g) + generative_art.reHex(b) 

        return hexString
    
    def reHex(hex_str):
        res = str(hex_str).replace("0x", "")
        if len(str(res)) == 1:
            return str(0) + res
        return res



        



