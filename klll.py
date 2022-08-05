from distutils.file_util import write_file
import pickle
def writing():
    fout = open("emp1.dat","wb+")
    while True:
        Empno = int(input("Enter your employee number:"))
        na =input("Enter name: ")
        Salary = float(input("Enter salary: "))
        e = [Empno,na,Salary]
        pickle.dump(e,fout)
        ans = input("Any more records(Y/N)")
        if ans!="Y" and ans!= 'y':
            break
    fout.close
    
def reading():
    fin  = open("emp1.dat","rb")
    try:
        while True:
            e= pickle.load(fin)
            print(e)
    except EOFError:
        pass
    fin.close

writing()
reading()
