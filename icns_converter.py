import os, sys
from tracemalloc import start
from PIL import Image

def convertSingleImage(imagePath, outputExtension):
    f, e = os.path.splitext(imagePath)
    outfile = f"{f}.{outputExtension}"
    if imagePath != outfile:
        try:
            with Image.open(imagePath) as im:
                im.save(outfile, str.upper(outputExtension))
        except OSError:
            print("cannot convert", imagePath)
    print("Enter quit to close")
    print("1. To convert a single image to another format")
    print("2. To convert a batch images to another format")

def convertBatchImages(imagesPath, inputExtension, outputExtension):
    for infile in os.listdir(imagesPath):
        f, e = os.path.splitext(infile)
        if e != f".{inputExtension}":
            continue
        outfile = f"{f}.{outputExtension}"
        if infile != outfile:
            try:
                with Image.open(os.path.join(imagesPath, infile)) as im:
                    im.save(outfile, str.upper(outputExtension))
            except OSError:
                print("cannot convert", infile)
    print("Enter quit to close")
    print("1. To convert a single image to another format")
    print("2. To convert a batch images to another format")

def main():
    option = "start"
    print("Enter quit to close")
    print("1. To convert a single image to another format")
    print("2. To convert a batch images to another format")
    while option != "quit":
        option = input("")
        if (option == "1"):
            inputPath = input("Enter image path\n")
            outputExtension = input("Enter output image extension\n")
            convertSingleImage(inputPath, outputExtension)
        elif (option == "2"):
            inputPath = input("Enter images input directory\n")
            inputExtension = input("Enter input images extension\n")
            outputExtension = input("Enter output images extension\n")
            convertBatchImages(inputPath, inputExtension, outputExtension)
        else:
            print("Enter a valid choose 1 or 2 to continue")

main()