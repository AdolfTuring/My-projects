class Employyes():
    lsemployyes={}
    def __init__(self, name, age, salary, job='Important job'):
        self.name=name
        self.age=age
        self.salary=salary
        self.job=job
        Employyes.lsemployyes[name]=f'Name: {name}, Age: {age}, Salary: {salary}, Job: {job}'   

    def show(self):
        print(f'Name: {self.name}\nAge: {self.age}\nSalary: {self.salary}\nJob: {self.job}')

    def salRaise(self, s):
        self.salary=self.salary+s

    def ShowEmployes(self):
        for x in Employyes.lsemployyes:
            print(Employyes.lsemployyes[x])
    
    def Fire(n):
        Employyes.lsemployyes.pop(n.name)

        

class Developer(Employyes):
    def __init__(self, name, age, salary, skill):
        Employyes.__init__(self, name, age, salary, job='Developer')
        self.skill=skill

    def ShowSkill(self):
        print(self.skill)

class Manager(Employyes):
    def __init__(self, name, age, salary):
        Employyes.__init__(self, name, age, salary, job='Manager')
        self.empl=[]

    def ShowDevs(self):
        print(self.empl)
    
    def addDevs(self, n):
        self.empl.append(n.name)

class ProjManager(Employyes):
    def __init__(self, name, age, salary):
        Employyes.__init__(self, name, age, salary, job='Project Manager')
        self.proj=[]

    def ShowProj(self):
        print(self.proj)
    
    def addProj(self, n):
        self.proj.append(n)



if __name__=='__main__':
    ad=Employyes('Jhon',26,150)
    ad.show()

    ser=Developer('Serhii',27,250,'Python')
    ser.show()

    vit=Manager('Vita',22,350)
    vit.show()
    
    vit.salRaise(200)
    vit.show()
    print(f'Vitas salsry are: {vit.salary}')
    dim=Developer('Dimma',27,250,'Python')
    vit.addDevs(dim)
    vit.ShowDevs()

    Employyes.ShowEmployes(Employyes)
    Employyes.Fire(ad)
    Employyes.ShowEmployes(Employyes)