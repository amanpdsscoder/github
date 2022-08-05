a = eval(input("Enter a tuple of number:"))
b = int(input("Enter the number to be searched :"))
for i in range(len(a)):
    if(a[i]==b):
        print("Element found at",(i+1),"position")
        break
    else:
        if(i==len(a)-1):
            print("Element not found")
        else:
            continue