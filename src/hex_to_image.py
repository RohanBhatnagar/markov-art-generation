from PIL import Image

from generative_art import generative_art 

class hex_to_image():
    def hexToImage(self, hex_string, image_width, image_height):
        size_tuple = (image_width, image_height)
        new_im = Image.new('RGB', size_tuple, "black")
        pixels = new_im.load()


        for i in range(0, image_width, 1):
            for j in range(0, image_height, 1):
                pixels[i,j] = hex_to_image.hexToDecimal(self, hex_string[:6])
                hex_string = hex_string[6:]

        return new_im

    def hexToDecimal(self, hex_color):
        return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
