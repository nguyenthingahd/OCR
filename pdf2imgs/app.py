from pdf2image import convert_from_path
import os

pdf_dir = '../pdf2imgs/pdf/'
output_dir = 'images'

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

for pdf_file in os.listdir(pdf_dir):
    if pdf_file.endswith('.pdf'):
        pdf_path = os.path.join(pdf_dir, pdf_file)
        images = convert_from_path(pdf_path, 500, poppler_path="C:/Program Files/poppler-24.02.0/Library/bin")

        for i, image in enumerate(images):
            image_path = os.path.join(output_dir, '{}_page{}.jpg'.format(os.path.splitext(pdf_file)[0], i))
            image.save(image_path, 'JPEG')
