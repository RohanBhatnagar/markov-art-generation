from PIL import Image

from generative_art import generative_art 

class hex_to_image():
    def hexToImage(self, hex_string, image_width, image_height, k):
        size_tuple = (image_width, image_height)
        new_im = Image.new('RGB', size_tuple, "black")
        # new_im.show()
        pixels = new_im.load()

        for i in range(0, image_width, 1):
            for j in range(0, image_height, 1):
                pixels[i,j] = tuple(hex_to_image.hexToDecimal(self, hex_string[0: k: 1]))
                hex_string = hex_string[k: len(hex_string)]

        return new_im

    def hexToDecimal(self, hex_color):
        rgb = []
        for i in (0,2,4):
            hex = "0x" + hex_color[i:i+2]
            print(hex)
            decimal = int("0x" + str(hex_color[i: i+2]), 16)
            rgb.append(decimal)
        return rgb
