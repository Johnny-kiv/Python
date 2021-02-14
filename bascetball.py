txt = open("hh.txt","r")
r1=0
r2=0
f = txt.readline().split()
r1=int(f[0])+r1
r2=int(f[1])+r2
f2 = txt.readline().split()
r1=int(f2[0])+r1
r2=int(f2[1])+r2
f3= txt.readline().split()
r1=int(f3[0])+r1
r2=int(f3[1])+r2
f4 = txt.readline().split()
r1=int(f4[0])+r1
r2=int(f4[1])+r2
txt.close()
txt2=open("outinput.txt","w")
if r1>r2:
    txt2.write("1")
if r1<r2:
    txt2.write("2")
else:
    txt2.write("DRAP")
txt2.close()