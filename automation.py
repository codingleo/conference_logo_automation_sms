import sys
from getopt import getopt

import os

import cv2

def main(argv):
    inputfile = ''
    outputfile = ''
    
    try:
        opts, args = getopt(argv, "hi:n:", ["ifile=", "filename="])
    except:
        print("python automation.py -i <inputfile> -n <conference_name>")
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print("python automation.py -i <inputfile> -n <conference_name>")
            sys.exit(2)
        elif opt in ('-i', '--inputfile'):
            inputfile = arg
        
        if opt in ('-n', '--name'):
            outputfile = f"{extract_path(inputfile)}/{arg}"
        else:
            outputfile = f"{extract_path(inputfile)}/new_image"

    write_image_for_navigation(inputfile, outputfile)
    write_image_for_pdf(inputfile, outputfile)

def write_image_for_pdf(input_path, output_path):
    success = resize_image(input_path, f"{output_path}.jpg", 263, 368)

    if success:
        print(f"PDF image written to: {output_path}.jpg")
    else:
        print("Failed writting PDF image")

def write_image_for_navigation(input_path, output_path):
    success = resize_image(input_path, f"{output_path}.png", 90, 120)

    if success:
        print(f"Navigation image written to: {output_path}.png")
    else:
        print("Failed writting navigation image")


def resize_image(input_path, output_path, width, height):
    img = cv2.imread(input_path, cv2.IMREAD_UNCHANGED)
    dim = (width, height)

    resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
    success = cv2.imwrite(output_path, resized)

    return success

def extract_path(image_path: str):
    return '/'.join(image_path.split('/')[:-1])


if __name__ == '__main__':
    main(sys.argv[1:])