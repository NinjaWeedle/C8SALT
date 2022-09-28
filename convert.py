import sys
file = sys.argv[1] 
f = open(file,"rb")
o = open("ROM.txt","w")
k = f.read()
f.close()
l = 0
s = "."
for i in k:
 l += 1
 s+=str(i).zfill(3)
 if l%4==0:
  o.write(s+"\n")
  s="."
o.close()
