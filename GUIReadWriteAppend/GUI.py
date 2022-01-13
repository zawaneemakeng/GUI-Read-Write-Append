from tkinter import *
from tkinter import messagebox
from tkinter import  ttk 
import time

named_tuple = time.localtime() 
time_string = time.strftime("%d/%m/%Y, %H:%M", named_tuple)

print(time_string)
gui = Tk() 
gui.title('My Note')
gui.geometry("600x400")

gui.configure(bg='#e6e5da') 
Font = ('Bahnschrift',16) 
Font2 = ('Bahnschrift',12)

def Clear():
	t_text.set('') 
	f_file.set('')

def File():
	text =  t_text.get() 
	file_p = f_file.get() 
	radio = r_radio.get() 
	if radio == 1 :
		f =  open(file_p,'r+',encoding='utf-8')
		f1 = f.read()
		print(f1)
		f.write(time_string+'\n')
		f.write('\t'+text+'\n')
		f.close()

	elif radio == 2:
		f =  open(file_p,'w',encoding='utf-8')
		f.write(time_string+'\n')
		f.write('\t'+text+'\n')
		f.close()

	else:
		f =  open(file_p,'a',encoding='utf-8')
		f.write(time_string+'\n')
		f.write('\t'+text+'\n')
		f.close()

	messagebox.showinfo('เเจ้งเตือน','\tต้องการบันทึกไฟล์ใช่ไหม\t')
	print('----บันทึกไฟล์สำเร็จ----')
	t_text.set('')
	f_file.set('')
	
 

t_text = StringVar() 
E1 = ttk.Entry(gui,textvariable=t_text,width=20,font=Font).place(x=280,y=30)
f_file = StringVar()
E2 = ttk.Entry(gui,textvariable=f_file,width=20,font=Font).place(x=280,y=80)

L1 = Label (gui,text=' Enter Text ',bg='#e6e5da',font=Font,fg='#663f0b').place(x=60,y=30)
L2 = Label (gui,text=' Enter File Name ',bg='#e6e5da',font=Font,fg='#663f0b').place(x=60,y=80)

r_radio = IntVar() 
R1 = Radiobutton(gui,text='อ่านไฟล์เเละเขียนไฟล์',variable=r_radio,value=1,bg='#e6e5da',font=Font,fg='#663f0b').place(x=270,y=140)
R2 = Radiobutton(gui,text='เขียนไฟล์',variable=r_radio,value=2,bg='#e6e5da',font=Font,fg='#663f0b').place(x=270,y=200)
R2 = Radiobutton(gui,text='ต่อท้ายไฟล์',variable=r_radio,value=3,bg='#e6e5da',font=Font,fg='#663f0b').place(x=270,y=260)

icon_b1 = PhotoImage(file='clear.png')
B1 = Button(gui,text=' Clear',width=100,image=icon_b1,bg='#66d8de',compound='left',font=Font2,fg='#663f0b',command=Clear).place(x=60,y=320)

icon_b2 = PhotoImage(file='ok.png')
B2 = Button(gui,text='   OK',width=100,image=icon_b2,bg='#66d8de',compound='left',font=Font2,fg='#663f0b',command=File).place(x=240,y=320)

icon_b3 = PhotoImage(file='cancle.png')
B3 = Button(gui,text=' Cancle ',width=100,image=icon_b3,bg='#66d8de',compound='left',font=Font2,fg='#663f0b',command=gui.destroy).place(x=430,y=320)

gui.mainloop()
