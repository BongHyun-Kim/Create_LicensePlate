import cv2
import numpy as np
import os
from PIL import Image
from tqdm import tqdm

import info

img_list = os.listdir('plate_images')
def rotate():
    for i in tqdm(range(len(img_list))):
        convert_path = np.fromfile((info.path + img_list[i]), np.uint8)
        img = cv2.imdecode(convert_path, cv2.IMREAD_COLOR)
        rows, cols = img.shape[:2]

        pts1 = np.float32([[100, 50], [200, 50], [100, 200]])
        pts2 = np.float32([[100, 60], [200, 50], [100, 200]])

        cv2.circle(img, (100, 50), 5, (255, 0, 0), -1)
        cv2.circle(img, (200, 50), 5, (0, 255, 0), -1)
        cv2.circle(img, (100, 200), 5, (0, 0, 255), -1)

        mtrx = cv2.getAffineTransform(pts1, pts2)

        dst = cv2.warpAffine(img, mtrx, (int(cols*1.5), rows))

        conv_img = Image.fromarray(dst, 'RGB')

        conv_img.save(os.path.join(info.path + img_list[i].split(".")[0] + "_rotated" + ".png"), "PNG")
