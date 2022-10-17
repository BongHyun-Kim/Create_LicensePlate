from PIL import Image, ImageDraw, ImageFont
import random
import os
from tqdm import tqdm

import info

korean = ['아', '바', '사', '자', '배']

def sales_plate(count):
    for f in tqdm(range(len(info.font_list))):
        for i in tqdm(range(int(count))):
            fore_num = [random.choice(info.number) for i in range(2)]
            seperator = [random.choice(korean) for i in range(1)]
            rear_num = [random.choice(info.number) for i in range(4)]
            region_select = [random.choice(info.region_list) for i in range(1)]

            region_fw = region_select[0][0:1]
            region_lw = region_select[0][1:]

            fore_num = ["".join(fore_num)]
            rear_num = ["".join(rear_num)]
            plate_words = fore_num + seperator + rear_num
            plate_words.insert(2," ")
            str = "".join(plate_words)
            draw_text = str
            font_dir = "./fonts/" + info.font_list[f]

            font = ImageFont.truetype(font_dir, 60, encoding = "unic")
            region_font = ImageFont.truetype(font_dir, 30, encoding="unic")

            path = "plate_back/license_plate_sales.png"
            image_pil = Image.open(path)
            draw = ImageDraw.Draw(image_pil)
            w, h = font.getsize(draw_text)
            if 'ARITA' in info.font_list[f]:
                draw.text((63, 18), draw_text, 'black', font)
                draw.text((30, 13), region_fw, 'black', region_font)
                draw.text((30, 43), region_lw, 'black', region_font)
            else:
                draw.text((63, -1), draw_text, 'black', font)
                draw.text((30, 5), region_fw, 'black', region_font)
                draw.text((30, 35), region_lw, 'black', region_font)

            image_pil.save(os.path.join(info.path + region_fw + region_lw + draw_text + '.png'), "PNG")