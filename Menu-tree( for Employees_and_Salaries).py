import Employees_and_Salaries as f
database=[]

def menu(x, n):
    print(f"Chose option:\n1.Add new {n}\n2.Show all {n}\n3.Fire {n}\n4.Rise salary")
    if x==3:
        print('5.Manager team')

def wait():
    while True:
        print('Press Space than Enter to go in the Menu', end='')
        if input(): break

def addNew(x):
    print("Name: ", end='')
    name=input()
    print("Age: ", end='')
    age=int(input())
    print("Salary: ", end='')
    salary=int(input())
    if x==1:
        print('Its rigt? y/n--', end='')
        choose=input()
        if choose=='y': 
            global database
            emp=f.Employyes(name, age, salary)
            database.append(emp)
        elif choose=='n': addNew(x)
    elif x==2:
        print("Skill: ", end='')
        skill=input()
        print('Its rigt? y/n--', end='')
        choose=input()
        if choose=='y': 
            #global database
            emp=f.Developer(name, age, salary,skill)
            database.append(emp)
        elif choose=='n': addNew(x)
    elif x==3:
        print('Its rigt? y/n--', end='')
        choose=input()
        if choose=='y': 
            #global database
            emp=f.Manager(name, age, salary)
            database.append(emp)
        elif choose=='n': addNew(x)
    elif x==4:
        print('Its rigt? y/n--', end='')
        choose=input()
        if choose=='y': 
            #global database
            emp=f.ProjManager(name, age, salary)
            database.append(emp)
        elif choose=='n': addNew(x)
    wait()

def show(n):
    global database
    for x in database:
        if n==1:
            x.show()
        elif n==2 and x.job=='Developer':
            x.show()
        elif n==3 and x.job=='Manager':
            x.show()
        elif n==4 and x.job=='Project Manager':
            x.show()
    wait()
        
def Fire(n):
    global database
    print("Name: ", end='')
    name=input()
    for x in database:
        if x.name==name:
            database.remove(x)
    wait()

def salraise(x):
    print('Who have a premium?')
    show(x)
    print('Input name: ', end='')
    name=input()
    print('Input premium: ', end='')
    prem=int(input())
    for x in database:
        if x.name==name:
            x.salRaise(prem)
            x.show()
    wait()

while True:
    print("Chose option:\n1.Employyes option\n2.Developers options\n3.Manager options\n4.Project Manager options\n5.Exit")
    x=int(input())
#Employyes menu 
    if x==1:
        menu(1, 'Employye')
        y=int(input())
        #Add Employye
        if y==1:
            addNew(1)      
        #Show all employyes
        if y==2:
            show(x)
        #Fire employyes
        if y==3:
            Fire(x)
        #Salary raise
        if y==4:
            salraise(x)
            
            
#Developers menu 
    if x==2:
        menu(2, 'Developer')
        y=int(input())
        #Add Developer
        if y==1:
            addNew(x)      
        #Show all Developers
        if y==2:
            show(x)
        #Fire Developer
        if y==3:
            Fire(x)
        #Salary raise
        if y==4:
            salraise(x) 

#Manager menu 
    if x==3:
        menu(3, 'Manager')
        y=int(input())
        #Add Manager
        if y==1:
            addNew(x)      
        #Show all Manager
        if y==2:
            show(x)
        #Fire Manager
        if y==3:
            Fire(x)
        #Salary raise
        if y==4:
            salraise(x)
        #Manager team
        if y==5:
            print('Not yet')
            


#ProjectManager menu 
    if x==4:
        menu(4, 'Project Manager')
        y=int(input())
        #Add ProjectManager
        if y==1:
            addNew(x)      
        #Show all ProjectManager
        if y==2:
            show(x)
        #Fire ProjectManager
        if y==3:
            Fire(x)
        #Salary raise
        if y==4:
            salraise(x) 
        

    if x==5:break
