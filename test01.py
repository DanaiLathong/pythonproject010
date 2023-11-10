# Exception handling
# ข้อผิดพลาด การจัดการ
#try except finally 

# Exception เกิดจากข้อผิดพลาดจากโปรอแกรม

try :
    num1 = int(input("Input Number 1 : "))
    num2 = int(input("Input Number 2 : "))

    print (f"num 1 = {num1}")
    print (f"num 2 = {num2}")

    sum = num1 + num2
    result = num1 / num2


    print (f"ผลบวกรวมของ {num1} + {num2} คือ {sum} ")
    print (f"ผลหารรวมของ {num1} / {num2} คือ {result} ")
except ValueError :
    print ("โปรดติดต่อเจ้าหน้าที่ หรือ กรุณากรอกแต่ตัวเลข ---- สงสัยติดต่อคนเขียน")
except ZeroDivisionError :
    print ("ต้องเป็นจำนวนเต็มป้อนตัวเลขตัวที่ 2 ห้ามเป็น 0 ---- สงสัยติดต่อคนเขียน")
except Exception :
    print ("มีข้อผิดพลาดกรุณากรอกดีๆดิว่ะ ---- สงสัยติดต่อคนเขียน")
finally :
    print ("Wow....")
    print ("Hello...")