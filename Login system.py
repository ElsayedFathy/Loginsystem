from tkinter import *
sy =Tk()
sy.title('LOGIN ABAN ')
sy.geometry('500x500')
sy.resizable(False,False)
sy.config(background='#ECF0F1')
sy.iconbitmap('E:\\New Life\\Data analysis package\\python\\tips\\log1.ico')
#Title
title = Label(sy,text='LOGIN ABAN', font=('Courier,15'),bg='#85929E',fg='white')
title.pack(fill=X)
#frame
fr1= Frame(sy,width='300',height='350',bg='#F7F9F9')
fr1.pack(pady=30)
#image
photo = PhotoImage(file="E:\\New Life\\Data analysis package\\python\\tips\\logo4.png")
res =photo.subsample(10,10)
panel = Label(sy, image=res)
panel.place(x=220,y=60)

sy.mainloop()
