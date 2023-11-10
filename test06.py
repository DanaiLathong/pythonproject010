
f_iot = open ("iot4.txt" , "r" , encoding="utf-8") # ถ้าไม่มีไฟล์มันจะสร้างใหม่

data = f_iot.readline()
print (data,end="")
data = f_iot.readline()
print (data,end="")
data = f_iot.readline()
print (data,end="")

f_iot.close()