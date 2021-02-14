txt = open("hh.txt","r")
r1=0
r2=0
f = txt.readline(1).split()
r1=int(f[1])+r1
r2=int(f[2])+r2
f2 = txt.readline(2).split()
r1=int(f2[1])+r1
r2=int(f2[2])+r2
f3= txt.readline(3).split()
r1=int(f3[1])+r1
r2=int(f3[2])+r2
f4 = txt.readline(4).split()
r1=int(f4[1])+r1
r2=int(f4[2])+r2
txt.close()
txt2=open("outinput.txt","w")
if r1>r2:
    txt2.write("1")
if r1<r2:
    txt2.write("2")
else:
    txt2.write("DRAP")
txt2.close()