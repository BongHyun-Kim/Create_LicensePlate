from PIL import Image, ImageDraw, ImageFont
import random
import os
from tqdm import tqdm

import info


def equip_plate_type1(count):
    for f in tqdm(range(len(info.font_list))):
        for i in tqdm(range(int(count))):
            fore_num = [random.choice(info.number) for i in range(2)]
            seperator = [random.choice(info.korean) for i in range(1)]
            rear_num = [random.choice(info.number) for i in range(4)]
            fore_num = ["".join(fore_num)]
            rear_num = ["".join(rear_num)]
            region_select = [random.choice(info.region_list) for i in range(1)]

            region_fw = region_select[0][0:1]
            region_lw = region_select[0][1:]
            plate_words = fore_num + seperator + rear_num
            plate_words.insert(2," ")
            str = "".join(plate_words)
            draw_text = str
            font_dir = "./fonts/" + info.font_list[f]
            font = ImageFont.truetype(font_dir, 55, encoding="unic")
            region_font = ImageFont.truetype(font_dir, 45, encoding="unic")
            path = "plate_back/license_plate_equipment.png"
            image_pil = Image.open(path)
            draw = ImageDraw.Draw(image_pil)
            w, h = font.getsize(draw_text)
            # draw.text((43, 23), draw_text, 'black', font)

            if 'ARITA' in info.font_list[f]:
                draw.text((32, 58), draw_text, 'black', font)
                draw.text((90, 15), region_fw, 'black', region_font)
                draw.text((180, 15), region_lw, 'black', region_font)
            else:
                draw.text((37, 48), draw_text, 'black', font)
                draw.text((90, 5), region_fw, 'black', region_font)
                draw.text((180, 5), region_lw, 'black', region_font)

            image_pil.save(os.path.join(info.path + region_fw + region_lw + draw_text + '.png'), "PNG")