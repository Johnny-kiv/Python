#####################################
# Программа должна задумать число от 1 до 99
# ПОльзователю предоставляется возможность
# угадать число за 8 ходов
# Автор: Johnny KIV
#####################################
import random
a=1
i=0
print('Тебе даётся 8 попыток штоб угадать загадоное число. ')
rand=random.randint(1,99)
for u in range(8):
    i=i+1
    b=rand
    a=int(input('Введи число:'))
    if a==rand:
        print('Правильно! Было число ',a)
        break
    elif a<rand:
        print('\a Неправильно, загадоное число, больше')
    elif a>rand:
        print('\a Неправильно, загадоное число, меньше')    
print('Было число',b)
print('Вы отгодали с',i,'попытки')
print('До всречи в следуйший раз')
