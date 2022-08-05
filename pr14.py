def push(a,val):
    a.append(val)
    print("Insertion successfull.....")

def pop(a):
    x= a.pop()
    print("Popped Item =",x)

def peek(a):
    index = len(a)-1
    print("Peak Element =",a[index])
    
def display(a):
    print("Stack Elements are:")
    for i in range(len(a)-1,-1,-1):
        print(a[i])
        
a = []
while True:
    choice =int(input("1.Push\n2.Pop\n3.Peek\n4.Display\n5.Exit\nEnter your choice :"))
    if choice==1:
        val=int(input("Enter Number to push:"))
        push(a,val)
    elif choice ==2:
        if len(a)==0:
            print("Stack underflow...")
        else:
            pop(a)
    elif choice ==3:
        if len(a) ==0:
            print("Stack undeflow...")
        else:
            peek(a)
    elif choice==4:
        if len(a)==0:
            print("Stack Underflow...")
        else:
            display(a)
    else:
        break
    