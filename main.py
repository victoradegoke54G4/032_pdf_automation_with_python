# Adding Cover Sheet to PDF files
"""The project will add cover sheet to all PDF files in the current directory and this will automate daily routine task."""

 
from PyPDF2 import PdfReader, PdfWriter

import os,shutil

if os.path.exists("Output Files"):
    shutil.rmtree("Output Files")

os.mkdir("Output Files")

file_directory = os.listdir('./Input Files')
for file in file_directory:
    if file.endswith('.pdf'):
        pdf_reader_cover =PdfReader('./Input Files/cover_sheet.pdf')
        page_cover = pdf_reader_cover.pages[0]

        pdf_reader = PdfReader(f'./Input Files/{file}')
        pdf_writer = PdfWriter()
        pdf_writer.add_page(page_cover)

        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            pdf_writer.add_page(page)
        
        with open(f"./Output Files/{file.replace('.pdf', '')}_cover.pdf", "wb") as output:
            pdf_writer.write(output)
