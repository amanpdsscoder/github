def Bsearch(AR,ITEM):
    beg = 0
    last = len(AR)-1
    while(beg<=last):
        mid =(beg+last)//2
        if(ITEM==AR[mid]):
            return mid
        elif(ITEM>AR[mid]):
            beg = mid+1
        else:
            last=mid-1
    else:
        return False
    
N = int(input("Enter desired linear- listsize(max50).."))
print("\n Enter elemets for linear list in Ascending order :\n")
AR = [0]*N
for i in range(N):
    AR[i]=int(input("Element"+str(i+1)+":"))
ITEM=int(input("Enter elemt to be searched for..."))
index = Bsearch(AR,ITEM)
if index:
    print("\n Element found at index",index,"position :",(index+1))
else:
    print("\n Sorry !!!! given element not found.")