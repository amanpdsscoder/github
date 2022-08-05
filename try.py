import pickle
emp = {}
found = False
fin = open('emp1.dat', 'rb+')
fin.seek (0)
try:
    while True :
        rpos = fin.tell()
        emp = pickle.load(fin)
        if emp['Empno'] == 1251 :
            emp[ 'Salary'] = emp['Salary'] + 2000
            fin.seek (rpos)
            pickle.dump(emp, fin)
            print (emp)
            found = True
except EOFError:
    if found == False:
        print("Sorry, no matching record found.")
    else:
        print("Record(s) successfully updated.")
    fin.close()
