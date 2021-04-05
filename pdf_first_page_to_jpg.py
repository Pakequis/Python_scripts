# Librarys: pdf2image and poppler-0.68.0

import os
from pdf2image import convert_from_path

pdf_dir = "PATH" #Path to the pdf folder

os.chdir(pdf_dir)

print("PDF to image start...")
for pdf_file in os.listdir(pdf_dir):

    if pdf_file.endswith(".pdf"):

        pages = convert_from_path(pdf_file, 150,None,1,1) #second argument is the image quality
        pdf_file = pdf_file[:-4]

        pages[0].save("%s.jpg" % (pdf_file), "JPEG")
        print(pdf_file)

print("End...")