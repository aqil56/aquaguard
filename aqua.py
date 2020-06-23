from tkinter import *
import guard


def get_selected(event):
    global selected
    index=list1.curselection()[0]
    selected=list1.get(index)
    e1.delete(0,END)
    e1.insert(END,selected[1])
    e2.delete(0,END)
    e2.insert(END,selected[2])
    e3.delete(0,END)
    e3.insert(END,selected[3])
    e4.delete(0,END)
    e4.insert(END,selected[4])
    e5.delete(0,END)
    e5.insert(END,selected[5])
    e6.delete(0,END)
    e6.insert(END,selected[6])
    e7.delete(0,END)
    e7.insert(END,selected[7])
    e8.delete(0,END)
    e8.insert(END,selected[8])
    e9.delete(0,END)
    e9.insert(END,selected[9])
    e10.delete(0,END)
    e10.insert(END,selected[10])
    e11.delete(0,END)
    e11.insert(END,selected[11])
    e12.delete(0,END)
    e12.insert(END,selected[12])

def view_c():
    list1.delete(0,END)
    for row in guard.view():
        list1.insert(END,row)

def search_c():
    list1.delete(0,END)
    for row in guard.search(fn_txt.get(),ln_txt.get(),st_txt.get(),citystate_txt.get(),zip_txt.get(),ph_txt.get(),rep_txt.get(),rs_txt.get(),status_txt.get(),sale_txt.get(),install_txt.get(),lead_txt.get()):
        list1.insert(END,row)

def add_c():
    guard.add(fn_txt.get(),ln_txt.get(),st_txt.get(),citystate_txt.get(),zip_txt.get(),ph_txt.get(),rep_txt.get(),rs_txt.get(),status_txt.get(),sale_txt.get(),install_txt.get(),lead_txt.get())
    list1.delete(0,END)
    list1.insert(fn_txt.get(),ln_txt.get(),st_txt.get(),citystate_txt.get(),zip_txt.get(),ph_txt.get(),rep_txt.get(),rs_txt.get(),status_txt.get(),sale_txt.get(),install_txt.get(),lead_txt.get())

def delete_c():
    guard.delete(selected[0])


def update_c():
    guard.update(selected[0],fn_txt.get(),ln_txt.get(),st_txt.get(),citystate_txt.get(),zip_txt.get(),ph_txt.get(),rep_txt.get(),rs_txt.get(),status_txt.get(),sale_txt.get(),install_txt.get(),lead_txt.get())










win=Tk()

win.wm_title("AQUAGUARD")

l1=Label(win,text="CUSTOMER INFO")
l1.grid(row=0,column=0,columnspan=2)

l2=Label(win,text="First Name")
l2.grid(row=1,column=0)

l3=Label(win,text="Last name")
l3.grid(row=1,column=1)

l4=Label(win,text="St address")
l4.grid(row=3,column=0,columnspan=2)

l5=Label(win,text="City, State")
l5.grid(row=5,column=0)

l6=Label(win,text="Zip")
l6.grid(row=5,column=1)

l7=Label(win,text="Phone Number")
l7.grid(row=7,column=0,columnspan=2)

l14=Label(win,text="COMPANY INFO")
l14.grid(row=0,column=2,columnspan=2)

l8=Label(win,text="Sales Rep")
l8.grid(row=1,column=2,columnspan=2)

l9=Label(win,text="Results")
l9.grid(row=3,column=2)

l10=Label(win,text="Status")
l10.grid(row=3,column=3)

l11=Label(win,text="Sale Date")
l11.grid(row=5,column=2)

l12=Label(win,text="Install Date")
l12.grid(row=5,column=3)

l13=Label(win,text="Lead Generator")
l13.grid(row=7,column=2,columnspan=2)

fn_txt=StringVar()
e1=Entry(win,textvariable=fn_txt)
e1.grid(row=2,column=0)

ln_txt=StringVar()
e2=Entry(win,textvariable=ln_txt)
e2.grid(row=2,column=1)

st_txt=StringVar()
e3=Entry(win,textvariable=st_txt)
e3.grid(row=4,column=0,columnspan=2)

citystate_txt=StringVar()
e4=Entry(win,textvariable=citystate_txt)
e4.grid(row=6,column=0)

zip_txt=StringVar()
e5=Entry(win,textvariable=zip_txt)
e5.grid(row=6,column=1)

ph_txt=StringVar()
e6=Entry(win,textvariable=ph_txt)
e6.grid(row=8,column=0,columnspan=2)

rep_txt=StringVar()
e7=Entry(win,textvariable=rep_txt)
e7.grid(row=2,column=2,columnspan=2)

rs_txt=StringVar()
e8=Entry(win,textvariable=rs_txt)
e8.grid(row=4,column=2)

status_txt=StringVar()
e9=Entry(win,textvariable=status_txt)
e9.grid(row=4,column=3)

sale_txt=StringVar()
e10=Entry(win,textvariable=sale_txt)
e10.grid(row=6,column=2)

install_txt=StringVar()
e11=Entry(win,textvariable=install_txt)
e11.grid(row=6,column=3)

lead_txt=StringVar()
e12=Entry(win,textvariable=lead_txt)
e12.grid(row=8,column=2,columnspan=2)

list1=Listbox(win,height=8,width=60)
list1.grid(row=9,column=0,rowspan=6,columnspan=2)

sb1=Scrollbar(win)
sb1.grid(row=9,column=2,rowspan=6)

sb2=Scrollbar(win, orient=HORIZONTAL)
sb2.grid(row=15,column=0,columnspan=2)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list1.configure(xscrollcommand=sb2.set)
sb2.configure(command=list1.xview)

list1.bind('<<ListboxSelector>>', get_selected)

b1=Button(win,text="View All",width=15,command=view_c)
b1.grid(row=9,column=3)

b2=Button(win,text="Add",width=15,command=add_c)
b2.grid(row=10,column=3)

b3=Button(win,text="Search",width=15,command=search_c)
b3.grid(row=11,column=3)

b4=Button(win,text="Update",width=15,command=update_c)
b4.grid(row=12,column=3)

b5=Button(win,text="Delete",width=15,command=delete_c)
b5.grid(row=13,column=3)

b6=Button(win,text="Close",width=15,command=win.destroy)
b6.grid(row=14,column=3)


win.mainloop()