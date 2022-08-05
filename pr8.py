import csv
fh = open("Items.csv", "w")
iwriter = csv.writer (fh)
ans = 'y'
itemrec = [['Item_Name', 'Description"', 'Price']]
print("Enter item details ")
while ans == 'y' :
    iname = input("Enter Item code : ")
    desc = input("Enter description : ")
    price = float(input("Enter price: "))
    itemrec.append([iname, desc, price])
    ans = input ("Want to enter more items? (y/n)... ")
else:
    iwriter.writerows(itemrec)
    print("Records written successfully.")
fh.close()
