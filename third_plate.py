from PIL import Image, ImageDraw, ImageFont
import random
import os
from tqdm import tqdm

import info


def third_plate(count):
    for f in tqdm(range(len(info.font_list))):
        for i in tqdm(range(int(count))):
            fore_num = [random.choice(info.number) for i in range(2)]
            seperator = [random.choice(info.korean) for i in range(1)]
            rear_num = [random.choice(info.number) for i in range(4)]
            fore_num = ["".join(fore_num)]
            rear_num = ["".join(rear_num)]
            plate_words = fore_num + seperator + rear_num
            plate_words.insert(2," ")
            str = "".join(plate_words)
            draw_text = str
            font_dir = "./fonts/" + info.font_list[f]
            font = ImageFont.truetype(font_dir, 55, encoding="unic")
            path = "plate_back/license_plate_sm.png"
            image_pil = Image.open(path)
            draw = ImageDraw.Draw(image_pil)
            w, h = font.getsize(draw_text)
            # draw.text((43, 23), draw_text, 'black', font)

            if 'ARITA' in info.font_list[f]:
                draw.text((41, 23), draw_text, 'black', font)
            else:
                draw.text((41, 7), draw_text, 'black', font)

            image_pil.save(os.path.join(info.path + draw_text + '.png'), "PNG")