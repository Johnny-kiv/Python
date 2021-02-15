#Решение Johnny.kiv
# ЗАДАЧА №25 		
	
# Больше-меньше
# (Время: 1 сек. Память: 16 Мб Сложность: 3%)

# Одна из основных операций с числами – их сравнение. Мы подозреваем, что вы в совершенстве владеете этой операцией и можете сравнивать любые числа, в том числе и целые. В данной задаче необходимо сравнить два целых числа.
# Входные данные

# В двух строчках входного файла INPUT.TXT записаны числа A и B, не превосходящие по абсолютной величине 2×109.
# Выходные данные

# Запишите в выходной файл OUTPUT.TXT один символ "<", если A < B, ">", если A > B и "=", если A=B.
txtin=open("input.txt","r")
filein1=txtin.readline()
filein2=txtin.readline()
txtin.close()
txtout=open("output.txt","w")
if int(filein1)==int(filein2):
    txtout.write("=")
elif int(filein1>filein2):
    txtout.write(">")
elif int(filein1<filein2):
    txtout.write("<")
txtout.close()