from tkinter import *
root=Tk()
root.title("simple calculator")
e= Entry(root,width=40, borderwidth=5)
e.grid(row=6,column=1,columnspan=3,padx=10,pady=10)

def button_click(number):
    current= e.get()
    e.delete(0,END)
    e.insert(0,str(current)+str(number))
    
def button_clear():
    e.delete(0,END)
def button_add():
     first_number= e.get()
     global f_num
     f=num=int(first_number)
     e.delete(0,END)
def button_equal():
    second_num=e.get()
    e.delete(0,END)
    e.insert(0,f_num+ int(second_num))



    
button_0=Button(root, text="0", padx=40, pady=20, command=lambda: button_click)
button_1=Button(root, text="1", padx=40, pady=20, command=lambda: button_click)
button_2=Button(root, text="2", padx=40, pady=20, command=lambda: button_click)
button_3=Button(root, text="3", padx=40, pady=20, command=lambda: button_click)
button_4=Button(root, text="4", padx=40, pady=20, command=lambda: button_click)
button_5=Button(root, text="5", padx=40, pady=20, command=lambda: button_click)
button_6=Button(root, text="6", padx=40, pady=20, command=lambda: button_click)
button_7=Button(root, text="7", padx=40, pady=20, command=lambda: button_click)
button_8=Button(root, text="8", padx=40, pady=20, command=lambda: button_click)
button_9=Button(root, text="9", padx=40, pady=20, command=lambda: button_click)
button_add= Button(root, text="+", padx=40, pady=20, command=button_add)
button_equal=Button(root, text="=", padx=40, pady=20, command=button_equal)
button_clear=Button(root, text="clear", padx=40, pady=18, command=button_clear)


button_0.grid(row=0 , column=0)
button_1.grid(row=0 , column=1)
button_2.grid(row=0 , column=2)
button_3.grid(row=1 , column=0)
button_4.grid(row=1 , column=1)
button_5.grid(row=1 , column=2)
button_6.grid(row=2 , column=0)
button_7.grid(row=2 , column=0)
button_8.grid(row=2 , column=1)
button_9.grid(row=2 , column=2)
button_add.grid(row=3, column=0)
button_equal.grid(row=3, column=1)
button_clear.grid(row=3, column=2)
root.mainloop()