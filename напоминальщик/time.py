#Это напоминальщик 
#версия 1
#Автор: johnny-kiv  
import time
a1=int(input("Введите секунды работы: "))
a2=int(input("Введите минуты работы: "))
a3=int(input("Введите часы работы: "))
b1=int(input("Введите секунды отдыха: "))   
b2=int(input("Введите минуты отдыха: "))
b3=int(input("Введите часы отдыха: "))
a4=a2*60+a1+3600*a3
b4=b2*60+b1+3600*b3
r=1
t=0
t1=0
print("Работаем")
while r:
    for r in range(a4):
        t=t+1
        time.sleep(1)
        print(t)
    print("\a  \n \t Отдыхаем")
    t=0
    for r in range(b4):
        t1=t1+1
        time.sleep(1)
        print(t1)
    print("\a Работаем")
    t1=0
