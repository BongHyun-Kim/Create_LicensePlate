import os

list_A = []
number = '0123456789'
for num in number:
    list_A.append(num)  # 번호판의 숫자를 담은 리스트
list_B = []
korean = '가나다라마거너더러머버서어저고노도로모보소오조구누두루무부수우주하허호배'
for kor in korean:
    list_B.append(kor)  # 번호판의 문자를 담은 리스트

region_list = ['강원','경기','경남','경북','광주','대구','대전','부산','서울','세종','울산','인천','전남','전북','제주','충남','충북']

font_list = os.listdir("fonts")

path = "plate_images/"