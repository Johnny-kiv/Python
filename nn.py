import random
a=1
b=0
i=0
while a:
    i+i+1
    rand=random.randint(1,10)
    a=int(input('Число загадоно попробуй отгадать '))
    if a==rand:
        b=b+1
        print('Правильно! Было число',a)
    else:
        print('Неправильно')
print('До всречи в следуйший раз')
if  b>=10:
    print('Поздравляю, у вас рекорд.',b,'очков')
else:
    print('У вас было',b,'очков')