# ЗАДАЧА №21 		
	
# Зарплата
# (Время: 1 сек. Память: 16 Мб Сложность: 4%)

# В отделе работают 3 сотрудника, которые получают заработную плату в рублях. Требуется определить: на сколько зарплата самого высокооплачиваемого из них отличается от самого низкооплачиваемого.
# Входные данные

# В единственной строке входного файла INPUT.TXT записаны размеры зарплат всех сотрудников через пробел. Каждая заработная плата – это натуральное число, не превышающее 105.
# Выходные данные

# В выходной файл OUTPUT.TXT необходимо вывести одно целое число — разницу между максимальной и минимальной зарплатой. 
txtin=open("input.txt","r")
filein1=int(txtin.readline())
filein2=int(txtin.readline())
filein3=int(txtin.readline())
txtin.close()
txtout= open("output.txt","w")
l=[filein3,filein2,filein1]
min1 = min(l)
max1 = max(l)
c = max1-min1
txtout.write(str(c))
txtout.close()