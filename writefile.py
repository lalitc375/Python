import os

fo=open("test.txt","w")
fo.write("This is test file create by python program writefile.py")
fo.close()
fo=open("test.txt","r")
print (fo.read())
fo.close()
