import os
os.environ["TESSDATA_PREFIX"] = "C:/Program Files/Tesseract-OCR/tessdata"
os.chdir('../data')
lang = 'vie'
number_of_files = len(os.listdir('./'))
for i in range(0, number_of_files):
     # os.system(f"tesseract eng.arial.exp{i}.jpg eng.arial.exp{i} batch.nochop makebox")
    os.system(f"tesseract vie.arial.exp{i}.jpg vie.arial.exp{i} -l {lang} batch.nochop makebox")
