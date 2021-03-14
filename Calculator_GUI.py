from tkinter import *

#math  function  
def mat(a,op,b):
    if op=='+': return str(float(a)+float(b))
    if op=='-': return str(float(a)-float(b))
    if op=='/': return str(float(a)/float(b))
    if op=='*': return str(float(a)*float(b))
#then we calculate function
def calc(pr2):
    res=pr2
    while '/' in res or '*' in res:
        for x in res:
            if x=='*'or x=='/': 
                r=res.index(x)
                c=mat(res[r-1],res[r],res[r+1])
                res=res[:r-1]+res[r+2:]
                res.insert(r-1,c)
    pr2=res
    while len(res)>=3:
        x=mat(res[0],res[1],res[2])
        res=res[3:]  
        res.insert(0,x) 
    return res[0]
# we looking for objects in string
def  fin(pr):
    pr='( '+pr+' )'
    pr2=pr.split()
    while len(pr2)>=3:
        f=-1
        l=0
        for x in range(len(pr2)):
            if pr2[x]=='(':
                f=x
            elif pr2[x]==')':
                l=x
                break
        c=str(calc(pr2[f+1:l]))
        pr2=pr2[:f]+[c]+pr2[l+1:]
    return (float(pr2[0]))
def res():
    c=str(fin(message.get()))
    message_entry.delete (0, 'end' )
    message_entry.insert(0, c)

def clear():
    message_entry.delete (0, 'end' )

window = Tk()
window.title("Калькулятор")
window.geometry('450x200')
lbl = Label(window, text="Введіть приклад використовуючи символи +-/*().\n  Розділяйте цифри та знаки пробілами. Наприклад: 2 + 2 / 4 \n Потім натисніть =", font=("Arial Bold", 12))
lbl.grid(column=0, row=0)

message = StringVar()
message_entry = Entry(textvariable=message, width=60)
message_entry.place(relx=.5, rely=.5, anchor="c", height=30)
 
message_button = Button(text="=", command=res)
message_button.place(x=10, relx=.9, rely=.5, anchor="c")

message_button = Button(text="Очистити", command=clear)
message_button.place(relx=.85, rely=.9, anchor="c")

window.mainloop()