from instabot import Bot
from text_to2_image import getImage
import requests
import time

bot = Bot()
bot.login(username="xxxxx", password="xxxxx")

while True:
    cur_id = 1
    response = requests.get('http://127.0.0.1:8000/Questions/')
    if response.status_code == 200:
        data = response.json()
        flag = 0
        if cur_id == 6:
            cur_id += 1
        for d in data:
            if d['id'] == cur_id:
                author, question = d['name'], d['question']
                getImage(question, cur_id)
                bot.upload_photo('static\images\post' +
                                 str(cur_id)+'.jfif', 'Author = '+author)
                time.sleep(5)
                cur_id += 1
