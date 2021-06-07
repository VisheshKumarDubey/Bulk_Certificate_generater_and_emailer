# importing necessary libraries 
import img2pdf 
import os 
import xlrd
# import required classes
from cert_generate import certificateGenerate
from PIL import Image, ImageDraw, ImageFont 
  
loc = ("index.xlsx") 
  
wb = xlrd.open_workbook(loc) 
sheet = wb.sheet_by_index(0) 
  
sheet.cell_value(0, 0) 
for x in range(0,sheet.nrows):
    
    email=sheet.row_values(x)[1]
    len1 = email.find('@')
    email = email[0:len1]
    # storing image path  C Users vishe Desktop UUCSS Certificates CertificatesPNG 27vaiagarwal
    img_path = "Certificates/CertificatesJPG/C Users vishe Desktop UUCSS Certificates CertificatesPNG "+email+".jpg"
    
    # storing pdf path 0
    pdf_path = "certificates/certificatesPDF/"+email+".pdf"
    
    # opening image 
    image = Image.open(img_path) 
    
    # converting into chunks using img2pdf 
    pdf_bytes = img2pdf.convert(image.filename) 
    
    # opening or creating pdf file 
    file = open(pdf_path, "wb") 
    
    # writing pdf files with chunks 
    file.write(pdf_bytes) 
    
    # closing image file 
    image.close() 
    
    # closing pdf file 
    file.close() 
    
    # output 
    print("Successfully made pdf file") 