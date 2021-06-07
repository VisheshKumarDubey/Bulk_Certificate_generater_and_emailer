# Python code to illustrate Sending mail with attachments 
# from your Gmail account 

# libraries to be imported 
import smtplib 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders 

import xlrd
# import required classes
from cert_generate import certificateGenerate
from PIL import Image, ImageDraw, ImageFont 
  
loc = ("indexgit.xlsx") 
  
wb = xlrd.open_workbook(loc) 
sheet = wb.sheet_by_index(0) 
  
sheet.cell_value(0, 0) 
  

for x in range(1,sheet.nrows):
    name=sheet.row_values(x)[1]
    len1 = name.find(' ')
    name = name[0:len1]
    email=sheet.row_values(x)[0]
    fromaddr = "emailaddress"
    toaddr =email
    print("\nSending.. to "+name+" at "+email)
    len1 = toaddr.find('@')
    email = toaddr[0:len1]
    

    # instance of MIMEMultipart 
    msg = MIMEMultipart() 

    # storing the senders email address 
    msg['From'] = fromaddr 
    
    year =2

    # storing the receivers email address 
    msg['To'] = toaddr 

    # storing the subject 
    msg['Subject'] = "Subject"

    # string to store the body of the mail 

    body = "Body"
    # attach the body with the msg instance 
    msg.attach(MIMEText(body, 'plain')) 

    # open the file to be sent 
    #filename = email+".pdf"
    #attachment = open("certificates/certificatesPDF/"+email+".pdf", "rb") 

    # instance of MIMEBase and named as p 
   # p = MIMEBase('application', 'octet-stream') 

    # To change the payload into encoded form 
    #p.set_payload((attachment).read()) 

    # encode into base64 
    #encoders.encode_base64(p) 

    #p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 

    # attach the instance 'p' to instance 'msg' 
    #msg.attach(p) 

    # creates SMTP session 
    s = smtplib.SMTP('smtp.gmail.com', 587) 

    # start TLS for security 
    s.starttls() 

    # Authentication 
    s.login(fromaddr, "Password") 

    # Converts the Multipart msg into a string 
    text = msg.as_string() 

    # sending the mail 
    s.sendmail(fromaddr, toaddr, text) 

    # terminating the session 
    s.quit() 
