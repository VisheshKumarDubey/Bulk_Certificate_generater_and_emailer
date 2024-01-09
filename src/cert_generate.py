import img2pdf
import os
from PIL import Image, ImageDraw, ImageFont

def certificateGenerate(sno, name, department, event_name, event_date, email):
    path = os.path.dirname(__file__)
    template_path = os.path.join(path, '../templates', 'template.jpg')
    font_path = os.path.join(path, '../font')

    image = Image.open(template_path)
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(os.path.join(font_path, 'GreatVibes-Regular.ttf'), size=95)

    # Customize as needed
    max_text_width = 400  # Maximum width allowed for text
    text_padding = 10  # Padding on both sides

    # Calculate text size for adjustment
    #text_width, text_height = draw.textsize(name, font=font)
    text_width = len(name) 
    adjusted_x = (image.width/2 - (text_width + text_padding)) / 2

    # Adjusting text placement based on the text width and image width
    (x, y) = (adjusted_x, 690)

    # Capitalize name to have the first letter of each word in capital
    name = name.title()

    draw.text((x, y), name, fill='rgb(233, 183, 46)', font=font)

    # Save the edited image
    output_image_path = os.path.join(path, '../output', 'jpg', f'{email}.jpg')
    image.save(output_image_path)

    # Create PDF
    output_pdf_path = os.path.join(path, '../output', 'pdf', f'{email}.pdf')
    with Image.open(output_image_path) as img:
        pdf_bytes = img2pdf.convert(img.filename)
        with open(output_pdf_path, "wb") as file:
            file.write(pdf_bytes)
    
    print("Successfully created PDF file")

# Example usage:
# certificateGenerate(1, "John Doe", "Department", "Event Name", "Event Date", "john@example.com")
