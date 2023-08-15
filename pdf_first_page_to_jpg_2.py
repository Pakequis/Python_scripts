import os
from pdf2image import convert_from_path

script_dir = os.path.dirname(os.path.abspath(__file__))
pdf_dir = script_dir

print("PDF to image start...")

error_files = []

for root, dirs, files in os.walk(pdf_dir):
    for pdf_file in files:
        if pdf_file.endswith(".pdf"):
            pdf_path = os.path.join(root, pdf_file)

            try:
                pages = convert_from_path(pdf_path, 150, None, 1, 1)  # segundo parâmetro é a qualidade da imagem
                pdf_file = pdf_file[:-4]

                output_dir = os.path.dirname(pdf_path)

                image_path = os.path.join(output_dir, f"{pdf_file}.jpg")
                pages[0].save(image_path, "JPEG")
                print(f"Converted: {pdf_path}")
            except Exception as e:
                error_files.append(pdf_path)
                print(f"Error converting {pdf_path}: {e}")

if error_files:
    print("Files with errors:")
    for file in error_files:
        print(file)

print("End...")