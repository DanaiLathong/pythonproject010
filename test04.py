# File Handling
# ไฟล์  การจัดการ
# คือ การทำงานเก็บไฟล์
# เขียนข้อมูลลงไฟล์ คือ output
# อ่านข้อมูลในไฟล์ คือ input
# การเปิดไฟล์ write (w) / extend (x) / read (r)

f_iot = open ("iot5.txt" , "a" , encoding="utf-8") # ถ้าไม่มีไฟล์มันจะสร้างใหม่

f_iot.write ("1111")
f_iot.write ("2222222\n")
f_iot.write ("333333333333\n")

f_iot.close()