import requests
import time
from PIL import Image, ImageDraw, ImageFont
import textwrap


def getImage(questions, cur_id):
    image = Image.open('static\images\Template.jfif')
    font = ImageFont.truetype('fonts/OpenSans-Bold.ttf', 12)
    draw = ImageDraw.Draw(image)
    FOREGROUND = (255, 255, 255)
    y_text, w, width = 100, 300, 200
    for question in questions.split('\n'):
        print(question)
        lines = textwrap.wrap(question, width=30)
        for line in lines:
            width, height = font.getsize(line)
            draw.text(((w - width) / 2, y_text), line,
                      font=font, fill=FOREGROUND)
            y_text += height
        y_text += 10
    image.save('static\images\post'+str(cur_id)+'.jfif')
