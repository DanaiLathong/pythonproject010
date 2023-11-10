f_iot = open ("iot4.txt" , "r" , encoding="utf-8") # ถ้าไม่มีไฟล์มันจะสร้างใหม่

data = f_iot.read()

f_iot.close()

print (data,"หมดแล้วนะ")