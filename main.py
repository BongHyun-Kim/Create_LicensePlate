

import latest_plate
import secondary_plate
import third_plate
import equip_plate_type1
import equip_plate_type2
import sales_plate
import sales_plate_older
import plate_older

# import CVRotate as cv_rotate

count = input("각 번호판을 몇개씩 만들지 입력하시오 \n")

latest_plate.latest_plate(count)
secondary_plate.secondary_plate(count)
third_plate.third_plate(count)
equip_plate_type1.equip_plate_type1(count)
equip_plate_type2.equip_plate_type2(count)
sales_plate.sales_plate(count)
sales_plate_older.sales_plate_older(count)
plate_older.plate_older(count)

# cv_rotate.rotate()

print("번호판 가상 데이터 생성 완료")