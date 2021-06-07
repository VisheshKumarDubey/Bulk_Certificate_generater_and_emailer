# Program to extract a particular row value 
import xlrd
# import required classes
from cert_generate import certificateGenerate
from PIL import Image, ImageDraw, ImageFont 
  
loc = ("index.xlsx") 
  
wb = xlrd.open_workbook(loc) 
sheet = wb.sheet_by_index(0) 
  
sheet.cell_value(0, 0) 
  
print("Your Certificates are being generated..")
for x in range(0,1):#sheet.nrows):
    name=sheet.row_values(x)[2]
    email=sheet.row_values(x)[1]
    if sheet.row_values(x)[4] :
     department = sheet.row_values(x)[3] +'('+sheet.row_values(x)[4]+')'
    else:
     department = sheet.row_values(x)[3]  

    event_name="CODEBYTE 2.0" 
    event_date = "12-10-2019"
    len1 = email.find('@')
    email = email[0:len1]
    certificateGenerate(x, name, department, event_name, event_date, email)
    #print(str(x)+"      "+name +"       "+ department +"     "+ event_name+"        "+event_date)

