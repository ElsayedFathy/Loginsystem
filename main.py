from tkinter import *
sy = Tk()
#sy2 = Tk()
sy.geometry('940x500+200+100') #عرض + طول + مسافة من العرض + مسافة من فوق
#sy.lift() #أساسية النافذة
#sy2.iconify() #تصغير
#sy2.lower() #إخفاء النافذة
#sy2.state('normal')
#sy2.state('iconic') #حالة
#sy2.state('withdrawn')
sy.resizable( True, True) # عدم التحكم في حجم النافذة
sy.title('ABAN Improvment System')
#sy2.title('new')
sy.config(background='gray') #لون الخلفية
sy.iconbitmap('E:\\New Life\\Data analysis package\\python\\tips\\icon.ico') #أيقونة
#عمل فريم
fr1 = Frame(width='300',height='499',bg='white')
fr1.place(x=10,y=1)
fr2 = Frame(width='300',height='499',bg='white')
fr2.place(x=320,y=1)
fr3 = Frame(width='300',height='499',bg='white')
fr3.place(x=630,y=1)
#sy.minsize(500,500)
#sy.maxsize(1000,1000)
#الأزرار
#var = tool(master, option)
bt1 = Button(fr1,text='entry',fg='white',bg='gray',width='30',height='10')
bt1.place(x=100,y=100)
bt2 = Button(fr2,text='entry',fg='white',bg='gray',width='30',cursor='heart')
bt2.place(x=100,y=50)
#labels
lbl1 = Label(fr1,text='5S',fg='black',bg='white',font='100')
lbl1.place(x=100,y=50)
#entry
en1= Entry(fr1, justify='center')
en1.place(x=20,y=300)

en1= Entry(fr1, justify='right',fg='red',bg='black')
en1.place(x=20,y=400)


#الاختيارمن  المتعدد
from tkinter import ttk
combo1= ttk.Combobox(fr1, value=('sort','set in order'),state='readonly')
combo1.place(x=100,y=30)

combo2= ttk.Combobox(fr2, value=('shine','standard'),state='readonly')
combo2.place(x=100,y=30)

#قائمة بيانات
lst1 =Listbox(fr3)
lst1.insert(0,'one')
lst1.insert(1,'two')
lst1.insert(2,'three')
lst1.pack() #يظهر في المنتصف

#زر اختياري
r1 = ttk.Radiobutton(fr3,text='sort', value=1)
r1.pack()
r2 = ttk.Radiobutton(fr3,text='set in order', value=2)
r2.pack()
#اختيار متعدد
c1=Checkbutton(fr3, text='sort')
c1.pack()
c2=Checkbutton(fr3, text='set in order')
c2.pack()
c3=Checkbutton(fr3, text='shine')
c3.pack()

#زر متعدد الخيارات
men = Menubutton(fr3, text='improve',relief='groove')
men.pack()
ss=Menu(men)
men['menu'] =ss
ss.add_checkbutton(label='sort')
ss.add_checkbutton(label='set in order')

#قوائم البرنامج
menubar = Menu(sy)
f = Menu(menubar,tearoff=0)
f.add_command(label='new')
f.add_command(label='open')
f.add_command(label='Save')
f.add_command(label='Save as')
f.add_separator()
f.add_command(label='Exit',command=sy.quit)
menubar.add_cascade(label='file',menu=f)
sy.config(menu=menubar)
#العداد
sc1 = Scale(fr3, from_= 1, to=100, orient=HORIZONTAL)
sc1.pack()
sc2 = Scale(fr3, from_= 1, to=200, orient=VERTICAL)
sc2.pack()
#سكرول بار
scr1 = Scrollbar(sy, orient=VERTICAL)
scr1.pack(side=RIGHT,fill=Y)
scr2= Scrollbar(sy, orient=HORIZONTAL)
scr2.pack(side=BOTTOM,fill=X)
#نوت بوك
nb = ttk.Notebook(sy)
nb.pack()
f1 = Frame(nb,width='800',height='100')
nb.add(f1,text='Home')
lbl5=Label(f1,text='kaizen',bg='silver')
lbl5.pack()
f2 = Frame(nb,width='800',height='100')
nb.add(f2,text='Tools')
lbl6=Label(f2,text='ghy',bg='red')
lbl6.pack()
#عداد الأرقام
sp = Spinbox(fr3, from_=0,to=100,)
sp.pack()
sp1 = Spinbox(sy,from_=20,to=50)
sp1.pack()

#زر بخلفية صورة
photo = PhotoImage(file= r"E:\\New Life\\Data analysis package\\python\\tips\\s.png",width='100',height='200')
res =photo.subsample(2,2)
bt1 = Button(sy,text= '5s', image = res, compound=TOP)
bt1.pack()

sy.mainloop()
sy.mainloop()


