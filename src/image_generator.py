from generative_art import generative_art
from hex_to_image import hex_to_image
from markov_model import markov_model 
from PIL import Image

class image_generator():
    def main():
        width_avg = 0
        height_avg = 0
        hex_string = ""
        generated_string = ""

        # k should be a multiple of 6 - hex codes are 6 digits long
        k = int(input("Enter K: "))

        # open list of images txt file
        image_file = open('/Users/rohanbhatnagar/Desktop/markov-art-generation/src/mountains.txt')
        Lines = image_file.readlines()

        for path in Lines: 
            image = Image.open(path.replace("\n", ""))
            width_avg += image.width
            height_avg += image.height
            g_art = generative_art(path.replace("\n", ""))
            hex_string += g_art.convertHex()
            hex_string += hex_string[0:k]

        width_avg = int(width_avg/len(Lines))
        height_avg = int(height_avg/len(Lines))

        model = markov_model(hex_string, k)

        T = width_avg*height_avg*6

        for i in range(0, T - k, 6):
            kgram = hex_string[i: i+k: 1]
            generated_string += model.getRandomChar(kgram)

        image_gen = hex_to_image()
        circular_generated = generated_string + generated_string[0:k]
        image_gen.hexToImage(circular_generated, width_avg, height_avg).show()

    main()
