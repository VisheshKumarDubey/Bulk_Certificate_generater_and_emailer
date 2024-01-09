import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import xlrd
import os

# import required classes
from cert_generate import certificateGenerate

def sendMail(file):
    wb = xlrd.open_workbook(file)
    sheet = wb.sheet_by_index(0)

    for x in range(1, sheet.nrows):
        name = sheet.row_values(x)[2]
        len1 = name.find(' ')
        name = name[0:len1]
        email = str(sheet.row_values(x)[1])
        fromaddr = "thecampusmonk@gmail.com"  # Your Gmail address
        password = "jGsdzKTHBIrODA4k"  # Your Gmail password
        toaddr = email
        email = toaddr[0:toaddr.find('@')]
        
        print("\nSending.. to "+name+" at "+email)
        
        # Create the HTML content for the email body
        html_content = f"""
        <html>
            <body>
                <p>Hi {name},</p>
                <p>Challenge conquered! Let's share our win on Instagram/LinkedIn — You can tag us there, and we'll surely give a shoutout!</p>
                <p>Please find your certificate in the attachments.</p>
                </br>
                <p>Regards</p>
                <p><strong>Rachit Rastogi</strong></p>
                <p>Founder - Campusmonk</p>
            </body>
        </html>
        """

        # Create the email message
        msg = MIMEMultipart()
        msg['From'] = fromaddr
        msg['To'] = toaddr
        msg['Subject'] = "Campusmonk - Certificate for Instagram Clone"

        # Attach HTML content as the email body
        msg.attach(MIMEText(html_content, 'html'))

        # Attach the certificate PDF file
        filename = email + ".pdf"
        attachment_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..','output','pdf' , f'{email}.pdf'))
        with open(attachment_path, 'rb') as attachment:
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(attachment.read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', f'attachment; filename= {filename}')
            msg.attach(part)

        # Create SMTP session and send the email
        with smtplib.SMTP('smtp-relay.brevo.com', 587) as server:
            server.starttls()
            server.login(fromaddr, password)
            server.sendmail(fromaddr, toaddr, msg.as_string())
