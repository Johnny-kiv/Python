import random
txt=open("input.txt","r")
f = txt.read()
txt.close()
r=1
while r:
    rand=random.randint(1,9)
    c=int(f)+rand
    if c<10:
        b=c-int(f)
        break
txt2=open("outinput.txt","w")
txt2.write(str(f)+str(c)+str(b))
txt2.close()