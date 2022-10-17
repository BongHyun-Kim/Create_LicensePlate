from PIL import Image, ImageDraw, ImageFont
import random
import os
from tqdm import tqdm


import info


def plate_older(count):
    for f in tqdm(range(len(info.font_list))):
        for i in tqdm(range(int(count))):
            fore_num = [random.choice(info.number) for i in range(2)]
            seperator = [random.choice(info.korean) for i in range(1)]
            rear_num = [random.choice(info.number) for i in range(4)]
            region_select = [random.choice(info.region_list) for i in range(1)]

            fore_num = ["".join(fore_num)]
            rear_num = ["".join(rear_num)]
            upper_info = region_select + fore_num
            donw_word = seperator
            down_num = rear_num
            upper_info.insert(1, " ")

            str = "".join(upper_info)
            str1 = "".join(donw_word)
            str2 = "".join(down_num)

            draw_text_up = str
            draw_text_word = str1
            draw_text_num = str2
            draw_text = str + str1 + str2
            font_dir = "./fonts/" + info.font_list[f]

            font = ImageFont.truetype(font_dir, 27, encoding = "unic")
            region_font = ImageFont.truetype(font_dir, 40, encoding="unic")
            num_font = ImageFont.truetype(font_dir, 50, encoding="unic")

            path = "plate_back/license_plate_equipment_type2.png_older.png"
            image_pil = Image.open(path)
            draw = ImageDraw.Draw(image_pil)
            w, h = font.getsize(draw_text_up)

            if 'ARITA' in info.font_list[f]:
                draw.text((60, 18), draw_text_up, 'black', font)
                draw.text((27, 55), draw_text_word, 'black', region_font)
                draw.text((65, 50), draw_text_num, 'black', num_font)
            else:
                draw.text((60, 5), draw_text_up, 'black', font)
                draw.text((27, 36), draw_text_word, 'black', region_font)
                draw.text((65, 30), draw_text_num, 'black', num_font)

            image_pil.save(os.path.join(info.path + draw_text + '.png'), "PNG")