from tkinter import Tk, filedialog
import xlrd
from cert_generate import certificateGenerate
from bulk_email import sendMail

class CertificateGenerator:
    def __init__(self, event, date):
        self.event = event
        self.date = date

    def select_file(self):
        root = Tk()
        root.withdraw()
        filetypes = (('Excel files', '*.xlsx'), ('All files', '*.*'))
        file_path = filedialog.askopenfilename(title='Open a file', filetypes=filetypes)
        return file_path

    def generate_certificates(self, file_path):
        wb = xlrd.open_workbook(file_path)
        sheet = wb.sheet_by_index(0)
        
        print("Your Certificates are being generated..")
        for x in range(sheet.nrows):
            name = sheet.row_values(x)[2]
            email = sheet.row_values(x)[1]
            department = sheet.row_values(x)[3]
            if sheet.row_values(x)[4]:
                department += '(' + sheet.row_values(x)[4] + ')'

            len1 = email.find('@')
            email = email[:len1]
            certificateGenerate(x, name, department, self.event, self.date, email)

        email_or_not = input("Do you want to email all the certificates? (Y/N)")
        if email_or_not.lower() == 'y':
            sendMail(file_path)
        else:
            print('Mails are not sent')

def main():
    event_name = "CodeByte"
    event_date = "20-20-20XX"

    generator = CertificateGenerator(event_name, event_date)
    file_path = generator.select_file()
    generator.generate_certificates(file_path)

if __name__ == "__main__":
    main()
