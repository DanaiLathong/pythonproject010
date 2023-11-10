# File Handling
# ไฟล์  การจัดการ
# คือ การทำงานเก็บไฟล์
# เขียนข้อมูลลงไฟล์ คือ output
# อ่านข้อมูลในไฟล์ คือ input
# การเปิดไฟล์ write (w) / extend (x) / read (r)

try :
    f_iot = open ("iot4.txt" , "x" , encoding="utf-8") # ถ้าไม่มีไฟล์มันจะสร้างใหม่

    f_iot.write ("hello na ja")
    f_iot.write ("hello naaa jaaa\n")
    f_iot.write ("hello naaaa jaaaa\n")
    f_iot.write ("HI kub\n")

    f_iot.close()
except FileExistsError :
    print ("กรุณาเปลี่ยนชื่อไฟล์ เพราะ ซ้ำ .... --")