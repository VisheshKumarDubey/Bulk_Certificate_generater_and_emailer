# import required classes
import img2pdf 
import os 
import xlrd
from PIL import Image, ImageDraw, ImageFont

path = os.path.dirname(__file__)
def certificateGenerate(sno, name, department, event_name, event_date, email):
    # create Image object with the input image

    image = Image.open(os.path.dirname(path)+'/templates/template.jpg')
    
    draw = ImageDraw.Draw(image)
 
    font = ImageFont.truetype(os.path.dirname(path)+'/font/PTSansNarrow-Bold.ttf', size=35)
    font2 = ImageFont.truetype(os.path.dirname(path)+'/font/PTSansNarrow-Bold.ttf', size=95)
    font3 = ImageFont.truetype(os.path.dirname(path)+'/font/PTSansNarrow-Bold.ttf', size=65)
    # starting position of the message

    (x, y) = (675, 50)
    xt=sno
    if xt < 10 :
        message = "Sr.No. UU/CSS/2019/E009/00"+ str(xt)+"P"
    elif xt< 99 :
        message = "Sr.No. UU/CSS/2019/E009/0"+ str(xt)+"P"
    else :
        message = "Sr.No. UU/CSS/2019/E009/"+ str(xt)+"P"
    color = 'rgb(0, 0, 0)' # black color

    # draw the message on the background

    draw.text((x, y), message, fill=color, font=font)
    (x, y) = (950, 898)
    color = 'rgb( 0, 0, 0)' # white color
    draw.text((x, y), name, fill=color, font=font2)

    (x, y) = (1550, 1020)
    color = 'rgb( 0, 0, 0)' # white color
    draw.text((x, y), department, fill=color, font=font2)

    (x, y) = (1375, 1145)
    color = 'rgb( 0, 0, 0)' # white color
    draw.text((x, y), "Participation", fill=color, font=font2)

    (x, y) = (1050, 1290)
    color = 'rgb( 0, 0, 0)' # white color
    draw.text((x, y), event_name, fill=color, font=font3)

    (x, y) = (1990, 1290)
    color = 'rgb( 0, 0, 0)' # white color
    draw.text((x, y), event_date, fill=color, font=font3)

    # save the edited image
    
    image.save(os.path.dirname(path)+'/output/jpg/'+email+".jpg")
    img_path = os.path.dirname(path)+'/output/jpg/'+email+".jpg"
    
    # storing pdf path 0
    pdf_path = os.path.dirname(path)+'/output/pdf/'+email+".pdf"
    
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
   