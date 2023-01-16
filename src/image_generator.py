from PIL import Image
from generative_art import generative_art
from hex_to_image import hex_to_image
from markov_model import markov_model 

class image_generator():
    def main():
        hex_string = ""
        generated_string = ""

        k = int(input("Enter K: "))
        T = int(input("Enter T: "))

        image_file = open('/Users/rohanbhatnagar/Desktop/markov-art-generation/src/images.txt')
        Lines = image_file.readlines()

        for path in Lines: 
            g_art = generative_art(path.replace("\n", ""))
            hex_string += g_art.convertHex()

        model = markov_model(hex_string, k)

        for i in range(0, T - k, 1):
            kgram = hex_string[i: i+k: 1]
            generated_string += model.getRandomChar(kgram)

        image_gen = hex_to_image()
        circular_generated = generated_string + generated_string[0:k]
        image_gen.hexToImage(circular_generated, 300, 240).show()

    main()
