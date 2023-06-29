import os
import csv
import barcode
from barcode.writer import ImageWriter
from sh import lp


def create_code_png(isbn,title):
    isbn13 = barcode.get_barcode_class('code128')
    return isbn13(isbn, writer = ImageWriter())

def remove_forbidden(string_in):
    forbidden_chars = ":;<>\"\\/?*|."
    return "".join([char for char in string_in if char not in forbidden_chars])

def codes_from_csv(list_location,destination_folder):
    with open(list_location, newline='') as csvfile:
        os.chdir(destination_folder)
        for row in csv.reader(csvfile, dialect='excel'):
            code = create_code_png(isbn:=row[0],title:=remove_forbidden(row[1]))
            code.save(isbn + " " + title)


if __name__ == "__main__":
    codes_from_csv("/Users/dheersheth/Desktop/Barcodes_TEST/data.csv","/Users/dheersheth/Desktop/Barcodes_TEST/Images")

import os
from os import listdir


folder_dir = "/Users/dheersheth/Desktop/Barcodes_TEST/Images"
for images in os.listdir(folder_dir):

    if (images.endswith(".png")):
        lp(images)
