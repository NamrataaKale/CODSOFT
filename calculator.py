from tkinter import *

root=Tk()
root.geometry("470x800")
root.resizable(False,False)
root.title("Calculator")
root.configure(bg="lavender")

a=StringVar()

entry=Entry(root,text=a,borderwidth=10,width=13,font="georgia 35 bold",fg="grey",bg="black")
entry.grid(row=0,column=0,columnspan=5)

def show(op):
    a.set(a.get()+op)
    
def eql():
    exp=a.get()
    a.set(eval(exp))
    
def clr():
    a.set(" ")


b1=Button(root,text="9",font="Futura 35 bold",command=lambda:show("9"),bg="pink",padx=23,pady=20,bd=5)
b1.grid(row=1,column=1)

b2=Button(root,text="8",font="Futura 35 bold",command=lambda:show("8"),bg="pink",padx=20,pady=20,bd=5)
b2.grid(row=1,column=2)

b3=Button(root,text="7",font="Futura 35 bold",command=lambda:show("7"),bg="pink",padx=20,pady=20,bd=5)
b3.grid(row=1,column=3)

b4=Button(root,text="6",font="Futura 35 bold",command=lambda:show("6"),bg="pink",padx=23,pady=20,bd=5)
b4.grid(row=2,column=1)

b5=Button(root,text="5",font="Futura 35 bold",command=lambda:show("5"),bg="pink",padx=20,pady=20,bd=5)
b5.grid(row=2,column=2)

b6=Button(root,text="4",font="Futura 35 bold",command=lambda:show("4"),bg="pink",padx=20,pady=20,bd=5)
b6.grid(row=2,column=3)

b7=Button(root,text="3",font="Futura 35 bold",command=lambda:show("3"),bg="pink",padx=23,pady=20,bd=5)
b7.grid(row=3,column=1)

b8=Button(root,text="2",font="Futura 35 bold",command=lambda:show("2"),bg="pink",padx=20,pady=20,bd=5)
b8.grid(row=3,column=2)

b9=Button(root,text="1",font="Futura 35 bold",command=lambda:show("1"),bg="pink",padx=20,pady=20,bd=5)
b9.grid(row=3,column=3)

b10=Button(root,text="+",font="Futura 35 bold",command=lambda:show("+"),bg="lavender",padx=20,pady=20,bd=5)
b10.grid(row=1,column=4)

b11=Button(root,text="-",font="Futura 35 bold",command=lambda:show("-"),bg="lavender",padx=25,pady=20,bd=5)
b11.grid(row=2,column=4)

b12=Button(root,text="*",font="Futura 35 bold",command=lambda:show("*"),bg="lavender",padx=25,pady=20,bd=5)
b12.grid(row=3,column=4)

b13=Button(root,text="=",font="Futura 35 bold",command=eql,padx=20,pady=20,bg="gray",bd=5)
b13.grid(row=5,column=2)

b14=Button(root,text=".",font="Futura 35 bold",command=lambda:show("."),bg="grey",padx=25,pady=20,bd=5)
b14.grid(row=5,column=3)

b15=Button(root,text="/",font="Futura 35 bold",command=lambda:show("/"),bg="lavender",padx=27,pady=20,bd=5)
b15.grid(row=4,column=4)

b16=Button(root,text="C",font="Futura 35 bold",command=clr,padx=20,pady=20,bg="gray",bd=5)
b16.grid(row=5,column=1)

b17=Button(root,text="0",font="Futura 35 bold",command=lambda:show("0"),bg="pink",padx=23,pady=20,bd=5)
b17.grid(row=4,column=1)

b18=Button(root,text="%",font="Futura 35 bold",command=lambda:show("%"),bg="lavender",padx=13,pady=20,bd=5)
b18.grid(row=5,column=4)

b19=Button(root,text="(",font="Futura 35 bold",command=lambda:show("("),bg="pink",padx=25,pady=20,bd=5)
b19.grid(row=4,column=2)

b20=Button(root,text=")",font="Futura 35 bold",command=lambda:show(")"),bg="pink",padx=25,pady=20,bd=5)
b20.grid(row=4,column=3)

root.mainloop()
    

