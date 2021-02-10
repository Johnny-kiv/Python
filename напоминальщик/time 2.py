#Это напоминальщик 
#версия 2
#Автор: johnny-kiv  

import time

a2=int(input("Введите минуты работы: "))
b2=int(input("Введите минуты отдыха: "))
a4=a2*60
b4=b2*60
r=1

print("Работаем")

while r:
    time.sleep(a4)
    print("\a  \n \t Отдыхаем")

    time.sleep(b4)

    print("\a Работаем")
