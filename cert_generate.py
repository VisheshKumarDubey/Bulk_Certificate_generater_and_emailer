# import required classes

from PIL import Image, ImageDraw, ImageFont

def certificateGenerate(sno, name, department, event_name, event_date, email):
    # create Image object with the input image

    image = Image.open('template.jpg')
    #print(image)

    # initialise the drawing context with
    # the image object as background

    draw = ImageDraw.Draw(image)
    # create font object with the font file and specify
    # desired size

    font = ImageFont.truetype('PTSansNarrow-Bold.ttf', size=35)
    font2 = ImageFont.truetype('PTSansNarrow-Bold.ttf', size=95)
    font3 = ImageFont.truetype('PTSansNarrow-Bold.ttf', size=65)
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
    
    image.save('Certificates/CertificatesPNG/'+email+".jpg")
   