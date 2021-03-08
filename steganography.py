#! /usr/bin/python3


import cv2
import time
import os
import numpy
import optparse
from PIL import Image


class Hide_reveal:
    def __init__(self):
        try:
            self.values = ""
            self.values = self.get_arguments()
            if self.values.hide and self.values.message and self.values.image:
                self.hide_data()
            elif self.values.reveal and self.values.image:
                list_object = self.reveal_data()
                self.show_data(list_object)
        except KeyboardInterrupt:
            print("Exiting...")
            time.sleep(1)
            os.sys.exit(0)

    def get_arguments(self):
        parser = optparse.OptionParser()
        parser.add_option("-i","--hide",dest="hide",help="Choose this if you want to hide a message behind an image(option + yes)")
        parser.add_option("-s","--message",dest="message",help="Type the string you want to hide behind the image")
        parser.add_option("-r","--reveal",dest="reveal",help="Type this to reveal the secret message(option + yes)")
        parser.add_option("-m","--image",dest="image",help="Type the path of the image that you want to hide the message in")
        values = parser.parse_args()[0]
        if not values.hide and not values.reveal:
            parser.error("You have to choose one from this options(reveal or hide)")
        elif values.hide  and not values.message and not values.image:
            parser.error("You have to type the message you want to  hide,and the image you want to hide behind it..")
        elif values.hide and values.message and not values.image:
            parser.error("You have to type the image you want to hide the message behind it..")
        elif values.hide and values.image and not  values.message:
            parser.error("You have to type the message yo u want behind the image..")
        elif values.reveal and not values.image:
            parser.error("You have to pass me the encoded image..")
        elif values.reveal and values.image and values.message:
            parser.error("Wrong usage for --message option(it needs only for hiding data)!!")
        else:
            return values

    def encode_image(self,image):
        print("Checking if the image is compatiible for steganography...")
        if not image.split(".")[-1]:
            print("I want an image with .png extension!!")
            print("Exiting...")
            time.sleep(2)
            os.sys.exit(0)
        else:
            accepted_extensions = [".PNG",".png"]
            extension = image.split(".")[-1]
            extension = "." + extension 
            if extension not in accepted_extensions:
                print("Incompatible image extension..")
                print("Exiting...")
                time.sleep(2)
                os.sys.exit(0)
            else:
                encoded_image = cv2.imread(image)
                time.sleep(2)                
                return encoded_image
 
        
    def convert_to_binary(self,data):
        #print(type(data))
        if type(data) == str:
            data =  ''.join([format(ord(i),"08b") for i in data])
            return data
        elif  type(data) == int or type(data) == numpy.uint8:
            return format(data,"08b")
        elif  type(data) == numpy.ndarray or type(data) == bytes:
            data = [format(i,"08b") for i in data]
            return data
            

    def save_image(self,image):
        print("Type the image file that you want to save in the steg image")
        accepted_extensions = [".png",".PNG"]
        path = os.sys.stdin.readline()
        path = path.strip("\n")
        extension = "." + path.split(".")[-1]
        if extension not in accepted_extensions:
            print("Incompatible image type")
            print("Exiting...")
            os.sys.exit(0)
        else:
            cv2.imwrite(path,image)
            if os.path.exists(path):
                print("Image saved successfully...")
                time.sleep(1)
            else:
                print("Error saving your image...")
                time.sleep(1)
                os.sys.exit(0)


    def hide_data(self):
        print("Encoding your image...")
        time.sleep(2)
        image = self.encode_image(self.values.image)
        print("Image encoded...")
        time.sleep(2)
        print("Calculate the image size...")
        time.sleep(1)
        size = image.size 
        image_in_bytes = size *3 //8
        if len(self.values.message) > size:
            print("Message too big for this image")
            print("Exiting...")
            time.sleep(2)
            os.sys.exit(0)
        print("Converting your message into binaries...")
        time.sleep(2)
        self.values.message = self.values.message + "*****"
        encoded_message = self.convert_to_binary(self.values.message)
        print("Message converted!!")
        time.sleep(2)
        print("Start hiding your message..")
        time.sleep(1)
        pointer = 0
        for i in image:
            for pixel in i:
                red,green,blue = self.convert_to_binary(pixel)
                if pointer < len(encoded_message):
                    pixel[0] = int(red[:-1] + encoded_message[pointer],base=2)
                    pointer = pointer + 1
                if pointer < len(encoded_message):
                    pixel[1] = int(green[:-1] + encoded_message[pointer],base=2)
                    pointer = pointer + 1
                if pointer <len(encoded_message):
                    pixel[2] = int(blue[:-1] + encoded_message[pointer],base=2)
                    pointer = pointer + 1                   
                else:
                    break

        print("Saving your new image...")
        time.sleep(1)
        self.save_image(image)


    def reveal_data(self):
        if not os.path.exists(self.values.image):
            print("Path does not exist...")
            print("Exiting...")
            os.sys.exit(0)
        encoded_image = self.encode_image(self.values.image)
        print("Extracting the secret message....")
        time.sleep(1)
        extract_data = ""
        for i in encoded_image:
            for px in i:
                red,green,blue = self.convert_to_binary(px)
                extract_data = extract_data + red[-1]
                extract_data = extract_data + green[-1]
                extract_data = extract_data + blue[-1]
            
        data = [extract_data[i:i+8] for i in range(0,len(extract_data),8)]
        new_list = []
        for i in data:
            new_list.append(chr(int(i,base=2)))
            if i[-5:] == "'*','*','*','*','*'":
                break
        return new_list[:-5]

    def show_data(self,extracted_data):
        print("Hidden information extracted..")
        time.sleep(2)
        print()
        print(extracted_data)
                



start = Hide_reveal()
start






















