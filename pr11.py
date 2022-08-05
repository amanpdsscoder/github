fname=input("Enter the file name : ")
fp=open(fname,"r")
sr=1
while True:
    data=fp.readline()
    if data=="":
        break
    print(sr,". ",data)
    sr=sr+1
fp.close()