
from tkinter import * 
from tkinter import ttk
from tkinter import filedialog as fd
import os
# Program to extract a particular row value 
import xlrd
# import required classes
from cert_generate import certificateGenerate
from bulk_email import sendMail

Tk().withdraw()

class Main:

    filetypes = (
        ('Excel files', '*.xlsx'),
        ('All files', '*.*')
    )

    def __init__(self, event, date):
        self.event = event
        self.date = date
        self.file = fd.askopenfilename(title='Open a file',  filetypes=self.filetypes)

    def run(self):
        wb = xlrd.open_workbook(self.file) 
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
            len1 = email.find('@')
            email = email[0:len1]
            certificateGenerate(x, name, department, self.event, self.date, email)
            #print(str(x)+"      "+name +"       "+ department +"     "+ event_name+"        "+event_date)
        email_or_not = input("Do you want to email all the certificates? (Y/N)")
        if email_or_not == 'Y' or email_or_not == 'y':
            sendMail(self.file)
        else:
            print('Mails are not sent')

m = Main("CodeByte", "20-20-20XX")
m.run()

