import os
import configparser
from PyPDF2 import PdfFileReader, PdfFileWriter

# Read Config File
config = configparser.ConfigParser()
config.read('/condig/config.cnf')

# Extract Values
source_folder = config.get('DEFAULT', 'source_foldername')
allowable_ext = config.get('DEFAULT', 'allowable_extensions')
dest_folder = config.get('DEFAULT', 'dest_foldername')

# Create destination folder if doesn't exist
if not os.path.exists(dest_folder):
    os.makedirs(dest_folder)

# Initialize PdfFileWriter
pdf_writer = PdfFileWriter()

# Loop through each file in the source folder
for filename in os.listdir(source_folder):
    if filename.endswith(f".{allowable_ext}"):
        pdf = PdfFileReader(f"{source_folder}/{filename}")
        for page_num in range(pdf.getNumPages()):
            page = pdf.getPage(page_num)
            pdf_writer.addPage(page)

# Write to a single PDF file
with open(f"{dest_folder}/merged.pdf", 'wb') as out_pdf:
    pdf_writer.write(out_pdf)
