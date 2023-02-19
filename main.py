from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
from tkcalendar import DateEntry
from random import randint
from data import *

main = Tk()
icon =  PhotoImage(file ='mortarboard.png')
main.iconphoto(False, icon)
main.minsize(700,600)
main.maxsize(700,600)
can0 = Canvas(main, background='#537FE7', width=700, height=600)
can0.place(x=-2, y=0)
main.title('Intro')
btn = Button(main, text='GET STARTED', fg='#E9F8F9', bg='#181823', width=30, height=2, font='Arial 10 bold', relief=GROOVE, command=lambda: signIN())
btn.place(x=230, y=400)

image=Image.open('Grades-bro.png')
img=image.resize((300, 300))
my_img=ImageTk.PhotoImage(img)
label=Label(main, image=my_img, bg='#537FE7')
label.place(x=210, y=50)


def signIN():
   main.minsize(700,600)
   main.maxsize(700,600)
   main.title('Sign In')
   can = Canvas(main, background='#537FE7', width=700, height=600)
   can.place(x=-2, y=0)
   sign_lb = Label(main, text='Sign In', fg='#E9F8F9', bg='#537FE7', font='Arial 40 bold')
   sign_lb.place(x=260, y=50)

   email_lb = Label(main, text='Email', fg='#181823', bg='#537FE7', font='Arial 12 bold')
   email_lb.place(x=220, y=180)
   email_etr = Entry(main, width=19, highlightthickness=2, highlightcolor='black', justify= 'center', font='Arial 20 ')
   email_etr.place(x=200, y=210)


   pass_lb = Label(main, text='Password', fg='#181823', bg='#537FE7', font='Arial 12 bold')
   pass_lb.place(x=220, y=280)
   pass_etr = Entry(main, width=19, highlightthickness=2, highlightcolor='black', justify= 'center', font='Arial 20 ', show='*')
   pass_etr.place(x=200, y=310)

   log_btn = Button(main, text='Log In', fg='#E9F8F9', bg='#181823', width=40, height=2, relief=GROOVE, command=lambda: open0())
   log_btn.place(x=200, y=400)

   def open0():
      if (email_etr.get() == 'Admin') and (pass_etr.get() == 'admin'):
         messagebox.showinfo("Successfully", "Successfully")
         adm()
      else:
         for i in range(len(std_signIn())):
            if (email_etr.get() == std_signIn()[i][6]) and (pass_etr.get() == std_signIn()[i][7]):
               messagebox.showinfo("Successfully", "Successfully")
               id = std_signIn()[i][0]
               std(id)
               break
            
         for i in range(len(display_worker_1())):
            if (email_etr.get() == display_worker_1()[i][6]) and (pass_etr.get() == display_worker_1()[i][7]) and (display_worker_1()[i][8] == 'teacher'):
               messagebox.showinfo("Successfully", "Successfully")
               id = display_worker_1()[i][0]
               teacher_acc(id)
               break
               
         else:
            messagebox.showerror("Incorrect", "Incorrect")

# THIS IS FOR TEACHERS


def teacher_acc(id=0):
    main.minsize(700,600)
    main.maxsize(700,600)
    main.title('Teacher')
    can1 = Canvas(main, background='#E9F8F9', width=700, height=600)
    can1.place(x=0, y=0)
    fn = edit_worker(id)[0][1] + ' ' + edit_worker(id)[0][2]
    fullname = Label(main, text=fn, font='Arial 30 bold')
    fullname.place(x=100, y=50)
    cat_lb = Label(main, text='Categories', fg='#537FE7', bg='#E9F8F9', font='Arial 20 bold')
    cat_lb.place(x=290, y=200)

    info_btn = Button(main, text='Add Grades', fg='#181823', bg='#E9F8F9', width=30, height=2, relief=GROOVE, command=lambda: stdGrades_1(id))
    info_btn.place(x=250, y=300)
    deco_btn = Button(main, text='Log out', fg='#181823', bg='#E9F8F9', width=30, height=2, relief=GROOVE, command=lambda: signIN())
    deco_btn.place(x=250, y=350)


# THIS IS FOR STUDENTS
def std(id=0):
   main.minsize(700,600)
   main.maxsize(700,600)
   main.title('Student')
   can1 = Canvas(main, background='#E9F8F9', width=700, height=600)
   can1.place(x=0, y=0)
   fn = std_Info(id)[0][1] + ' ' + std_Info(id)[0][2]
   fullname = Label(main, text=fn, font='Arial 30 bold')
   fullname.place(x=100, y=50)
   cat_lb = Label(main, text='Categories', fg='#537FE7', bg='#E9F8F9', font='Arial 20 bold')
   cat_lb.place(x=290, y=150)

   info_btn = Button(main, text='My info', fg='#181823', bg='#E9F8F9', width=30, height=2, relief=GROOVE, command=lambda: info0(id))
   info_btn.place(x=250, y=200)
   note_btn = Button(main, text='Grades', fg='#181823', bg='#E9F8F9', width=30, height=2, relief=GROOVE, command=lambda: display_grade_For_STD(id))
   note_btn.place(x=250, y=250)
   settings_btn = Button(main, text='Settings', fg='#181823', bg='#E9F8F9', width=30, height=2, relief=GROOVE, command=lambda: notAvia(id))
   settings_btn.place(x=250, y=300)
   deco_btn = Button(main, text='Log out', fg='#181823', bg='#E9F8F9', width=30, height=2, relief=GROOVE, command=lambda: signIN())
   deco_btn.place(x=250, y=350)
   
   
def info0(id=0):
   main.minsize(700,600)
   main.maxsize(700,600)
   main.title('Student')
   can1 = Canvas(main, background='#E9F8F9', width=700, height=600)
   can1.place(x=0, y=0)

   info0 = Label(main, text="info", fg='red', font='Arial 11')
   info0.place(x=100, y=150)
   fn = std_Info(id)[0][1] + ' ' + std_Info(id)[0][2]
   fullname = Label(main, text=fn, font='Arial 30 bold')
   fullname.place(x=100, y=50)
   date = Label(main, text="Date of birth", font='Arial 15')
   date.place(x=100, y=200)
   date1 = Label(main, text=std_Info(id)[0][3], font='Arial 15')
   date1.place(x=300, y=200)
   born = Label(main, text="Born", font='Arial 15')
   born.place(x=100, y=250)
   born1 = Label(main, text=std_Info(id)[0][4], font='Arial 15')
   born1.place(x=300, y=250)
   address = Label(main, text="Address", font='Arial 15')
   address.place(x=100, y=300)
   address1 = Label(main, text=std_Info(id)[0][5], font='Arial 15')
   address1.place(x=300, y=300)
   level = Label(main, text="Level Acadimic", font='Arial 15')
   level.place(x=100, y=350)
   level1 = Label(main, text=std_Info(id)[0][8], font='Arial 15')
   level1.place(x=300, y=350)
   grp = Label(main, text="Group", font='Arial 15')
   grp.place(x=100, y=400)
   grp1 = Label(main, text=std_Info(id)[0][9], font='Arial 15')
   grp1.place(x=300, y=400)
   back_btn = Button(main, text='Back', fg='#181823', bg='#E9F8F9', width=30, height=2, relief=GROOVE, command=lambda: std(id))
   back_btn.place(x=250, y=490)

def notAvia(id):
   main.minsize(700,600)
   main.maxsize(700,600)
   main.title('NOT AVAILABLE')
   can1 = Canvas(main, background='#E9F8F9', width=700, height=600)
   can1.place(x=0, y=0)
   not0 = Label(main, text="This page isn't available now", font='Arial 30 bold')
   not0.place(x=100, y=200)
   back_btn = Button(main, text='Back', fg='#181823', bg='#E9F8F9', width=30, height=2, relief=GROOVE, command=lambda: std(id))
   back_btn.place(x=250, y=490)

def display_grade_For_STD(id):
    main.minsize(700,600)
    main.maxsize(700,600)
    can0 = Canvas(main, background='#E9F8F9', width=700, height=600)
    can0.place(x=0, y=0)
    main.title('Display - grade')
    full = std_Info(id)[0][1] + ' ' + std_Info(id)[0][2]
    full_lb = Label(main, text=full, fg='#537FE7', bg='#E9F8F9', font='Arial 20 bold')
    full_lb.place(x=205, y=10)

    n_lb = Label(main, text='N1', fg='#537FE7', bg='#E9F8F9', font='Arial 10 italic')
    n_lb.place(x=210, y=90)
    n_lb = Label(main, text='N2', fg='#537FE7', bg='#E9F8F9', font='Arial 10 italic')
    n_lb.place(x=280, y=90)
    n_lb = Label(main, text='N3', fg='#537FE7', bg='#E9F8F9', font='Arial 10 italic')
    n_lb.place(x=350, y=90)
    n_lb = Label(main, text='N4', fg='#537FE7', bg='#E9F8F9', font='Arial 10 italic')
    n_lb.place(x=420, y=90)
    n_lb = Label(main, text='N5', fg='#537FE7', bg='#E9F8F9', font='Arial 10 italic')
    n_lb.place(x=500, y=90)
    #math
    can_math = Canvas(main, background='red', width=500, height=20)
    can_math.place(x=170, y=120)
    math_lb = Label(main, text='Math', fg='#537FE7', bg='#E9F8F9', font='Arial 12 italic')
    math_lb.place(x=50, y=120)
    for i in range(len(display_math(id))):
        for j in range(1,6):# widith 13
            e = Entry(can_math, width=13, font=('Arial',8))
            e.grid(row=i, column=j)
            e.insert(END, display_math(id)[i][j])

    #pc
    can_pc = Canvas(main, background='red', width=500, height=20)
    can_pc.place(x=170, y=160)
    math_lb = Label(main, text='pc', fg='#537FE7', bg='#E9F8F9', font='Arial 12 italic')
    math_lb.place(x=50, y=160)
    for i in range(len(display_pc(id))):
        for j in range(1,6):# widith 13
            e = Entry(can_pc, width=13, font=('Arial',8))
            e.grid(row=i, column=j)
            e.insert(END, display_pc(id)[i][j])

    #svt
    can_svt = Canvas(main, background='red', width=500, height=20)
    can_svt.place(x=170, y=200)
    math_lb = Label(main, text='Svt', fg='#537FE7', bg='#E9F8F9', font='Arial 12 italic')
    math_lb.place(x=50, y=200)
    for i in range(len(display_svt(id))):
        for j in range(1,6):# widith 13
            e = Entry(can_svt, width=13, font=('Arial',8))
            e.grid(row=i, column=j)
            e.insert(END, display_svt(id)[i][j])

    #arabic
    can_arabic = Canvas(main, background='red', width=500, height=20)
    can_arabic.place(x=170, y=240)
    math_lb = Label(main, text='Arabic', fg='#537FE7', bg='#E9F8F9', font='Arial 12 italic')
    math_lb.place(x=50, y=240)
    for i in range(len(display_arabic(id))):
        for j in range(1,6):# widith 13
            e = Entry(can_arabic, width=13, font=('Arial',8))
            e.grid(row=i, column=j)
            e.insert(END, display_arabic(id)[i][j])

    #islamic
    can_islamic = Canvas(main, background='red', width=500, height=20)
    can_islamic.place(x=170, y=280)
    math_lb = Label(main, text='Islamic edu', fg='#537FE7', bg='#E9F8F9', font='Arial 12 italic')
    math_lb.place(x=50, y=280)
    for i in range(len(display_islamic(id))):
        for j in range(1,6):# widith 13
            e = Entry(can_islamic, width=13, font=('Arial',8))
            e.grid(row=i, column=j)
            e.insert(END, display_islamic(id)[i][j])

    #english
    can_english = Canvas(main, background='red', width=500, height=20)
    can_english.place(x=170, y=320)
    math_lb = Label(main, text='English', fg='#537FE7', bg='#E9F8F9', font='Arial 12 italic')
    math_lb.place(x=50, y=320)
    for i in range(len(display_english(id))):
        for j in range(1,6):# widith 13
            e = Entry(can_english, width=13, font=('Arial',8))
            e.grid(row=i, column=j)
            e.insert(END, display_english(id)[i][j])

    #french
    can_french = Canvas(main, background='red', width=500, height=20)
    can_french.place(x=170, y=360)
    math_lb = Label(main, text='French', fg='#537FE7', bg='#E9F8F9', font='Arial 12 italic')
    math_lb.place(x=50, y=360)
    for i in range(len(display_french(id))):
        for j in range(1,6):# widith 13
            e = Entry(can_french, width=13, font=('Arial',8))
            e.grid(row=i, column=j)
            e.insert(END, display_french(id)[i][j])

    #Philosophy
    can_philo = Canvas(main, background='red', width=500, height=20)
    can_philo.place(x=170, y=400)
    math_lb = Label(main, text='Philosophy', fg='#537FE7', bg='#E9F8F9', font='Arial 12 italic')
    math_lb.place(x=50, y=400)
    for i in range(len(display_philosophy(id))):
        for j in range(1,6):# widith 13
            e = Entry(can_philo, width=13, font=('Arial',8))
            e.grid(row=i, column=j)
            e.insert(END, display_philosophy(id)[i][j])

    #sport
    can_sport = Canvas(main, background='red', width=500, height=20)
    can_sport.place(x=170, y=440)
    math_lb = Label(main, text='Sport edu', fg='#537FE7', bg='#E9F8F9', font='Arial 12 italic')
    math_lb.place(x=50, y=440)
    for i in range(len(display_sport(id))):
        for j in range(1,6):# widith 13
            e = Entry(can_sport, width=13, font=('Arial',8))
            e.grid(row=i, column=j)
            e.insert(END, display_sport(id)[i][j])

    #Diligence
    can_dab = Canvas(main, background='red', width=500, height=20)
    can_dab.place(x=170, y=480)
    math_lb = Label(main, text='Diligence \nand \nBehaviour', fg='#537FE7', bg='#E9F8F9', font='Arial 12 italic')
    math_lb.place(x=50, y=480)
    for i in range(len(display_dab(id))):
        for j in range(1,6):# widith 13
            e = Entry(can_dab, width=13, font=('Arial',8))
            e.grid(row=i, column=j)
            e.insert(END, display_dab(id)[i][j])

    back_btn = Button(main, text='Back', fg='black', bg='#E9F8F9', width=20, height=2, relief=GROOVE, command=lambda: std(id))
    back_btn.place(x=300, y=530)


# THIS IS FOR Administration
def adm():
   main.minsize(700,600)
   main.maxsize(700,600)
   main.title('Administration')
   can1 = Canvas(main, background='#E9F8F9', width=700, height=600)
   can1.place(x=0, y=0)

   cat_lb = Label(main, text='Categories', fg='#537FE7', bg='#E9F8F9', font='Arial 20 bold')
   cat_lb.place(x=290, y=150)

   display_btn = Button(main, text='Display', fg='#181823', bg='#E9F8F9', width=30, height=2, relief=GROOVE, command=lambda: display_all1())
   display_btn.place(x=250, y=200)
   add_btn = Button(main, text='Add', fg='#181823', bg='#E9F8F9', width=30, height=2, relief=GROOVE, command=lambda: display2())
   add_btn.place(x=250, y=250)
   edit_btn = Button(main, text='Edit', fg='#181823', bg='#E9F8F9', width=30, height=2, relief=GROOVE, command=lambda: into_edit())
   edit_btn.place(x=250, y=300)
   remove_btn = Button(main, text='Remove', fg='#181823', bg='#E9F8F9', width=30, height=2, relief=GROOVE, command=lambda: into_remove())
   remove_btn.place(x=250, y=350)
   settings_btn = Button(main, text='Settings', fg='#181823', bg='#E9F8F9', width=30, height=2, relief=GROOVE, command=lambda: settings())
   settings_btn.place(x=250, y=400)
   deco_btn = Button(main, text='Log out', fg='#181823', bg='#E9F8F9', width=30, height=2, relief=GROOVE, command=lambda: signIN())
   deco_btn.place(x=250, y=450)


def display():
   main.minsize(700,600)
   main.maxsize(700,600)
   main.title('Display - Student')
   can1 = Canvas(main, background='#E9F8F9', width=700, height=600)
   can1.place(x=0, y=0)
   display_lb = Label(main, text='Display', fg='#537FE7', bg='#E9F8F9', font='Arial 10 italic')
   display_lb.place(x=350, y=10)

   level_lb = Label(main, text='Level', fg='#537FE7', bg='#E9F8F9', font='Arial 20 bold')
   level_lb.place(x=320, y=150)
   tcs_btn = Button(main, text='TCS', fg='#181823', bg='#E9F8F9', width=30, height=2, relief=GROOVE, command=lambda: tcs())
   tcs_btn.place(x=250, y=200)
   bac1_btn = Button(main, text='1BAC', fg='#181823', bg='#E9F8F9', width=30, height=2, relief=GROOVE, command=lambda: bac1())
   bac1_btn.place(x=250, y=250)
   bac2_btn = Button(main, text='2BAC', fg='#181823', bg='#E9F8F9', width=30, height=2, relief=GROOVE, command=lambda: bac2())
   bac2_btn.place(x=250, y=300)
   back_btn = Button(main, text='Back', fg='#181823', bg='#E9F8F9', width=30, height=2, relief=GROOVE, command=lambda: display_all1())
   back_btn.place(x=250, y=350)


def add():
   main.minsize(700,600)
   main.maxsize(700,600)
   main.title('Add Student')
   can1 = Canvas(main, background='#E9F8F9', width=700, height=600)
   can1.place(x=0, y=0)

   back_btn = Button(main, text='Back', relief=GROOVE, command=lambda: display2())
   back_btn.place(x=650, y=10)

   code_lb = Label(main, text='Code', fg='#537FE7', bg='#E9F8F9', font='Arial 12 italic')
   code_lb.place(x=100, y=50)
   code_etr = Entry(main, width=20, font='Arial 15 ')
   code_etr.place(x=300, y=50)
   #-----
   l = []
   for i in std_signIn():
      l.append(i[0])

   while True :
      ra = 's' + str(randint(1111,99999))
      if ra not in l:
         code_etr.insert(END, ra)
         break
      else:
         continue
      #-----

   fname_lb = Label(main, text='First name', fg='#537FE7', bg='#E9F8F9', font='Arial 12 italic')
   fname_lb.place(x=100, y=100)
   fname_etr = Entry(main, width=20, font='Arial 15 ')
   fname_etr.place(x=300, y=100)

   lname_lb = Label(main, text='Last name', fg='#537FE7', bg='#E9F8F9', font='Arial 12 italic')
   lname_lb.place(x=100, y=150)
   lname_etr = Entry(main, width=20, font='Arial 15 ')
   lname_etr.place(x=300, y=150)

   date_lb = Label(main, text='Date of birth', fg='#537FE7', bg='#E9F8F9', font='Arial 12 italic')
   date_lb.place(x=100, y=200)
   date_etr=DateEntry(main ,selectmode='day', date_pattern='MM-dd-yyyy', width=18, font='Arial 15 ')
   date_etr.place(x=300, y=200)

   born_lb = Label(main, text='Born', fg='#537FE7', bg='#E9F8F9', font='Arial 12 italic')
   born_lb.place(x=100, y=250)
   born_etr = Entry(main, width=20, font='Arial 15 ')
   born_etr.place(x=300, y=250)

   address_lb = Label(main, text='Address', fg='#537FE7', bg='#E9F8F9', font='Arial 12 italic')
   address_lb.place(x=100, y=300)
   address_etr = Entry(main, width=20, font='Arial 15 ')
   address_etr.place(x=300, y=300)
   
   email_lb = Label(main, text='Email', fg='#537FE7', bg='#E9F8F9', font='Arial 12 italic')
   email_lb.place(x=100, y=350)
   email_etr = Entry(main, width=20, font='Arial 15 ')
   email_etr.place(x=300, y=350)
   email_etr.insert(END, code_etr.get())

   pass_lb = Label(main, text='Password', fg='#537FE7', bg='#E9F8F9', font='Arial 12 italic')
   pass_lb.place(x=100, y=400)
   pass_etr = Entry(main, width=20, font='Arial 15 ')
   pass_etr.place(x=300, y=400)
   pass_etr.insert(END, '123456')

   level_lb = Label(main, text='Level', fg='#537FE7', bg='#E9F8F9', font='Arial 12 italic')
   level_lb.place(x=100, y=450)
   le_el = ['tcs', '1bac', '2bac']
   g_p = ['1','2','3','4']

   level_etr = ttk.Combobox(main, width=18, justify='center', values=le_el, font='Arial 15')
   level_etr.set('tcs')
   level_etr.place(x=300, y=450)

   grp_lb = Label(main, text='Group', fg='#537FE7', bg='#E9F8F9', font='Arial 12 italic')
   grp_lb.place(x=100, y=500)
   grp_etr = ttk.Combobox(main, width=18, justify='center', values=g_p, font='Arial 15')
   grp_etr.set('1')
   grp_etr.place(x=300, y=500)

   add_btn = Button(main, text='Valid', fg='white', bg='green', width=31, height=2, relief=GROOVE, command=lambda: db())
   add_btn.place(x=300, y=550)

   def db():
      g1 = code_etr.get()
      g2 = fname_etr.get()
      g3 = lname_etr.get()
      g4 = date_etr.get()
      g5 = born_etr.get()
      g6 = address_etr.get()
      g7 = email_etr.get()
      g8 = pass_etr.get()
      g9 = level_etr.get()
      g10 = grp_etr.get()
      
      if (g1 != '') and (g2 != '') and (g3 != '') and (g4 != '') and (g5 != '') and (g6 != '') and (g7 != '') and (g8 != '') and (g9 != '') and (g10 != ''): 
         messagebox.showinfo("Successfully", "Successfully")
         add_std(g1, g2, g3, g4, g5, g6, g7, g8, g9, g10)
      else:
         messagebox.showerror("Error", "Error")


def edit():
   main.minsize(700,600)
   main.maxsize(700,600)
   main.title('Edit Student')
   can1 = Canvas(main, background='#E9F8F9', width=700, height=600)
   can1.place(x=0, y=0)
   edit_lb = Label(main, text='Edit', fg='#537FE7', bg='#E9F8F9', font='Arial 10 italic')
   edit_lb.place(x=350, y=10)

   back_btn = Button(main, text='Back', relief=GROOVE, command=lambda: into_edit())
   back_btn.place(x=650, y=10)

   code_lb = Label(main, text='Code', fg='#537FE7', bg='#E9F8F9', font='Arial 12 italic')
   code_lb.place(x=100, y=50)
   code_etr_edit = Entry(main, width=20, font='Arial 15 ')
   code_etr_edit.place(x=300, y=50)

   fname_lb = Label(main, text='First name', fg='#537FE7', bg='#E9F8F9', font='Arial 12 italic')
   fname_lb.place(x=100, y=100)
   fname_etr_edit = Entry(main, width=20, font='Arial 15 ')
   fname_etr_edit.place(x=300, y=100)
   
   lname_lb = Label(main, text='Last name', fg='#537FE7', bg='#E9F8F9', font='Arial 12 italic')
   lname_lb.place(x=100, y=150)
   lname_etr_edit = Entry(main, width=20, font='Arial 15 ')
   lname_etr_edit.place(x=300, y=150)

   date_lb = Label(main, text='Date of birth', fg='#537FE7', bg='#E9F8F9', font='Arial 12 italic')
   date_lb.place(x=100, y=200)
   date_etr_edit = Entry(main, width=20, font='Arial 15 ')
   date_etr_edit.place(x=300, y=200)

   born_lb = Label(main, text='Born', fg='#537FE7', bg='#E9F8F9', font='Arial 12 italic')
   born_lb.place(x=100, y=250)
   born_etr_edit = Entry(main, width=20, font='Arial 15 ')
   born_etr_edit.place(x=300, y=250)

   address_lb = Label(main, text='Address', fg='#537FE7', bg='#E9F8F9', font='Arial 12 italic')
   address_lb.place(x=100, y=300)
   address_etr_edit = Entry(main, width=20, font='Arial 15 ')
   address_etr_edit.place(x=300, y=300)
   
   email_lb = Label(main, text='Email', fg='#537FE7', bg='#E9F8F9', font='Arial 12 italic')
   email_lb.place(x=100, y=350)
   email_etr_edit = Entry(main, width=20, font='Arial 15 ')
   email_etr_edit.place(x=300, y=350)

   pass_lb = Label(main, text='Password', fg='#537FE7', bg='#E9F8F9', font='Arial 12 italic')
   pass_lb.place(x=100, y=400)
   pass_etr_edit = Entry(main, width=20, font='Arial 15 ')
   pass_etr_edit.place(x=300, y=400)

   level_lb = Label(main, text='Level', fg='#537FE7', bg='#E9F8F9', font='Arial 12 italic')
   level_lb.place(x=100, y=450)
   le_el = ['tcs', '1bac', '2bac']
   g_p = ['1','2','3','4']

   level_etr = ttk.Combobox(main, width=18, justify='center', values=le_el, font='Arial 15')
   level_etr.set('tcs')
   level_etr.place(x=300, y=450)

   grp_lb = Label(main, text='Group', fg='#537FE7', bg='#E9F8F9', font='Arial 12 italic')
   grp_lb.place(x=100, y=500)
   grp_etr = ttk.Combobox(main, width=18, justify='center', values=g_p, font='Arial 15')
   grp_etr.set('1')
   grp_etr.place(x=300, y=500)


   add_btn = Button(main, text='Search', bg='#E9F8F9', width=14, height=2, relief=GROOVE, command=lambda: get_code())
   add_btn.place(x=300, y=550)
   add_btn_edit = Button(main, text='Valid', fg='white', bg='#537FE7', width=14, height=2, relief=GROOVE, command=lambda: edit_info())
   add_btn_edit.place(x=417, y=550)

   def get_code():
      id = code_etr_edit.get()
      display_edit(id)
      level_etr.set('')
      grp_etr.set('')
      fname_etr_edit.insert(END, display_edit(id)[0][1])
      lname_etr_edit.insert(END, display_edit(id)[0][2])
      date_etr_edit.insert(END, display_edit(id)[0][3])
      born_etr_edit.insert(END, display_edit(id)[0][4])
      address_etr_edit.insert(END, display_edit(id)[0][5])
      email_etr_edit.insert(END, display_edit(id)[0][6])
      pass_etr_edit.insert(END, display_edit(id)[0][7])
      level_etr.insert(END, display_edit(id)[0][8])
      grp_etr.insert(END, display_edit(id)[0][9])
   
   def edit_info():
      d0 = code_etr_edit.get()
      d1 = fname_etr_edit.get()
      d2 = lname_etr_edit.get()
      d3 = date_etr_edit.get()
      d4 = born_etr_edit.get()
      d5 = address_etr_edit.get()
      d6 = email_etr_edit.get()
      d7 = pass_etr_edit.get()
      d8 = level_etr.get()
      d9 = grp_etr.get()
      if (d1 != '') and (d2 != '') and (d3 != '') and (d4 != '') and (d5 != '') and (d6 != '') and (d7 != '') and (d8 != '') and (d9 != ''):
         messagebox.showinfo("Successfully", "Successfully")
         edit_std(d1, d2, d3, d4, d5, d6, d7, d8, d9, d0)
      else:
         messagebox.showerror("Error", "Error")
 

def remove():
   main.minsize(700,600)
   main.maxsize(700,600)
   main.title('Remove - Student')
   can1 = Canvas(main, background='#E9F8F9', width=700, height=600)
   can1.place(x=0, y=0)
   remove_lb = Label(main, text='Remove', fg='#537FE7', bg='#E9F8F9', font='Arial 10 italic')
   remove_lb.place(x=350, y=10)

   back_btn = Button(main, text='Back', relief=GROOVE, command=lambda: into_remove())
   back_btn.place(x=650, y=10)

   code_lb = Label(main, text='Code', fg='#537FE7', bg='#E9F8F9', font='Arial 12 italic')
   code_lb.place(x=100, y=50)
   code_etr = Entry(main, width=20, font='Arial 15 ')
   code_etr.place(x=300, y=50)

   fname_lb = Label(main, text='First name', fg='#537FE7', bg='#E9F8F9', font='Arial 12 italic')
   fname_lb.place(x=100, y=100)
   fname_etr = Entry(main, width=20, font='Arial 15 ')
   fname_etr.place(x=300, y=100)

   lname_lb = Label(main, text='Last name', fg='#537FE7', bg='#E9F8F9', font='Arial 12 italic')
   lname_lb.place(x=100, y=150)
   lname_etr = Entry(main, width=20, font='Arial 15 ')
   lname_etr.place(x=300, y=150)

   date_lb = Label(main, text='Date of birth', fg='#537FE7', bg='#E9F8F9', font='Arial 12 italic')
   date_lb.place(x=100, y=200)
   date_etr = Entry(main, width=20, font='Arial 15 ')
   date_etr.place(x=300, y=200)

   born_lb = Label(main, text='Born', fg='#537FE7', bg='#E9F8F9', font='Arial 12 italic')
   born_lb.place(x=100, y=250)
   born_etr = Entry(main, width=20, font='Arial 15 ')
   born_etr.place(x=300, y=250)

   address_lb = Label(main, text='Address', fg='#537FE7', bg='#E9F8F9', font='Arial 12 italic')
   address_lb.place(x=100, y=300)
   address_etr = Entry(main, width=20, font='Arial 15 ')
   address_etr.place(x=300, y=300)
   
   email_lb = Label(main, text='Email', fg='#537FE7', bg='#E9F8F9', font='Arial 12 italic')
   email_lb.place(x=100, y=350)
   email_etr = Entry(main, width=20, font='Arial 15 ')
   email_etr.place(x=300, y=350)

   pass_lb = Label(main, text='Password', fg='#537FE7', bg='#E9F8F9', font='Arial 12 italic')
   pass_lb.place(x=100, y=400)
   pass_etr = Entry(main, width=20, font='Arial 15 ')
   pass_etr.place(x=300, y=400)

   level_lb = Label(main, text='Level', fg='#537FE7', bg='#E9F8F9', font='Arial 12 italic')
   level_lb.place(x=100, y=450)
   level_etr = Entry(main, width=20, font='Arial 15 ')
   level_etr.place(x=300, y=450)

   grp_lb = Label(main, text='Group', fg='#537FE7', bg='#E9F8F9', font='Arial 12 italic')
   grp_lb.place(x=100, y=500)
   grp_etr = Entry(main, width=20, font='Arial 15 ')
   grp_etr.place(x=300, y=500)

   add_btn = Button(main, text='Search', bg='#E9F8F9', width=14, height=2, relief=GROOVE, command=lambda: get_code())
   add_btn.place(x=300, y=550)
   add_btn = Button(main, text='Valid', fg='white', bg='red', width=14, height=2, relief=GROOVE, command=lambda: delete_info())
   add_btn.place(x=417, y=550)

   def get_code():
      id = code_etr.get()
      display_edit(id)
      fname_etr.insert(END, display_edit(id)[0][1])
      lname_etr.insert(END, display_edit(id)[0][2])
      date_etr.insert(END, display_edit(id)[0][3])
      born_etr.insert(END, display_edit(id)[0][4])
      address_etr.insert(END, display_edit(id)[0][5])
      email_etr.insert(END, display_edit(id)[0][6])
      pass_etr.insert(END, display_edit(id)[0][7])
      level_etr.insert(END, display_edit(id)[0][8])
      grp_etr.insert(END, display_edit(id)[0][9])

   def delete_info():
      id = code_etr.get()
      delete_std(id)
      reomve_math(id)
      reomve_pc(id)
      reomve_svt(id)
      reomve_arabic(id)
      reomve_islamic(id)
      reomve_english(id)
      reomve_french(id)
      reomve_philosophy(id)
      reomve_sport(id)
      reomve_dab(id)

      messagebox.showinfo('Successfully','Successfully')


def settings():
   main.minsize(700,600)
   main.maxsize(700,600)
   main.title('Administration')
   can1 = Canvas(main, background='#E9F8F9', width=700, height=600)
   can1.place(x=0, y=0)

   setting_lb = Label(main, text='Settings', fg='#537FE7', bg='#E9F8F9', font='Arial 20 bold')
   setting_lb.place(x=300, y=150)
   change_email_btn = Button(main, text='Change email', fg='#181823', bg='#E9F8F9', width=30, height=2, relief=GROOVE, command=lambda: notAvai())
   change_email_btn.place(x=250, y=200)
   change_pass_btn = Button(main, text='Change password', fg='#181823', bg='#E9F8F9', width=30, height=2, relief=GROOVE, command=lambda: notAvai())
   change_pass_btn.place(x=250, y=250)
   back_btn = Button(main, text='Back', fg='#181823', bg='#E9F8F9', width=30, height=2, relief=GROOVE, command=lambda: adm())
   back_btn.place(x=250, y=300)


def tcs():
   main.minsize(700,600)
   main.maxsize(700,600)
   main.title('Administration')
   can1 = Canvas(main, background='#E9F8F9', width=700, height=600)
   can1.place(x=0, y=0)
   display_lb = Label(main, text='TCS', fg='#537FE7', bg='#E9F8F9', font='Arial 10 italic')
   display_lb.place(x=350, y=10)

   level_lb = Label(main, text='Group', fg='#537FE7', bg='#E9F8F9', font='Arial 20 bold')
   level_lb.place(x=320, y=150)
   tcs_btn = Button(main, text='1', fg='#181823', bg='#E9F8F9', width=30, height=2, relief=GROOVE, command=lambda: tcs_1())
   tcs_btn.place(x=250, y=200)
   bac1_btn = Button(main, text='2', fg='#181823', bg='#E9F8F9', width=30, height=2, relief=GROOVE, command=lambda: tcs_2())
   bac1_btn.place(x=250, y=250)
   bac2_btn = Button(main, text='3', fg='#181823', bg='#E9F8F9', width=30, height=2, relief=GROOVE, command=lambda: tcs_3())
   bac2_btn.place(x=250, y=300)
   bac2_btn = Button(main, text='4', fg='#181823', bg='#E9F8F9', width=30, height=2, relief=GROOVE, command=lambda: tcs_4())
   bac2_btn.place(x=250, y=350)
   back_btn = Button(main, text='Back', fg='#181823', bg='#E9F8F9', width=30, height=2, relief=GROOVE, command=lambda: display())
   back_btn.place(x=250, y=400)


def bac1():
   main.minsize(700,600)
   main.maxsize(700,600)
   main.title('Administration')
   can1 = Canvas(main, background='#E9F8F9', width=700, height=600)
   can1.place(x=0, y=0)
   display_lb = Label(main, text='1BAC', fg='#537FE7', bg='#E9F8F9', font='Arial 10 italic')
   display_lb.place(x=350, y=10)

   level_lb = Label(main, text='Group', fg='#537FE7', bg='#E9F8F9', font='Arial 20 bold')
   level_lb.place(x=320, y=150)
   tcs_btn = Button(main, text='1', fg='#181823', bg='#E9F8F9', width=30, height=2, relief=GROOVE, command=lambda: bac1_1())
   tcs_btn.place(x=250, y=200)
   bac1_btn = Button(main, text='2', fg='#181823', bg='#E9F8F9', width=30, height=2, relief=GROOVE, command=lambda: bac1_2())
   bac1_btn.place(x=250, y=250)
   bac2_btn = Button(main, text='3', fg='#181823', bg='#E9F8F9', width=30, height=2, relief=GROOVE, command=lambda: bac1_3())
   bac2_btn.place(x=250, y=300)
   bac2_btn = Button(main, text='4', fg='#181823', bg='#E9F8F9', width=30, height=2, relief=GROOVE, command=lambda: bac1_4())
   bac2_btn.place(x=250, y=350)
   back_btn = Button(main, text='Back', fg='#181823', bg='#E9F8F9', width=30, height=2, relief=GROOVE, command=lambda: display())
   back_btn.place(x=250, y=400)


def bac2():
   main.minsize(700,600)
   main.maxsize(700,600)
   main.title('Administration')
   can1 = Canvas(main, background='#E9F8F9', width=700, height=600)
   can1.place(x=0, y=0)
   display_lb = Label(main, text='2BAC', fg='#537FE7', bg='#E9F8F9', font='Arial 10 italic')
   display_lb.place(x=350, y=10)

   level_lb = Label(main, text='Group', fg='#537FE7', bg='#E9F8F9', font='Arial 20 bold')
   level_lb.place(x=320, y=150)
   tcs_btn = Button(main, text='1', fg='#181823', bg='#E9F8F9', width=30, height=2, relief=GROOVE, command=lambda: bac2_1())
   tcs_btn.place(x=250, y=200)
   bac1_btn = Button(main, text='2', fg='#181823', bg='#E9F8F9', width=30, height=2, relief=GROOVE, command=lambda: bac2_2())
   bac1_btn.place(x=250, y=250)
   bac2_btn = Button(main, text='3', fg='#181823', bg='#E9F8F9', width=30, height=2, relief=GROOVE, command=lambda: bac2_3())
   bac2_btn.place(x=250, y=300)
   bac2_btn = Button(main, text='4', fg='#181823', bg='#E9F8F9', width=30, height=2, relief=GROOVE, command=lambda: bac2_4())
   bac2_btn.place(x=250, y=350)
   back_btn = Button(main, text='Back', fg='#181823', bg='#E9F8F9', width=30, height=2, relief=GROOVE, command=lambda: display())
   back_btn.place(x=250, y=400)


def tcs_1():
   main.minsize(700,600)
   main.maxsize(700,600)
   main.title('Administration')
   can1 = Canvas(main, background='#E9F8F9', width=700, height=600)
   can1.place(x=0, y=0)
   can2 = Canvas(main, width=700, height=600)
   can2.place(x=-1, y=90)

   for i in range(len(display_std('tcs', '1'))):
      for j in range(8):
         e = Entry(can2, width=15, font=('Arial',8))
         e.grid(row=i, column=j)
         e.insert(END, display_std('tcs', '1')[i][j])

   display_lb = Label(main, text='TCS - 1', fg='#537FE7', bg='#E9F8F9', font='Arial 10 italic')
   display_lb.place(x=350, y=10)
   back_btn = Button(main, text='Back', fg='#181823', bg='#E9F8F9', width=5, height=1, relief=GROOVE, command=lambda: tcs())
   back_btn.place(x=640, y=10)

   code_lb = Label(main, text='Code', fg='#181823', bg='#E9F8F9', font='Arial 10 bold')
   code_lb.place(x=20, y=60)
   fname_lb = Label(main, text='First name', fg='#181823', bg='#E9F8F9', font='Arial 10 bold')
   fname_lb.place(x=80, y=60)
   lname_lb = Label(main, text='Last name', fg='#181823', bg='#E9F8F9', font='Arial 10 bold')
   lname_lb.place(x=170, y=60)
   date_lb = Label(main, text='Date of birth', fg='#181823', bg='#E9F8F9', font='Arial 10 bold')
   date_lb.place(x=260, y=60)
   born_lb = Label(main, text='Born', fg='#181823', bg='#E9F8F9', font='Arial 10 bold')
   born_lb.place(x=360, y=60)
   address_lb = Label(main, text='Address', fg='#181823', bg='#E9F8F9', font='Arial 10 bold')
   address_lb.place(x=430, y=60)
   email_lb = Label(main, text='Email', fg='#181823', bg='#E9F8F9', font='Arial 10 bold')
   email_lb.place(x=550, y=60)
   pass_lb = Label(main, text='Password', fg='#181823', bg='#E9F8F9', font='Arial 10 bold')
   pass_lb.place(x=620, y=60)


def tcs_2():
   main.minsize(700,600)
   main.maxsize(700,600)
   main.title('Administration')
   can1 = Canvas(main, background='#E9F8F9', width=700, height=600)
   can1.place(x=0, y=0)
   can2 = Canvas(main, width=700, height=600)
   can2.place(x=-1, y=90)

   for i in range(len(display_std('tcs', '2'))):
      for j in range(8):
         e = Entry(can2, width=15, font=('Arial',8))
         e.grid(row=i, column=j)
         e.insert(END, display_std('tcs', '2')[i][j])

   display_lb = Label(main, text='TCS - 2', fg='#537FE7', bg='#E9F8F9', font='Arial 10 italic')
   display_lb.place(x=350, y=10)
   back_btn = Button(main, text='Back', fg='#181823', bg='#E9F8F9', width=5, height=1, relief=GROOVE, command=lambda: tcs())
   back_btn.place(x=640, y=10)

   code_lb = Label(main, text='Code', fg='#181823', bg='#E9F8F9', font='Arial 10 bold')
   code_lb.place(x=20, y=60)
   fname_lb = Label(main, text='First name', fg='#181823', bg='#E9F8F9', font='Arial 10 bold')
   fname_lb.place(x=80, y=60)
   lname_lb = Label(main, text='Last name', fg='#181823', bg='#E9F8F9', font='Arial 10 bold')
   lname_lb.place(x=170, y=60)
   date_lb = Label(main, text='Date of birth', fg='#181823', bg='#E9F8F9', font='Arial 10 bold')
   date_lb.place(x=260, y=60)
   born_lb = Label(main, text='Born', fg='#181823', bg='#E9F8F9', font='Arial 10 bold')
   born_lb.place(x=360, y=60)
   address_lb = Label(main, text='Address', fg='#181823', bg='#E9F8F9', font='Arial 10 bold')
   address_lb.place(x=430, y=60)
   email_lb = Label(main, text='Email', fg='#181823', bg='#E9F8F9', font='Arial 10 bold')
   email_lb.place(x=550, y=60)
   pass_lb = Label(main, text='Password', fg='#181823', bg='#E9F8F9', font='Arial 10 bold')
   pass_lb.place(x=620, y=60)


def tcs_3():
   main.minsize(700,600)
   main.maxsize(700,600)
   main.title('Administration')
   can1 = Canvas(main, background='#E9F8F9', width=700, height=600)
   can1.place(x=0, y=0)
   can2 = Canvas(main, width=700, height=600)
   can2.place(x=-1, y=90)

   for i in range(len(display_std('tcs', '3'))):
      for j in range(8):
         e = Entry(can2, width=15, font=('Arial',8))
         e.grid(row=i, column=j)
         e.insert(END, display_std('tcs', '3')[i][j])

   display_lb = Label(main, text='TCS - 3', fg='#537FE7', bg='#E9F8F9', font='Arial 10 italic')
   display_lb.place(x=350, y=10)
   back_btn = Button(main, text='Back', fg='#181823', bg='#E9F8F9', width=5, height=1, relief=GROOVE, command=lambda: tcs())
   back_btn.place(x=640, y=10)

   code_lb = Label(main, text='Code', fg='#181823', bg='#E9F8F9', font='Arial 10 bold')
   code_lb.place(x=20, y=60)
   fname_lb = Label(main, text='First name', fg='#181823', bg='#E9F8F9', font='Arial 10 bold')
   fname_lb.place(x=80, y=60)
   lname_lb = Label(main, text='Last name', fg='#181823', bg='#E9F8F9', font='Arial 10 bold')
   lname_lb.place(x=170, y=60)
   date_lb = Label(main, text='Date of birth', fg='#181823', bg='#E9F8F9', font='Arial 10 bold')
   date_lb.place(x=260, y=60)
   born_lb = Label(main, text='Born', fg='#181823', bg='#E9F8F9', font='Arial 10 bold')
   born_lb.place(x=360, y=60)
   address_lb = Label(main, text='Address', fg='#181823', bg='#E9F8F9', font='Arial 10 bold')
   address_lb.place(x=430, y=60)
   email_lb = Label(main, text='Email', fg='#181823', bg='#E9F8F9', font='Arial 10 bold')
   email_lb.place(x=550, y=60)
   pass_lb = Label(main, text='Password', fg='#181823', bg='#E9F8F9', font='Arial 10 bold')
   pass_lb.place(x=620, y=60)


def tcs_4():
   main.minsize(700,600)
   main.maxsize(700,600)
   main.title('Administration')
   can1 = Canvas(main, background='#E9F8F9', width=700, height=600)
   can1.place(x=0, y=0)
   can2 = Canvas(main, width=700, height=600)
   can2.place(x=-1, y=90)

   for i in range(len(display_std('tcs', '4'))):
      for j in range(8):
         e = Entry(can2, width=15, font=('Arial',8))
         e.grid(row=i, column=j)
         e.insert(END, display_std('tcs', '4')[i][j])

   display_lb = Label(main, text='TCS - 4', fg='#537FE7', bg='#E9F8F9', font='Arial 10 italic')
   display_lb.place(x=350, y=10)
   back_btn = Button(main, text='Back', fg='#181823', bg='#E9F8F9', width=5, height=1, relief=GROOVE, command=lambda: tcs())
   back_btn.place(x=640, y=10)

   code_lb = Label(main, text='Code', fg='#181823', bg='#E9F8F9', font='Arial 10 bold')
   code_lb.place(x=20, y=60)
   fname_lb = Label(main, text='First name', fg='#181823', bg='#E9F8F9', font='Arial 10 bold')
   fname_lb.place(x=80, y=60)
   lname_lb = Label(main, text='Last name', fg='#181823', bg='#E9F8F9', font='Arial 10 bold')
   lname_lb.place(x=170, y=60)
   date_lb = Label(main, text='Date of birth', fg='#181823', bg='#E9F8F9', font='Arial 10 bold')
   date_lb.place(x=260, y=60)
   born_lb = Label(main, text='Born', fg='#181823', bg='#E9F8F9', font='Arial 10 bold')
   born_lb.place(x=360, y=60)
   address_lb = Label(main, text='Address', fg='#181823', bg='#E9F8F9', font='Arial 10 bold')
   address_lb.place(x=430, y=60)
   email_lb = Label(main, text='Email', fg='#181823', bg='#E9F8F9', font='Arial 10 bold')
   email_lb.place(x=550, y=60)
   pass_lb = Label(main, text='Password', fg='#181823', bg='#E9F8F9', font='Arial 10 bold')
   pass_lb.place(x=620, y=60)

#
def bac1_1():
   main.minsize(700,600)
   main.maxsize(700,600)
   main.title('Administration')
   can1 = Canvas(main, background='#E9F8F9', width=700, height=600)
   can1.place(x=0, y=0)
   can2 = Canvas(main, width=700, height=600)
   can2.place(x=-1, y=90)

   for i in range(len(display_std('1bac', '1'))):
      for j in range(8):
         e = Entry(can2, width=15, font=('Arial',8))
         e.grid(row=i, column=j)
         e.insert(END, display_std('1bac', '1')[i][j])

   display_lb = Label(main, text='1Bac - 1', fg='#537FE7', bg='#E9F8F9', font='Arial 10 italic')
   display_lb.place(x=350, y=10)
   back_btn = Button(main, text='Back', fg='#181823', bg='#E9F8F9', width=5, height=1, relief=GROOVE, command=lambda: bac1())
   back_btn.place(x=640, y=10)

   code_lb = Label(main, text='Code', fg='#181823', bg='#E9F8F9', font='Arial 10 bold')
   code_lb.place(x=20, y=60)
   fname_lb = Label(main, text='First name', fg='#181823', bg='#E9F8F9', font='Arial 10 bold')
   fname_lb.place(x=80, y=60)
   lname_lb = Label(main, text='Last name', fg='#181823', bg='#E9F8F9', font='Arial 10 bold')
   lname_lb.place(x=170, y=60)
   date_lb = Label(main, text='Date of birth', fg='#181823', bg='#E9F8F9', font='Arial 10 bold')
   date_lb.place(x=260, y=60)
   born_lb = Label(main, text='Born', fg='#181823', bg='#E9F8F9', font='Arial 10 bold')
   born_lb.place(x=360, y=60)
   address_lb = Label(main, text='Address', fg='#181823', bg='#E9F8F9', font='Arial 10 bold')
   address_lb.place(x=430, y=60)
   email_lb = Label(main, text='Email', fg='#181823', bg='#E9F8F9', font='Arial 10 bold')
   email_lb.place(x=550, y=60)
   pass_lb = Label(main, text='Password', fg='#181823', bg='#E9F8F9', font='Arial 10 bold')
   pass_lb.place(x=620, y=60)


def bac1_2():
   main.minsize(700,600)
   main.maxsize(700,600)
   main.title('Administration')
   can1 = Canvas(main, background='#E9F8F9', width=700, height=600)
   can1.place(x=0, y=0)
   can2 = Canvas(main, width=700, height=600)
   can2.place(x=-1, y=90)

   for i in range(len(display_std('1bac', '2'))):
      for j in range(8):
         e = Entry(can2, width=15, font=('Arial',8))
         e.grid(row=i, column=j)
         e.insert(END, display_std('1bac', '2')[i][j])

   display_lb = Label(main, text='1Bac - 2', fg='#537FE7', bg='#E9F8F9', font='Arial 10 italic')
   display_lb.place(x=350, y=10)
   back_btn = Button(main, text='Back', fg='#181823', bg='#E9F8F9', width=5, height=1, relief=GROOVE, command=lambda: bac1())
   back_btn.place(x=640, y=10)

   code_lb = Label(main, text='Code', fg='#181823', bg='#E9F8F9', font='Arial 10 bold')
   code_lb.place(x=20, y=60)
   fname_lb = Label(main, text='First name', fg='#181823', bg='#E9F8F9', font='Arial 10 bold')
   fname_lb.place(x=80, y=60)
   lname_lb = Label(main, text='Last name', fg='#181823', bg='#E9F8F9', font='Arial 10 bold')
   lname_lb.place(x=170, y=60)
   date_lb = Label(main, text='Date of birth', fg='#181823', bg='#E9F8F9', font='Arial 10 bold')
   date_lb.place(x=260, y=60)
   born_lb = Label(main, text='Born', fg='#181823', bg='#E9F8F9', font='Arial 10 bold')
   born_lb.place(x=360, y=60)
   address_lb = Label(main, text='Address', fg='#181823', bg='#E9F8F9', font='Arial 10 bold')
   address_lb.place(x=430, y=60)
   email_lb = Label(main, text='Email', fg='#181823', bg='#E9F8F9', font='Arial 10 bold')
   email_lb.place(x=550, y=60)
   pass_lb = Label(main, text='Password', fg='#181823', bg='#E9F8F9', font='Arial 10 bold')
   pass_lb.place(x=620, y=60)


def bac1_3():
   main.minsize(700,600)
   main.maxsize(700,600)
   main.title('Administration')
   can1 = Canvas(main, background='#E9F8F9', width=700, height=600)
   can1.place(x=0, y=0)
   can2 = Canvas(main, width=700, height=600)
   can2.place(x=-1, y=90)

   for i in range(len(display_std('1bac', '3'))):
      for j in range(8):
         e = Entry(can2, width=15, font=('Arial',8))
         e.grid(row=i, column=j)
         e.insert(END, display_std('1bac', '3')[i][j])

   display_lb = Label(main, text='1Bac - 3', fg='#537FE7', bg='#E9F8F9', font='Arial 10 italic')
   display_lb.place(x=350, y=10)
   back_btn = Button(main, text='Back', fg='#181823', bg='#E9F8F9', width=5, height=1, relief=GROOVE, command=lambda: bac1())
   back_btn.place(x=640, y=10)

   code_lb = Label(main, text='Code', fg='#181823', bg='#E9F8F9', font='Arial 10 bold')
   code_lb.place(x=20, y=60)
   fname_lb = Label(main, text='First name', fg='#181823', bg='#E9F8F9', font='Arial 10 bold')
   fname_lb.place(x=80, y=60)
   lname_lb = Label(main, text='Last name', fg='#181823', bg='#E9F8F9', font='Arial 10 bold')
   lname_lb.place(x=170, y=60)
   date_lb = Label(main, text='Date of birth', fg='#181823', bg='#E9F8F9', font='Arial 10 bold')
   date_lb.place(x=260, y=60)
   born_lb = Label(main, text='Born', fg='#181823', bg='#E9F8F9', font='Arial 10 bold')
   born_lb.place(x=360, y=60)
   address_lb = Label(main, text='Address', fg='#181823', bg='#E9F8F9', font='Arial 10 bold')
   address_lb.place(x=430, y=60)
   email_lb = Label(main, text='Email', fg='#181823', bg='#E9F8F9', font='Arial 10 bold')
   email_lb.place(x=550, y=60)
   pass_lb = Label(main, text='Password', fg='#181823', bg='#E9F8F9', font='Arial 10 bold')
   pass_lb.place(x=620, y=60)


def bac1_4():
   main.minsize(700,600)
   main.maxsize(700,600)
   main.title('Administration')
   can1 = Canvas(main, background='#E9F8F9', width=700, height=600)
   can1.place(x=0, y=0)
   can2 = Canvas(main, width=700, height=600)
   can2.place(x=-1, y=90)

   for i in range(len(display_std('1bac', '4'))):
      for j in range(8):
         e = Entry(can2, width=15, font=('Arial',8))
         e.grid(row=i, column=j)
         e.insert(END, display_std('1bac', '4')[i][j])

   display_lb = Label(main, text='1Bac - 4', fg='#537FE7', bg='#E9F8F9', font='Arial 10 italic')
   display_lb.place(x=350, y=10)
   back_btn = Button(main, text='Back', fg='#181823', bg='#E9F8F9', width=5, height=1, relief=GROOVE, command=lambda: bac1())
   back_btn.place(x=640, y=10)

   code_lb = Label(main, text='Code', fg='#181823', bg='#E9F8F9', font='Arial 10 bold')
   code_lb.place(x=20, y=60)
   fname_lb = Label(main, text='First name', fg='#181823', bg='#E9F8F9', font='Arial 10 bold')
   fname_lb.place(x=80, y=60)
   lname_lb = Label(main, text='Last name', fg='#181823', bg='#E9F8F9', font='Arial 10 bold')
   lname_lb.place(x=170, y=60)
   date_lb = Label(main, text='Date of birth', fg='#181823', bg='#E9F8F9', font='Arial 10 bold')
   date_lb.place(x=260, y=60)
   born_lb = Label(main, text='Born', fg='#181823', bg='#E9F8F9', font='Arial 10 bold')
   born_lb.place(x=360, y=60)
   address_lb = Label(main, text='Address', fg='#181823', bg='#E9F8F9', font='Arial 10 bold')
   address_lb.place(x=430, y=60)
   email_lb = Label(main, text='Email', fg='#181823', bg='#E9F8F9', font='Arial 10 bold')
   email_lb.place(x=550, y=60)
   pass_lb = Label(main, text='Password', fg='#181823', bg='#E9F8F9', font='Arial 10 bold')
   pass_lb.place(x=620, y=60)

#--
def bac2_1():
   main.minsize(700,600)
   main.maxsize(700,600)
   main.title('Administration')
   can1 = Canvas(main, background='#E9F8F9', width=700, height=600)
   can1.place(x=0, y=0)
   can2 = Canvas(main, width=700, height=600)
   can2.place(x=-1, y=90)

   for i in range(len(display_std('2bac', '1'))):
      for j in range(8):
         e = Entry(can2, width=15, font=('Arial',8))
         e.grid(row=i, column=j)
         e.insert(END, display_std('2bac', '1')[i][j])

   display_lb = Label(main, text='2Bac - 1', fg='#537FE7', bg='#E9F8F9', font='Arial 10 italic')
   display_lb.place(x=350, y=10)
   back_btn = Button(main, text='Back', fg='#181823', bg='#E9F8F9', width=5, height=1, relief=GROOVE, command=lambda: bac2())
   back_btn.place(x=640, y=10)

   code_lb = Label(main, text='Code', fg='#181823', bg='#E9F8F9', font='Arial 10 bold')
   code_lb.place(x=20, y=60)
   fname_lb = Label(main, text='First name', fg='#181823', bg='#E9F8F9', font='Arial 10 bold')
   fname_lb.place(x=80, y=60)
   lname_lb = Label(main, text='Last name', fg='#181823', bg='#E9F8F9', font='Arial 10 bold')
   lname_lb.place(x=170, y=60)
   date_lb = Label(main, text='Date of birth', fg='#181823', bg='#E9F8F9', font='Arial 10 bold')
   date_lb.place(x=260, y=60)
   born_lb = Label(main, text='Born', fg='#181823', bg='#E9F8F9', font='Arial 10 bold')
   born_lb.place(x=360, y=60)
   address_lb = Label(main, text='Address', fg='#181823', bg='#E9F8F9', font='Arial 10 bold')
   address_lb.place(x=430, y=60)
   email_lb = Label(main, text='Email', fg='#181823', bg='#E9F8F9', font='Arial 10 bold')
   email_lb.place(x=550, y=60)
   pass_lb = Label(main, text='Password', fg='#181823', bg='#E9F8F9', font='Arial 10 bold')
   pass_lb.place(x=620, y=60)


def bac2_2():
   main.minsize(700,600)
   main.maxsize(700,600)
   main.title('Administration')
   can1 = Canvas(main, background='#E9F8F9', width=700, height=600)
   can1.place(x=0, y=0)
   can2 = Canvas(main, width=700, height=600)
   can2.place(x=-1, y=90)

   for i in range(len(display_std('2bac', '2'))):
      for j in range(8):
         e = Entry(can2, width=15, font=('Arial',8))
         e.grid(row=i, column=j)
         e.insert(END, display_std('2bac', '2')[i][j])

   display_lb = Label(main, text='2Bac - 2', fg='#537FE7', bg='#E9F8F9', font='Arial 10 italic')
   display_lb.place(x=350, y=10)
   back_btn = Button(main, text='Back', fg='#181823', bg='#E9F8F9', width=5, height=1, relief=GROOVE, command=lambda: bac2())
   back_btn.place(x=640, y=10)

   code_lb = Label(main, text='Code', fg='#181823', bg='#E9F8F9', font='Arial 10 bold')
   code_lb.place(x=20, y=60)
   fname_lb = Label(main, text='First name', fg='#181823', bg='#E9F8F9', font='Arial 10 bold')
   fname_lb.place(x=80, y=60)
   lname_lb = Label(main, text='Last name', fg='#181823', bg='#E9F8F9', font='Arial 10 bold')
   lname_lb.place(x=170, y=60)
   date_lb = Label(main, text='Date of birth', fg='#181823', bg='#E9F8F9', font='Arial 10 bold')
   date_lb.place(x=260, y=60)
   born_lb = Label(main, text='Born', fg='#181823', bg='#E9F8F9', font='Arial 10 bold')
   born_lb.place(x=360, y=60)
   address_lb = Label(main, text='Address', fg='#181823', bg='#E9F8F9', font='Arial 10 bold')
   address_lb.place(x=430, y=60)
   email_lb = Label(main, text='Email', fg='#181823', bg='#E9F8F9', font='Arial 10 bold')
   email_lb.place(x=550, y=60)
   pass_lb = Label(main, text='Password', fg='#181823', bg='#E9F8F9', font='Arial 10 bold')
   pass_lb.place(x=620, y=60)


def bac2_3():
   main.minsize(700,600)
   main.maxsize(700,600)
   main.title('Administration')
   can1 = Canvas(main, background='#E9F8F9', width=700, height=600)
   can1.place(x=0, y=0)
   can2 = Canvas(main, width=700, height=600)
   can2.place(x=-1, y=90)

   for i in range(len(display_std('2bac', '3'))):
      for j in range(8):
         e = Entry(can2, width=15, font=('Arial',8))
         e.grid(row=i, column=j)
         e.insert(END, display_std('2bac', '3')[i][j])

   display_lb = Label(main, text='2Bac - 3', fg='#537FE7', bg='#E9F8F9', font='Arial 10 italic')
   display_lb.place(x=350, y=10)
   back_btn = Button(main, text='Back', fg='#181823', bg='#E9F8F9', width=5, height=1, relief=GROOVE, command=lambda: bac2())
   back_btn.place(x=640, y=10)

   code_lb = Label(main, text='Code', fg='#181823', bg='#E9F8F9', font='Arial 10 bold')
   code_lb.place(x=20, y=60)
   fname_lb = Label(main, text='First name', fg='#181823', bg='#E9F8F9', font='Arial 10 bold')
   fname_lb.place(x=80, y=60)
   lname_lb = Label(main, text='Last name', fg='#181823', bg='#E9F8F9', font='Arial 10 bold')
   lname_lb.place(x=170, y=60)
   date_lb = Label(main, text='Date of birth', fg='#181823', bg='#E9F8F9', font='Arial 10 bold')
   date_lb.place(x=260, y=60)
   born_lb = Label(main, text='Born', fg='#181823', bg='#E9F8F9', font='Arial 10 bold')
   born_lb.place(x=360, y=60)
   address_lb = Label(main, text='Address', fg='#181823', bg='#E9F8F9', font='Arial 10 bold')
   address_lb.place(x=430, y=60)
   email_lb = Label(main, text='Email', fg='#181823', bg='#E9F8F9', font='Arial 10 bold')
   email_lb.place(x=550, y=60)
   pass_lb = Label(main, text='Password', fg='#181823', bg='#E9F8F9', font='Arial 10 bold')
   pass_lb.place(x=620, y=60)


def bac2_4():
   main.minsize(700,600)
   main.maxsize(700,600)
   main.title('Administration')
   can1 = Canvas(main, background='#E9F8F9', width=700, height=600)
   can1.place(x=0, y=0)
   can2 = Canvas(main, width=700, height=600)
   can2.place(x=-1, y=90)

   for i in range(len(display_std('2bac', '4'))):
      for j in range(8):
         e = Entry(can2, width=15, font=('Arial',8))
         e.grid(row=i, column=j)
         e.insert(END, display_std('2bac', '4')[i][j])

   display_lb = Label(main, text='2Bac - 4', fg='#537FE7', bg='#E9F8F9', font='Arial 10 italic')
   display_lb.place(x=350, y=10)
   back_btn = Button(main, text='Back', fg='#181823', bg='#E9F8F9', width=5, height=1, relief=GROOVE, command=lambda: bac2())
   back_btn.place(x=640, y=10)

   code_lb = Label(main, text='Code', fg='#181823', bg='#E9F8F9', font='Arial 10 bold')
   code_lb.place(x=20, y=60)
   fname_lb = Label(main, text='First name', fg='#181823', bg='#E9F8F9', font='Arial 10 bold')
   fname_lb.place(x=80, y=60)
   lname_lb = Label(main, text='Last name', fg='#181823', bg='#E9F8F9', font='Arial 10 bold')
   lname_lb.place(x=170, y=60)
   date_lb = Label(main, text='Date of birth', fg='#181823', bg='#E9F8F9', font='Arial 10 bold')
   date_lb.place(x=260, y=60)
   born_lb = Label(main, text='Born', fg='#181823', bg='#E9F8F9', font='Arial 10 bold')
   born_lb.place(x=360, y=60)
   address_lb = Label(main, text='Address', fg='#181823', bg='#E9F8F9', font='Arial 10 bold')
   address_lb.place(x=430, y=60)
   email_lb = Label(main, text='Email', fg='#181823', bg='#E9F8F9', font='Arial 10 bold')
   email_lb.place(x=550, y=60)
   pass_lb = Label(main, text='Password', fg='#181823', bg='#E9F8F9', font='Arial 10 bold')
   pass_lb.place(x=620, y=60)

def notAvai():
   main.minsize(700,600)
   main.maxsize(700,600)
   main.title('NOT AVAILABLE')
   can1 = Canvas(main, background='#E9F8F9', width=700, height=600)
   can1.place(x=0, y=0)
   not0 = Label(main, text="This page isn't available now", font='Arial 30 bold')
   not0.place(x=100, y=200)
   back_btn = Button(main, text='Back', fg='#181823', bg='#E9F8F9', width=30, height=2, relief=GROOVE, command=lambda: settings())
   back_btn.place(x=250, y=490)

#------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------
# THIS IS FOR ADD

def display2():
    main.minsize(700,600)
    main.maxsize(700,600)
    main.title('Add')
    can1 = Canvas(main, background='#E9F8F9', width=700, height=600)
    can1.place(x=0, y=0)
    cat_lb = Label(main, text='ADD', fg='#537FE7', bg='#E9F8F9', font='Arial 20 bold')
    cat_lb.place(x=300, y=150)
    sts_btn = Button(main, text='Student', fg='#181823', bg='#E9F8F9', width=30, height=2, relief=GROOVE, command=lambda: add())
    sts_btn.place(x=250, y=200)
    worker_btn = Button(main, text='Worker', fg='#181823', bg='#E9F8F9', width=30, height=2, relief=GROOVE, command=lambda: worker())
    worker_btn.place(x=250, y=250)
    grade_btn = Button(main, text='Grades', fg='#181823', bg='#E9F8F9', width=30, height=2, relief=GROOVE, command=lambda: stdGrades())
    grade_btn.place(x=250, y=300)
    back_btn = Button(main, text='Back', fg='#181823', bg='#E9F8F9', width=30, height=2, relief=GROOVE, command=lambda: adm())
    back_btn.place(x=250, y=350)

# THIS FOR GRADES

def stdGrades():
    main.minsize(700,600)
    main.maxsize(700,600)
    main.title('Add Grades')
    can1 = Canvas(main, background='#E9F8F9', width=700, height=600)
    can1.place(x=0, y=0)

    code_lb = Label(main, text='Code', fg='#537FE7', bg='#E9F8F9', font='Arial 12 italic')
    code_lb.place(x=130, y=200)
    code_etr = Entry(main, width=10, font='Arial 15 ')
    code_etr.place(x=100, y=250)

    fname_lb = Label(main, text='First name', fg='#537FE7', bg='#E9F8F9', font='Arial 12 italic')
    fname_lb.place(x=280, y=200)
    fname_etr = Entry(main, width=15, font='Arial 15 ')
    fname_etr.place(x=250, y=250)

    lname_lb = Label(main, text='Last name', fg='#537FE7', bg='#E9F8F9', font='Arial 12 italic')
    lname_lb.place(x=480, y=200)
    lname_etr = Entry(main, width=15, font='Arial 15 ')
    lname_etr.place(x=450, y=250)

    search_btn = Button(main, text='Search', fg='black', bg='#E9F8F9', width=20, height=2, relief=GROOVE, command=lambda: search00())
    search_btn.place(x=100, y=330)
    notes_btn = Button(main, text='Add', fg='white', bg='#537FE7', width=26, height=2, relief=GROOVE, command=lambda: enter00())
    notes_btn.place(x=265, y=330)
    back_btn = Button(main, text='Back', fg='black', bg='#E9F8F9', width=20, height=2, relief=GROOVE, command=lambda: display2())
    back_btn.place(x=470, y=330)

    def search00():
        global code_id
        idG = code_etr.get()
        display_edit(idG)
        fname_etr.insert(END, display_edit(idG)[0][1])
        lname_etr.insert(END, display_edit(idG)[0][2])
        code_id = idG

    def enter00():
       if (fname_etr.get() != '') and (lname_etr.get() != '') and (code_etr.get() != ''):
          grades()
       else:
          messagebox.showwarning("Error", "Error")

def grades():
    main.minsize(700,600)
    main.maxsize(700,600)
    main.title('Add Grades')
    can1 = Canvas(main, background='#E9F8F9', width=700, height=600)
    can1.place(x=0, y=0)
      
    back_btn = Button(main, text='Back', relief=GROOVE, command=lambda: stdGrades())
    back_btn.place(x=650, y=10)

    n_lb = Label(main, text='N1', fg='#537FE7', bg='#E9F8F9', font='Arial 10 italic')
    n_lb.place(x=210, y=10)
    n_lb = Label(main, text='N2', fg='#537FE7', bg='#E9F8F9', font='Arial 10 italic')
    n_lb.place(x=280, y=10)
    n_lb = Label(main, text='N3', fg='#537FE7', bg='#E9F8F9', font='Arial 10 italic')
    n_lb.place(x=350, y=10)
    n_lb = Label(main, text='N4', fg='#537FE7', bg='#E9F8F9', font='Arial 10 italic')
    n_lb.place(x=420, y=10)
    n_lb = Label(main, text='N5', fg='#537FE7', bg='#E9F8F9', font='Arial 10 italic')
    n_lb.place(x=490, y=10)

    math_lb = Label(main, text='Math', fg='#537FE7', bg='#E9F8F9', font='Arial 12 italic')
    math_lb.place(x=100, y=50)
    math1_etr = Entry(main, width=4, font='Arial 15 ')
    math1_etr.place(x=200, y=50)
    math2_etr = Entry(main, width=4, font='Arial 15 ')
    math2_etr.place(x=270, y=50)
    math3_etr = Entry(main, width=4, font='Arial 15 ')
    math3_etr.place(x=340, y=50)
    math4_etr = Entry(main, width=4, font='Arial 15 ')
    math4_etr.place(x=410, y=50)
    math5_etr = Entry(main, width=4, font='Arial 15 ')
    math5_etr.place(x=480, y=50)

    pc_lb = Label(main, text='pc', fg='black', bg='#E9F8F9', font='Arial 12 italic')
    pc_lb.place(x=100, y=100)
    pc_etr1 = Entry(main, width=4, font='Arial 15 ')
    pc_etr1.place(x=200, y=100)
    pc_etr2 = Entry(main, width=4, font='Arial 15 ')
    pc_etr2.place(x=270, y=100)
    pc_etr3 = Entry(main, width=4, font='Arial 15 ')
    pc_etr3.place(x=340, y=100)
    pc_etr4 = Entry(main, width=4, font='Arial 15 ')
    pc_etr4.place(x=410, y=100)
    pc_etr5 = Entry(main, width=4, font='Arial 15 ')
    pc_etr5.place(x=480, y=100)

    svt_lb = Label(main, text='Svt', fg='#537FE7', bg='#E9F8F9', font='Arial 12 italic')
    svt_lb.place(x=100, y=150)
    svt_etr1 = Entry(main, width=4, font='Arial 15 ')
    svt_etr1.place(x=200, y=150)
    svt_etr2 = Entry(main, width=4, font='Arial 15 ')
    svt_etr2.place(x=270, y=150)
    svt_etr3 = Entry(main, width=4, font='Arial 15 ')
    svt_etr3.place(x=340, y=150)
    svt_etr4 = Entry(main, width=4, font='Arial 15 ')
    svt_etr4.place(x=410, y=150)
    svt_etr5 = Entry(main, width=4, font='Arial 15 ')
    svt_etr5.place(x=480, y=150)

    ar_lb = Label(main, text='Arabic', fg='black', bg='#E9F8F9', font='Arial 12 italic')
    ar_lb.place(x=100, y=200)
    ar_etr1 = Entry(main, width=4, font='Arial 15 ')
    ar_etr1.place(x=200, y=200)
    ar_etr2 = Entry(main, width=4, font='Arial 15 ')
    ar_etr2.place(x=270, y=200)
    ar_etr3 = Entry(main, width=4, font='Arial 15 ')
    ar_etr3.place(x=340, y=200)
    ar_etr4 = Entry(main, width=4, font='Arial 15 ')
    ar_etr4.place(x=410, y=200)
    ar_etr5 = Entry(main, width=4, font='Arial 15 ')
    ar_etr5.place(x=480, y=200)

    is_lb = Label(main, text='Islamic edu', fg='#537FE7', bg='#E9F8F9', font='Arial 12 italic')
    is_lb.place(x=100, y=250)
    is_etr1 = Entry(main, width=4, font='Arial 15 ')
    is_etr1.place(x=200, y=250)
    is_etr2 = Entry(main, width=4, font='Arial 15 ')
    is_etr2.place(x=270, y=250)
    is_etr3 = Entry(main, width=4, font='Arial 15 ')
    is_etr3.place(x=340, y=250)
    is_etr4 = Entry(main, width=4, font='Arial 15 ')
    is_etr4.place(x=410, y=250)
    is_etr5 = Entry(main, width=4, font='Arial 15 ')
    is_etr5.place(x=480, y=250)

    eng_lb = Label(main, text='English', fg='black', bg='#E9F8F9', font='Arial 12 italic')
    eng_lb.place(x=100, y=300)
    eng_etr1 = Entry(main, width=4, font='Arial 15 ')
    eng_etr1.place(x=200, y=300)
    eng_etr2 = Entry(main, width=4, font='Arial 15 ')
    eng_etr2.place(x=270, y=300)
    eng_etr3 = Entry(main, width=4, font='Arial 15 ')
    eng_etr3.place(x=340, y=300)
    eng_etr4 = Entry(main, width=4, font='Arial 15 ')
    eng_etr4.place(x=410, y=300)
    eng_etr5 = Entry(main, width=4, font='Arial 15 ')
    eng_etr5.place(x=480, y=300)

    fr_lb = Label(main, text='French', fg='#537FE7', bg='#E9F8F9', font='Arial 12 italic')
    fr_lb.place(x=100, y=350)
    fr_etr1 = Entry(main, width=4, font='Arial 15 ')
    fr_etr1.place(x=200, y=350)
    fr_etr2 = Entry(main, width=4, font='Arial 15 ')
    fr_etr2.place(x=270, y=350)
    fr_etr3 = Entry(main, width=4, font='Arial 15 ')
    fr_etr3.place(x=340, y=350)
    fr_etr4 = Entry(main, width=4, font='Arial 15 ')
    fr_etr4.place(x=410, y=350)
    fr_etr5 = Entry(main, width=4, font='Arial 15 ')
    fr_etr5.place(x=480, y=350)

    philo_lb = Label(main, text='Philosophy', fg='black', bg='#E9F8F9', font='Arial 12 italic')
    philo_lb.place(x=100, y=400)
    philo_etr1 = Entry(main, width=4, font='Arial 15 ')
    philo_etr1.place(x=200, y=400)
    philo_etr2 = Entry(main, width=4, font='Arial 15 ')
    philo_etr2.place(x=270, y=400)
    philo_etr3 = Entry(main, width=4, font='Arial 15 ')
    philo_etr3.place(x=340, y=400)
    philo_etr4 = Entry(main, width=4, font='Arial 15 ')
    philo_etr4.place(x=410, y=400)
    philo_etr5 = Entry(main, width=4, font='Arial 15 ')
    philo_etr5.place(x=480, y=400)

    sport_lb = Label(main, text='Sport edu', fg='#537FE7', bg='#E9F8F9', font='Arial 12 italic')
    sport_lb.place(x=100, y=450)
    sport_etr1 = Entry(main, width=4, font='Arial 15 ')
    sport_etr1.place(x=200, y=450)
    sport_etr2 = Entry(main, width=4, font='Arial 15 ')
    sport_etr2.place(x=270, y=450)
    sport_etr3 = Entry(main, width=4, font='Arial 15 ')
    sport_etr3.place(x=340, y=450)
    sport_etr4 = Entry(main, width=4, font='Arial 15 ')
    sport_etr4.place(x=410, y=450)
    sport_etr5 = Entry(main, width=4, font='Arial 15 ')
    sport_etr5.place(x=480, y=450)

    solok_lb = Label(main, text='Diligence \nand \nBehaviour', fg='black', bg='#E9F8F9', font='Arial 12 italic')
    solok_lb.place(x=100, y=500)
    solok_etr1 = Entry(main, width=4, font='Arial 15 ')
    solok_etr1.place(x=200, y=500)
    solok_etr2 = Entry(main, width=4, font='Arial 15 ')
    solok_etr2.place(x=270, y=500)
    solok_etr3 = Entry(main, width=4, font='Arial 15 ')
    solok_etr3.place(x=340, y=500)
    solok_etr4 = Entry(main, width=4, font='Arial 15 ')
    solok_etr4.place(x=410, y=500)
    solok_etr5 = Entry(main, width=4, font='Arial 15 ')
    solok_etr5.place(x=480, y=500)

    add_btn = Button(main, text='Valid', fg='white', bg='green', width=31, height=2, relief=GROOVE, command= lambda: notes())
    add_btn.place(x=300, y=550)

    def notes():
        dd = code_id
        m1 = math1_etr.get()
        m2 = math2_etr.get()
        m3 = math3_etr.get()
        m4 = math4_etr.get()
        m5 = math5_etr.get()
        add_math(dd, m1 ,m2, m3, m4, m5)

        pc1 = pc_etr1.get()
        pc2 = pc_etr2.get()
        pc3 = pc_etr3.get()
        pc4 = pc_etr4.get()
        pc5 = pc_etr5.get()
        add_pc(dd, pc1, pc2, pc3, pc4, pc5)

        svt1 = svt_etr1.get()
        svt2 = svt_etr2.get()
        svt3 = svt_etr3.get()
        svt4 = svt_etr4.get()
        svt5 = svt_etr5.get()
        add_svt(dd, svt1, svt2, svt3, svt4, svt5)

        ar1 = ar_etr1.get()
        ar2 = ar_etr2.get()
        ar3 = ar_etr3.get()
        ar4 = ar_etr4.get()
        ar5 = ar_etr5.get()
        add_arabic(dd, ar1, ar2, ar3, ar4, ar5)

        is1 = is_etr1.get()
        is2 = is_etr2.get()
        is3 = is_etr3.get()
        is4 = is_etr4.get()
        is5 = is_etr5.get()
        add_islamic(dd, is1, is2, is3, is4, is5)

        eng1 = eng_etr1.get()
        eng2 = eng_etr2.get()
        eng3 = eng_etr3.get()
        eng4 = eng_etr4.get()
        eng5 = eng_etr5.get()
        add_english(dd, eng1, eng2, eng3, eng4, eng5)

        fr1 = fr_etr1.get()
        fr2 = fr_etr2.get()
        fr3 = fr_etr3.get()
        fr4 = fr_etr4.get()
        fr5 = fr_etr5.get()
        add_french(dd, fr1, fr2, fr3, fr4, fr5)

        philo1 = philo_etr1.get()
        philo2 = philo_etr2.get()
        philo3 = philo_etr3.get()
        philo4 = philo_etr4.get()
        philo5 = philo_etr5.get()
        add_philosophy(dd, philo1, philo2, philo3, philo4, philo5)

        sport1 = sport_etr1.get()
        sport2 = sport_etr2.get()
        sport3 = sport_etr3.get()
        sport4 = sport_etr4.get()
        sport5 = sport_etr5.get()
        add_sport(dd, sport1, sport2, sport3, sport4, sport5)

        dab1 = solok_etr1.get()
        dab2 = solok_etr2.get()
        dab3 = solok_etr3.get()
        dab4 = solok_etr4.get()
        dab5 = solok_etr5.get()
        add_dab(dd, dab1, dab2, dab3, dab4, dab5)
        messagebox.showinfo("Successfully", "Successfully")

# THIS FOR WORKERS

def worker():
    main.minsize(700,600)
    main.maxsize(700,600)
    main.title('Add Worker')
    can1 = Canvas(main, background='#E9F8F9', width=700, height=600)
    can1.place(x=0, y=0)  

    back_btn = Button(main, text='Back', relief=GROOVE, command=lambda: display2())
    back_btn.place(x=650, y=10)

    code_lb = Label(main, text='Code', fg='#537FE7', bg='#E9F8F9', font='Arial 12 italic')
    code_lb.place(x=100, y=50)
    code_etr = Entry(main, width=20, font='Arial 15 ')
    code_etr.place(x=300, y=50)
    #-----
    l = []
    for i in display_worker_1():
       l.append(i[0])

    while True :
       ra = 'w' + str(randint(1111,99999))
       if ra not in l:
          code_etr.insert(END, ra)
          break
       else:
          continue
      #-----

    fname_lb = Label(main, text='First name', fg='#537FE7', bg='#E9F8F9', font='Arial 12 italic')
    fname_lb.place(x=100, y=100)
    fname_etr = Entry(main, width=20, font='Arial 15 ')
    fname_etr.place(x=300, y=100)

    lname_lb = Label(main, text='Last name', fg='#537FE7', bg='#E9F8F9', font='Arial 12 italic')
    lname_lb.place(x=100, y=150)
    lname_etr = Entry(main, width=20, font='Arial 15 ')
    lname_etr.place(x=300, y=150)

    date_lb = Label(main, text='Date of birth', fg='#537FE7', bg='#E9F8F9', font='Arial 12 italic')
    date_lb.place(x=100, y=200)
    date_etr=DateEntry(main ,selectmode='day', date_pattern='MM-dd-yyyy', width=18, font='Arial 15 ')
    date_etr.place(x=300, y=200)

    born_lb = Label(main, text='Born', fg='#537FE7', bg='#E9F8F9', font='Arial 12 italic')
    born_lb.place(x=100, y=250)
    born_etr = Entry(main, width=20, font='Arial 15 ')
    born_etr.place(x=300, y=250)

    address_lb = Label(main, text='Address', fg='#537FE7', bg='#E9F8F9', font='Arial 12 italic')
    address_lb.place(x=100, y=300)
    address_etr = Entry(main, width=20, font='Arial 15 ')
    address_etr.place(x=300, y=300)
    
    email_lb = Label(main, text='Email', fg='#537FE7', bg='#E9F8F9', font='Arial 12 italic')
    email_lb.place(x=100, y=350)
    email_etr = Entry(main, width=20, font='Arial 15 ')
    email_etr.place(x=300, y=350)
    email_etr.insert(END, code_etr.get())

    pass_lb = Label(main, text='Password', fg='#537FE7', bg='#E9F8F9', font='Arial 12 italic')
    pass_lb.place(x=100, y=400)
    pass_etr = Entry(main, width=20, font='Arial 15 ')
    pass_etr.place(x=300, y=400)
    pass_etr.insert(END, '123456')
 
    tok_lb = Label(main, text='Type of work', fg='#537FE7', bg='#E9F8F9', font='Arial 12 italic')
    tok_lb.place(x=100, y=450)
   #  tok_etr = Entry(main, width=20, font='Arial 15 ')
   #  tok_etr.place(x=300, y=450)
    t_k = ['teacher', 'Other']
    tok_etr = ttk.Combobox(main, width=18, values=t_k, font='Arial 15')
    tok_etr.set('teacher')
    tok_etr.place(x=300, y=450)

    add_btn = Button(main, text='Valid', fg='white', bg='green', width=31, height=2, relief=GROOVE, command=lambda: add_worker_0())
    add_btn.place(x=300, y=500)

    def add_worker_0():
        a1 = code_etr.get()
        a2 = fname_etr.get()
        a3 = lname_etr.get()
        a4 = date_etr.get()
        a5 = born_etr.get()
        a6 = address_etr.get()
        a7 = email_etr.get()
        a8 = pass_etr.get()
        a9 = tok_etr.get()
        if (a1 == '') and (a2 == '') and (a3 == '') and (a4 == '') and (a5 == '') and (a6 == '') and (a7 == '') and (a8 == '') and (a9 == ''):
            messagebox.showwarning("Error", "Error")
        else:
            messagebox.showinfo("Successfully", "Successfully")
            add_worker(a1, a2, a3, a4, a5, a6, a7, a8, a9)

#------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------
# THIS IS FOR EDIT

def into_edit():
    main.minsize(700,600)
    main.maxsize(700,600)
    main.title('Display - Edit')
    can1 = Canvas(main, background='#E9F8F9', width=700, height=600)
    can1.place(x=0, y=0)
    cat_lb = Label(main, text='EDIT', fg='#537FE7', bg='#E9F8F9', font='Arial 20 bold')
    cat_lb.place(x=300, y=150)
    sts_btn = Button(main, text='Student', fg='#181823', bg='#E9F8F9', width=30, height=2, relief=GROOVE, command=lambda: edit())
    sts_btn.place(x=250, y=200)
    worker_btn = Button(main, text='Worker', fg='#181823', bg='#E9F8F9', width=30, height=2, relief=GROOVE, command=lambda: worker_edit())
    worker_btn.place(x=250, y=250)
    grade_btn = Button(main, text='Grades', fg='#181823', bg='#E9F8F9', width=30, height=2, relief=GROOVE, command=lambda: stdGrades_edit())
    grade_btn.place(x=250, y=300)
    back_btn = Button(main, text='Back', fg='#181823', bg='#E9F8F9', width=30, height=2, relief=GROOVE, command=lambda: adm())
    back_btn.place(x=250, y=350)

def worker_edit():
    main.minsize(700,600)
    main.maxsize(700,600)
    main.title('Edit Worker')
    can1 = Canvas(main, background='#E9F8F9', width=700, height=600)
    can1.place(x=0, y=0)

    code_lb = Label(main, text='Code', fg='#537FE7', bg='#E9F8F9', font='Arial 12 italic')
    code_lb.place(x=100, y=50)
    code_etr = Entry(main, width=20, font='Arial 15 ')
    code_etr.place(x=300, y=50) 

    fname_lb = Label(main, text='First name', fg='#537FE7', bg='#E9F8F9', font='Arial 12 italic')
    fname_lb.place(x=100, y=100)
    fname_etr = Entry(main, width=20, font='Arial 15 ')
    fname_etr.place(x=300, y=100)

    lname_lb = Label(main, text='Last name', fg='#537FE7', bg='#E9F8F9', font='Arial 12 italic')
    lname_lb.place(x=100, y=150)
    lname_etr = Entry(main, width=20, font='Arial 15 ')
    lname_etr.place(x=300, y=150)

    date_lb = Label(main, text='Date of birth', fg='#537FE7', bg='#E9F8F9', font='Arial 12 italic')
    date_lb.place(x=100, y=200)
    date_etr = Entry(main, width=20, font='Arial 15 ')
    date_etr.place(x=300, y=200)

    born_lb = Label(main, text='Born', fg='#537FE7', bg='#E9F8F9', font='Arial 12 italic')
    born_lb.place(x=100, y=250)
    born_etr = Entry(main, width=20, font='Arial 15 ')
    born_etr.place(x=300, y=250)

    address_lb = Label(main, text='Address', fg='#537FE7', bg='#E9F8F9', font='Arial 12 italic')
    address_lb.place(x=100, y=300)
    address_etr = Entry(main, width=20, font='Arial 15 ')
    address_etr.place(x=300, y=300)
    
    email_lb = Label(main, text='Email', fg='#537FE7', bg='#E9F8F9', font='Arial 12 italic')
    email_lb.place(x=100, y=350)
    email_etr = Entry(main, width=20, font='Arial 15 ')
    email_etr.place(x=300, y=350)

    pass_lb = Label(main, text='Password', fg='#537FE7', bg='#E9F8F9', font='Arial 12 italic')
    pass_lb.place(x=100, y=400)
    pass_etr = Entry(main, width=20, font='Arial 15 ')
    pass_etr.place(x=300, y=400)
 
    tok_lb = Label(main, text='Type of work', fg='#537FE7', bg='#E9F8F9', font='Arial 12 italic')
    tok_lb.place(x=100, y=450)
   
    t_k = ['teacher', 'Other']
    tok_etr = ttk.Combobox(main, width=18, values=t_k, font='Arial 15')
    tok_etr.set('teacher')
    tok_etr.place(x=300, y=450)
    

    add_btn = Button(main, text='Valid', fg='white', bg='#537FE7', width=14, height=2, relief=GROOVE, command=lambda: worker002())
    add_btn.place(x=417, y=500)
    add_btn = Button(main, text='Search', bg='#E9F8F9', width=14, height=2, relief=GROOVE, command=lambda: worker001())
    add_btn.place(x=300, y=500)
    back_btn = Button(main, text='Back', relief=GROOVE, command=lambda: into_edit())
    back_btn.place(x=650, y=10)

    def worker001():
        id = code_etr.get()
        edit_worker(id)
        tok_etr.set('')
        fname_etr.insert(END,edit_worker(id)[0][1])
        lname_etr.insert(END,edit_worker(id)[0][2])
        date_etr.insert(END,edit_worker(id)[0][3])
        born_etr.insert(END,edit_worker(id)[0][4])
        address_etr.insert(END,edit_worker(id)[0][5])
        email_etr.insert(END,edit_worker(id)[0][6])
        pass_etr.insert(END,edit_worker(id)[0][7])
        tok_etr.insert(END,edit_worker(id)[0][8])
    
    def worker002():
        c0 = code_etr.get()
        c1 = fname_etr.get()
        c2 = lname_etr.get()
        c3 = date_etr.get()
        c4 = born_etr.get()
        c5 = address_etr.get()
        c6 = email_etr.get()
        c7 = pass_etr.get()
        c8 = tok_etr.get()
        if (c1 != '') and (c2 != '') and (c3 != '') and (c4 != '') and (c5 != '') and (c6 != '') and (c7 != '') and (c8 != ''):
            messagebox.showinfo("Successfully", "Successfully")
            edit_worker1(c1, c2, c3, c4, c5, c6, c7, c8, c0)
        else:
            messagebox.showerror("Error", "Error")


def stdGrades_edit():
    main.minsize(700,600)
    main.maxsize(700,600)
    main.title('Edit Grades')
    can1 = Canvas(main, background='#E9F8F9', width=700, height=600)
    can1.place(x=0, y=0)

    code_lb = Label(main, text='Code', fg='#537FE7', bg='#E9F8F9', font='Arial 12 italic')
    code_lb.place(x=130, y=200)
    code_etr = Entry(main, width=10, font='Arial 15 ')
    code_etr.place(x=100, y=250)

    fname_lb = Label(main, text='First name', fg='#537FE7', bg='#E9F8F9', font='Arial 12 italic')
    fname_lb.place(x=280, y=200)
    fname_etr = Entry(main, width=15, font='Arial 15 ')
    fname_etr.place(x=250, y=250)

    lname_lb = Label(main, text='Last name', fg='#537FE7', bg='#E9F8F9', font='Arial 12 italic')
    lname_lb.place(x=480, y=200)
    lname_etr = Entry(main, width=15, font='Arial 15 ')
    lname_etr.place(x=450, y=250)

    search_btn = Button(main, text='Search', fg='black', bg='#E9F8F9', width=20, height=2, relief=GROOVE, command=lambda: search00())
    search_btn.place(x=100, y=330)
    notes_btn = Button(main, text='Add', fg='white', bg='#537FE7', width=26, height=2, relief=GROOVE, command=lambda: enter00())
    notes_btn.place(x=265, y=330)
    back_btn = Button(main, text='Back', fg='black', bg='#E9F8F9', width=20, height=2, relief=GROOVE, command=lambda: into_edit())
    back_btn.place(x=470, y=330)

    def search00():
        global code_id1
        idG = code_etr.get()
        display_edit(idG)
        fname_etr.insert(END, display_edit(idG)[0][1])
        lname_etr.insert(END, display_edit(idG)[0][2])
        code_id1 = idG

    def enter00():
       if (fname_etr.get() != '') and (lname_etr.get() != '') and (code_etr.get() != ''):
          grades_edit()
       else:
          messagebox.showwarning("Error", "Error")
def grades_edit():
    main.minsize(700,600)
    main.maxsize(700,600)
    main.title('Edit Grades')
    can1 = Canvas(main, background='#E9F8F9', width=700, height=600)
    can1.place(x=0, y=0)

    n_lb = Label(main, text='N1', fg='#537FE7', bg='#E9F8F9', font='Arial 10 italic')
    n_lb.place(x=210, y=10)
    n_lb = Label(main, text='N2', fg='#537FE7', bg='#E9F8F9', font='Arial 10 italic')
    n_lb.place(x=280, y=10)
    n_lb = Label(main, text='N3', fg='#537FE7', bg='#E9F8F9', font='Arial 10 italic')
    n_lb.place(x=350, y=10)
    n_lb = Label(main, text='N4', fg='#537FE7', bg='#E9F8F9', font='Arial 10 italic')
    n_lb.place(x=420, y=10)
    n_lb = Label(main, text='N5', fg='#537FE7', bg='#E9F8F9', font='Arial 10 italic')
    n_lb.place(x=490, y=10)

    math_lb = Label(main, text='Math', fg='#537FE7', bg='#E9F8F9', font='Arial 12 italic')
    math_lb.place(x=100, y=50)
    math1_etr = Entry(main, width=4, font='Arial 15 ')
    math1_etr.place(x=200, y=50)
    math2_etr = Entry(main, width=4, font='Arial 15 ')
    math2_etr.place(x=270, y=50)
    math3_etr = Entry(main, width=4, font='Arial 15 ')
    math3_etr.place(x=340, y=50)
    math4_etr = Entry(main, width=4, font='Arial 15 ')
    math4_etr.place(x=410, y=50)
    math5_etr = Entry(main, width=4, font='Arial 15 ')
    math5_etr.place(x=480, y=50)

    pc_lb = Label(main, text='pc', fg='black', bg='#E9F8F9', font='Arial 12 italic')
    pc_lb.place(x=100, y=100)
    pc_etr1 = Entry(main, width=4, font='Arial 15 ')
    pc_etr1.place(x=200, y=100)
    pc_etr2 = Entry(main, width=4, font='Arial 15 ')
    pc_etr2.place(x=270, y=100)
    pc_etr3 = Entry(main, width=4, font='Arial 15 ')
    pc_etr3.place(x=340, y=100)
    pc_etr4 = Entry(main, width=4, font='Arial 15 ')
    pc_etr4.place(x=410, y=100)
    pc_etr5 = Entry(main, width=4, font='Arial 15 ')
    pc_etr5.place(x=480, y=100)

    svt_lb = Label(main, text='Svt', fg='#537FE7', bg='#E9F8F9', font='Arial 12 italic')
    svt_lb.place(x=100, y=150)
    svt_etr1 = Entry(main, width=4, font='Arial 15 ')
    svt_etr1.place(x=200, y=150)
    svt_etr2 = Entry(main, width=4, font='Arial 15 ')
    svt_etr2.place(x=270, y=150)
    svt_etr3 = Entry(main, width=4, font='Arial 15 ')
    svt_etr3.place(x=340, y=150)
    svt_etr4 = Entry(main, width=4, font='Arial 15 ')
    svt_etr4.place(x=410, y=150)
    svt_etr5 = Entry(main, width=4, font='Arial 15 ')
    svt_etr5.place(x=480, y=150)

    ar_lb = Label(main, text='Arabic', fg='black', bg='#E9F8F9', font='Arial 12 italic')
    ar_lb.place(x=100, y=200)
    ar_etr1 = Entry(main, width=4, font='Arial 15 ')
    ar_etr1.place(x=200, y=200)
    ar_etr2 = Entry(main, width=4, font='Arial 15 ')
    ar_etr2.place(x=270, y=200)
    ar_etr3 = Entry(main, width=4, font='Arial 15 ')
    ar_etr3.place(x=340, y=200)
    ar_etr4 = Entry(main, width=4, font='Arial 15 ')
    ar_etr4.place(x=410, y=200)
    ar_etr5 = Entry(main, width=4, font='Arial 15 ')
    ar_etr5.place(x=480, y=200)

    is_lb = Label(main, text='Islamic edu', fg='#537FE7', bg='#E9F8F9', font='Arial 12 italic')
    is_lb.place(x=100, y=250)
    is_etr1 = Entry(main, width=4, font='Arial 15 ')
    is_etr1.place(x=200, y=250)
    is_etr2 = Entry(main, width=4, font='Arial 15 ')
    is_etr2.place(x=270, y=250)
    is_etr3 = Entry(main, width=4, font='Arial 15 ')
    is_etr3.place(x=340, y=250)
    is_etr4 = Entry(main, width=4, font='Arial 15 ')
    is_etr4.place(x=410, y=250)
    is_etr5 = Entry(main, width=4, font='Arial 15 ')
    is_etr5.place(x=480, y=250)

    eng_lb = Label(main, text='English', fg='black', bg='#E9F8F9', font='Arial 12 italic')
    eng_lb.place(x=100, y=300)
    eng_etr1 = Entry(main, width=4, font='Arial 15 ')
    eng_etr1.place(x=200, y=300)
    eng_etr2 = Entry(main, width=4, font='Arial 15 ')
    eng_etr2.place(x=270, y=300)
    eng_etr3 = Entry(main, width=4, font='Arial 15 ')
    eng_etr3.place(x=340, y=300)
    eng_etr4 = Entry(main, width=4, font='Arial 15 ')
    eng_etr4.place(x=410, y=300)
    eng_etr5 = Entry(main, width=4, font='Arial 15 ')
    eng_etr5.place(x=480, y=300)

    fr_lb = Label(main, text='French', fg='#537FE7', bg='#E9F8F9', font='Arial 12 italic')
    fr_lb.place(x=100, y=350)
    fr_etr1 = Entry(main, width=4, font='Arial 15 ')
    fr_etr1.place(x=200, y=350)
    fr_etr2 = Entry(main, width=4, font='Arial 15 ')
    fr_etr2.place(x=270, y=350)
    fr_etr3 = Entry(main, width=4, font='Arial 15 ')
    fr_etr3.place(x=340, y=350)
    fr_etr4 = Entry(main, width=4, font='Arial 15 ')
    fr_etr4.place(x=410, y=350)
    fr_etr5 = Entry(main, width=4, font='Arial 15 ')
    fr_etr5.place(x=480, y=350)

    philo_lb = Label(main, text='Philosophy', fg='black', bg='#E9F8F9', font='Arial 12 italic')
    philo_lb.place(x=100, y=400)
    philo_etr1 = Entry(main, width=4, font='Arial 15 ')
    philo_etr1.place(x=200, y=400)
    philo_etr2 = Entry(main, width=4, font='Arial 15 ')
    philo_etr2.place(x=270, y=400)
    philo_etr3 = Entry(main, width=4, font='Arial 15 ')
    philo_etr3.place(x=340, y=400)
    philo_etr4 = Entry(main, width=4, font='Arial 15 ')
    philo_etr4.place(x=410, y=400)
    philo_etr5 = Entry(main, width=4, font='Arial 15 ')
    philo_etr5.place(x=480, y=400)

    sport_lb = Label(main, text='Sport edu', fg='#537FE7', bg='#E9F8F9', font='Arial 12 italic')
    sport_lb.place(x=100, y=450)
    sport_etr1 = Entry(main, width=4, font='Arial 15 ')
    sport_etr1.place(x=200, y=450)
    sport_etr2 = Entry(main, width=4, font='Arial 15 ')
    sport_etr2.place(x=270, y=450)
    sport_etr3 = Entry(main, width=4, font='Arial 15 ')
    sport_etr3.place(x=340, y=450)
    sport_etr4 = Entry(main, width=4, font='Arial 15 ')
    sport_etr4.place(x=410, y=450)
    sport_etr5 = Entry(main, width=4, font='Arial 15 ')
    sport_etr5.place(x=480, y=450)

    solok_lb = Label(main, text='Diligence \nand \nBehaviour', fg='black', bg='#E9F8F9', font='Arial 12 italic')
    solok_lb.place(x=100, y=500)
    solok_etr1 = Entry(main, width=4, font='Arial 15 ')
    solok_etr1.place(x=200, y=500)
    solok_etr2 = Entry(main, width=4, font='Arial 15 ')
    solok_etr2.place(x=270, y=500)
    solok_etr3 = Entry(main, width=4, font='Arial 15 ')
    solok_etr3.place(x=340, y=500)
    solok_etr4 = Entry(main, width=4, font='Arial 15 ')
    solok_etr4.place(x=410, y=500)
    solok_etr5 = Entry(main, width=4, font='Arial 15 ')
    solok_etr5.place(x=480, y=500)

    add_btn = Button(main, text='Valid', fg='white', bg='#537FE7', width=14, height=2, relief=GROOVE, command= lambda: change_notes())
    add_btn.place(x=320, y=550)
    add_btn = Button(main, text='Search', bg='#E9F8F9', width=14, height=2, relief=GROOVE, command=lambda: insert_notes())
    add_btn.place(x=200, y=550)
    back_btn = Button(main, text='Back', bg='#E9F8F9', width=14, height=2, relief=GROOVE, command=lambda: stdGrades_edit())
    back_btn.place(x=440, y=550)

    def insert_notes():
        #math
        math1_etr.insert(END, display_math(code_id1)[0][1])
        math2_etr.insert(END, display_math(code_id1)[0][2])
        math3_etr.insert(END, display_math(code_id1)[0][3])
        math4_etr.insert(END, display_math(code_id1)[0][4])
        math5_etr.insert(END, display_math(code_id1)[0][5])
        #pc
        pc_etr1.insert(END, display_pc(code_id1)[0][1])
        pc_etr2.insert(END, display_pc(code_id1)[0][2])
        pc_etr3.insert(END, display_pc(code_id1)[0][3])
        pc_etr4.insert(END, display_pc(code_id1)[0][4])
        pc_etr5.insert(END, display_pc(code_id1)[0][5])
        #svt
        svt_etr1.insert(END, display_svt(code_id1)[0][1])
        svt_etr2.insert(END, display_svt(code_id1)[0][2])
        svt_etr3.insert(END, display_svt(code_id1)[0][3])
        svt_etr4.insert(END, display_svt(code_id1)[0][4])
        svt_etr5.insert(END, display_svt(code_id1)[0][5])
        #arabic
        ar_etr1.insert(END, display_arabic(code_id1)[0][1])
        ar_etr2.insert(END, display_arabic(code_id1)[0][2])
        ar_etr3.insert(END, display_arabic(code_id1)[0][3])
        ar_etr4.insert(END, display_arabic(code_id1)[0][4])
        ar_etr5.insert(END, display_arabic(code_id1)[0][5])
        #islamic
        is_etr1.insert(END, display_islamic(code_id1)[0][1])
        is_etr2.insert(END, display_islamic(code_id1)[0][2])
        is_etr3.insert(END, display_islamic(code_id1)[0][3])
        is_etr4.insert(END, display_islamic(code_id1)[0][4])
        is_etr5.insert(END, display_islamic(code_id1)[0][5])
        #english
        eng_etr1.insert(END, display_english(code_id1)[0][1])
        eng_etr2.insert(END, display_english(code_id1)[0][2])
        eng_etr3.insert(END, display_english(code_id1)[0][3])
        eng_etr4.insert(END, display_english(code_id1)[0][4])
        eng_etr5.insert(END, display_english(code_id1)[0][5])
        #french
        fr_etr1.insert(END, display_french(code_id1)[0][1])
        fr_etr2.insert(END, display_french(code_id1)[0][2])
        fr_etr3.insert(END, display_french(code_id1)[0][3])
        fr_etr4.insert(END, display_french(code_id1)[0][4])
        fr_etr5.insert(END, display_french(code_id1)[0][5])
        #philo
        philo_etr1.insert(END, display_philosophy(code_id1)[0][1])
        philo_etr2.insert(END, display_philosophy(code_id1)[0][2])
        philo_etr3.insert(END, display_philosophy(code_id1)[0][3])
        philo_etr4.insert(END, display_philosophy(code_id1)[0][4])
        philo_etr5.insert(END, display_philosophy(code_id1)[0][5])
        #sport
        sport_etr1.insert(END, display_sport(code_id1)[0][1])
        sport_etr2.insert(END, display_sport(code_id1)[0][2])
        sport_etr3.insert(END, display_sport(code_id1)[0][3])
        sport_etr4.insert(END, display_sport(code_id1)[0][4])
        sport_etr5.insert(END, display_sport(code_id1)[0][5])
        #solok
        solok_etr1.insert(END, display_dab(code_id1)[0][1])
        solok_etr2.insert(END, display_dab(code_id1)[0][2])
        solok_etr3.insert(END, display_dab(code_id1)[0][3])
        solok_etr4.insert(END, display_dab(code_id1)[0][4])
        solok_etr5.insert(END, display_dab(code_id1)[0][5])
    def change_notes():
        #math
        m1 = math1_etr.get()
        m2 = math2_etr.get()
        m3 = math3_etr.get()
        m4 = math4_etr.get()
        m5 = math5_etr.get()
        edit_math(m1,m2,m3,m4,m5,code_id1)
        #pc
        pc1 = pc_etr1.get()
        pc2 = pc_etr2.get()
        pc3 = pc_etr3.get()
        pc4 = pc_etr4.get()
        pc5 = pc_etr5.get()
        edit_pc(pc1,pc2,pc3,pc4,pc5,code_id1)
        #svt
        svt1 = svt_etr1.get()
        svt2 = svt_etr2.get()
        svt3 = svt_etr3.get()
        svt4 = svt_etr4.get()
        svt5 = svt_etr5.get()
        edit_svt(svt1,svt2,svt3,svt4,svt5,code_id1)
        #arabic
        ar1 = ar_etr1.get()
        ar2 = ar_etr2.get()
        ar3 = ar_etr3.get()
        ar4 = ar_etr4.get()
        ar5 = ar_etr5.get()
        edit_arabic(ar1,ar2,ar3,ar4,ar5,code_id1)
        #islamic
        is1 = is_etr1.get()
        is2 = is_etr2.get()
        is3 = is_etr3.get()
        is4 = is_etr4.get()
        is5 = is_etr5.get()
        edit_islamic(is1,is2,is3,is4,is5,code_id1)
        #english
        eng1 = eng_etr1.get()
        eng2 = eng_etr2.get()
        eng3 = eng_etr3.get()
        eng4 = eng_etr4.get()
        eng5 = eng_etr5.get()
        edit_english(eng1,eng2,eng3,eng4,eng5,code_id1)
        #fransh
        fr1 = fr_etr1.get()
        fr2 = fr_etr2.get()
        fr3 = fr_etr3.get()
        fr4 = fr_etr4.get()
        fr5 = fr_etr5.get()
        edit_french(fr1,fr2,fr3,fr4,fr5,code_id1)
        #philo
        philo1 = philo_etr1.get()
        philo2 = philo_etr2.get()
        philo3 = philo_etr3.get()
        philo4 = philo_etr4.get()
        philo5 = philo_etr5.get()
        edit_philosophy(philo1,philo2,philo3,philo4,philo5,code_id1)
        #sport
        sport1 = sport_etr1.get()
        sport2 = sport_etr2.get()
        sport3 = sport_etr3.get()
        sport4 = sport_etr4.get()
        sport5 = sport_etr5.get()
        edit_sport(sport1,sport2,sport3,sport4,sport5,code_id1)
        #dab
        dab1 = solok_etr1.get()
        dab2 = solok_etr2.get()
        dab3 = solok_etr3.get()
        dab4 = solok_etr4.get()
        dab5 = solok_etr5.get()
        edit_dab(dab1,dab2,dab3,dab4,dab5,code_id1)
        messagebox.showinfo("Successfully", "Successfully")

#------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------
# THIS IS FOR REMOVE

def into_remove():
    main.minsize(700,600)
    main.maxsize(700,600)
    main.title('Display - Remove')
    can1 = Canvas(main, background='#E9F8F9', width=700, height=600)
    can1.place(x=0, y=0)
    cat_lb = Label(main, text='Remove', fg='#537FE7', bg='#E9F8F9', font='Arial 20 bold')
    cat_lb.place(x=300, y=150)
    sts_btn = Button(main, text='Student', fg='#181823', bg='#E9F8F9', width=30, height=2, relief=GROOVE, command=lambda: remove())
    sts_btn.place(x=250, y=200)
    worker_btn = Button(main, text='Worker', fg='#181823', bg='#E9F8F9', width=30, height=2, relief=GROOVE, command=lambda: remove_worker())
    worker_btn.place(x=250, y=250)
    back_btn = Button(main, text='Back', fg='#181823', bg='#E9F8F9', width=30, height=2, relief=GROOVE, command=lambda: adm())
    back_btn.place(x=250, y=300)

def remove_worker():
    main.minsize(700,600)
    main.maxsize(700,600)
    main.title('Remove - Worker')
    can1 = Canvas(main, background='#E9F8F9', width=700, height=600)
    can1.place(x=0, y=0)

    back_btn = Button(main, text='Back', relief=GROOVE, command=lambda: into_remove())
    back_btn.place(x=650, y=10)

    code_lb = Label(main, text='Code', fg='#537FE7', bg='#E9F8F9', font='Arial 12 italic')
    code_lb.place(x=100, y=50)
    code_etr = Entry(main, width=20, font='Arial 15 ')
    code_etr.place(x=300, y=50) 

    fname_lb = Label(main, text='First name', fg='#537FE7', bg='#E9F8F9', font='Arial 12 italic')
    fname_lb.place(x=100, y=100)
    fname_etr = Entry(main, width=20, font='Arial 15 ')
    fname_etr.place(x=300, y=100)

    lname_lb = Label(main, text='Last name', fg='#537FE7', bg='#E9F8F9', font='Arial 12 italic')
    lname_lb.place(x=100, y=150)
    lname_etr = Entry(main, width=20, font='Arial 15 ')
    lname_etr.place(x=300, y=150)

    date_lb = Label(main, text='Date of birth', fg='#537FE7', bg='#E9F8F9', font='Arial 12 italic')
    date_lb.place(x=100, y=200)
    date_etr = Entry(main, width=20, font='Arial 15 ')
    date_etr.place(x=300, y=200)

    born_lb = Label(main, text='Born', fg='#537FE7', bg='#E9F8F9', font='Arial 12 italic')
    born_lb.place(x=100, y=250)
    born_etr = Entry(main, width=20, font='Arial 15 ')
    born_etr.place(x=300, y=250)

    address_lb = Label(main, text='Address', fg='#537FE7', bg='#E9F8F9', font='Arial 12 italic')
    address_lb.place(x=100, y=300)
    address_etr = Entry(main, width=20, font='Arial 15 ')
    address_etr.place(x=300, y=300)
    
    email_lb = Label(main, text='Email', fg='#537FE7', bg='#E9F8F9', font='Arial 12 italic')
    email_lb.place(x=100, y=350)
    email_etr = Entry(main, width=20, font='Arial 15 ')
    email_etr.place(x=300, y=350)

    pass_lb = Label(main, text='Password', fg='#537FE7', bg='#E9F8F9', font='Arial 12 italic')
    pass_lb.place(x=100, y=400)
    pass_etr = Entry(main, width=20, font='Arial 15 ')
    pass_etr.place(x=300, y=400)
 
    tok_lb = Label(main, text='Type of work', fg='#537FE7', bg='#E9F8F9', font='Arial 12 italic')
    tok_lb.place(x=100, y=450)
    tok_etr = Entry(main, width=20, font='Arial 15 ')
    tok_etr.place(x=300, y=450)

    add_btn = Button(main, text='Search', bg='#E9F8F9', width=14, height=2, relief=GROOVE, command=lambda: insert_remove())
    add_btn.place(x=300, y=550)
    add_btn_edit = Button(main, text='Valid', fg='white', bg='red', width=14, height=2, relief=GROOVE, command=lambda: remove_worker0())
    add_btn_edit.place(x=417, y=550)

    def insert_remove():
        global id_00
        id = code_etr.get()
        edit_worker(id)
        fname_etr.insert(END, edit_worker(id)[0][1])
        lname_etr.insert(END, edit_worker(id)[0][2])
        date_etr.insert(END, edit_worker(id)[0][3])
        born_etr.insert(END, edit_worker(id)[0][4])
        address_etr.insert(END, edit_worker(id)[0][5])
        email_etr.insert(END, edit_worker(id)[0][6])
        pass_etr.insert(END, edit_worker(id)[0][7])
        tok_etr.insert(END, edit_worker(id)[0][8])
        id_00 = id
        
    def remove_worker0():
        reomve_worker(id_00)
        messagebox.showinfo("Successfully", "Successfully")



#------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------
# THIS IS FOR DISPLAY


def display_all1():
    main.minsize(700,600)
    main.maxsize(700,600)
    can0 = Canvas(main, background='#E9F8F9', width=700, height=600)
    can0.place(x=0, y=0)
    main.title('Display')

    cat_lb = Label(main, text='Display', fg='#537FE7', bg='#E9F8F9', font='Arial 20 bold')
    cat_lb.place(x=300, y=150)
    sts_btn = Button(main, text='Student', fg='#181823', bg='#E9F8F9', width=30, height=2, relief=GROOVE, command=lambda: display())
    sts_btn.place(x=250, y=200)
    grade_btn = Button(main, text='Grades', fg='#181823', bg='#E9F8F9', width=30, height=2, relief=GROOVE, command=lambda: display_grade_1())
    grade_btn.place(x=250, y=250)
    worker_btn = Button(main, text='Worker', fg='#181823', bg='#E9F8F9', width=30, height=2, relief=GROOVE, command=lambda: display_worker())
    worker_btn.place(x=250, y=300)
    back_btn = Button(main, text='Back', fg='#181823', bg='#E9F8F9', width=30, height=2, relief=GROOVE, command=lambda: adm())
    back_btn.place(x=250, y=350)


def display_worker():
    main.minsize(700,600)
    main.maxsize(700,600)
    can0 = Canvas(main, background='#E9F8F9', width=700, height=600)
    can0.place(x=0, y=0)
    main.title('Display - Worker')
    back_btn = Button(main, text='Back', fg='#181823', bg='#E9F8F9', width=5, height=1, relief=GROOVE, command=lambda: display_all1())
    back_btn.place(x=640, y=10)
    can1 = Canvas(main, background='#E9F8F9', width=700, height=600)
    can1.place(x=-1, y=80)
    display_lb = Label(main, text='Worker', fg='#537FE7', bg='#E9F8F9', font='Arial 10 italic')
    display_lb.place(x=350, y=10)
    code_lb = Label(main, text='Code', fg='#181823', bg='#E9F8F9', font='Arial 10 bold')
    code_lb.place(x=10, y=50)
    fname_lb = Label(main, text='First name', fg='#181823', bg='#E9F8F9', font='Arial 10 bold')
    fname_lb.place(x=80, y=50)
    lname_lb = Label(main, text='Last name', fg='#181823', bg='#E9F8F9', font='Arial 10 bold')
    lname_lb.place(x=167, y=50)
    date_lb = Label(main, text='Date of birth', fg='#181823', bg='#E9F8F9', font='Arial 10 bold')
    date_lb.place(x=250, y=50)
    born_lb = Label(main, text='Born', fg='#181823', bg='#E9F8F9', font='Arial 10 bold')
    born_lb.place(x=350, y=50)
    address_lb = Label(main, text='Address', fg='#181823', bg='#E9F8F9', font='Arial 10 bold')
    address_lb.place(x=420, y=50)
    email_lb = Label(main, text='Email', fg='#181823', bg='#E9F8F9', font='Arial 10 bold')
    email_lb.place(x=510, y=50)
    pass_lb = Label(main, text='Password', fg='#181823', bg='#E9F8F9', font='Arial 10 bold')
    pass_lb.place(x=570, y=50)
    pass_lb = Label(main, text='Type', fg='#181823', bg='#E9F8F9', font='Arial 10 bold')
    pass_lb.place(x=650, y=50)


    for i in range(len(display_worker_1())):
        for j in range(9):# widith 13
            e = Entry(can1, width=13, font=('Arial',8))
            e.grid(row=i, column=j)
            e.insert(END, display_worker_1()[i][j])
           
def display_grade_1():
    main.minsize(700,600)
    main.maxsize(700,600)
    can0 = Canvas(main, background='#E9F8F9', width=700, height=600)
    can0.place(x=0, y=0)
    main.title('Display - grade')

    code_lb = Label(main, text='Code', fg='#181823', bg='#E9F8F9', font='Arial 10 bold')
    code_lb.place(x=150, y=200)
    code_etr = Entry(main, width=11, font='Arial 15')
    code_etr.place(x=130, y=230)
    fname_lb = Label(main, text='First name', fg='#181823', bg='#E9F8F9', font='Arial 10 bold')
    fname_lb.place(x=320, y=200)
    fname_etr = Entry(main, width=11, font='Arial 15')
    fname_etr.place(x=310, y=230)
    lname_lb = Label(main, text='Last name', fg='#181823', bg='#E9F8F9', font='Arial 10 bold')
    lname_lb.place(x=490, y=200)
    lname_etr = Entry(main, width=11, font='Arial 15')
    lname_etr.place(x=480, y=230)

    search_btn = Button(main, text='Search', fg='black', bg='#E9F8F9', width=20, height=2, relief=GROOVE, command=lambda: displaySTD())
    search_btn.place(x=130, y=300)
    display_btn = Button(main, text='Display', fg='white', bg='#537FE7', width=20, height=2, relief=GROOVE, command=lambda: display_grade_2())
    display_btn.place(x=294, y=300)
    back_btn = Button(main, text='Back', fg='black', bg='#E9F8F9', width=20, height=2, relief=GROOVE, command=lambda: display_all1())
    back_btn.place(x=455, y=300)

    def displaySTD():
        global idGrade 
        id = code_etr.get()
        display_edit(id)
        fname_etr.insert(END, display_edit(id)[0][1])
        lname_etr.insert(END, display_edit(id)[0][2])
        idGrade = id

def display_grade_2():
    main.minsize(700,600)
    main.maxsize(700,600)
    can0 = Canvas(main, background='#E9F8F9', width=700, height=600)
    can0.place(x=0, y=0)
    main.title('Display - grade')
    full = display_edit(idGrade)[0][1] + ' ' + display_edit(idGrade)[0][2]
    full_lb = Label(main, text=full, fg='#537FE7', bg='#E9F8F9', font='Arial 20 bold')
    full_lb.place(x=205, y=10)

    n_lb = Label(main, text='N1', fg='#537FE7', bg='#E9F8F9', font='Arial 10 italic')
    n_lb.place(x=210, y=90)
    n_lb = Label(main, text='N2', fg='#537FE7', bg='#E9F8F9', font='Arial 10 italic')
    n_lb.place(x=280, y=90)
    n_lb = Label(main, text='N3', fg='#537FE7', bg='#E9F8F9', font='Arial 10 italic')
    n_lb.place(x=350, y=90)
    n_lb = Label(main, text='N4', fg='#537FE7', bg='#E9F8F9', font='Arial 10 italic')
    n_lb.place(x=420, y=90)
    n_lb = Label(main, text='N5', fg='#537FE7', bg='#E9F8F9', font='Arial 10 italic')
    n_lb.place(x=500, y=90)
    #math
    can_math = Canvas(main, background='red', width=500, height=20)
    can_math.place(x=170, y=120)
    math_lb = Label(main, text='Math', fg='#537FE7', bg='#E9F8F9', font='Arial 12 italic')
    math_lb.place(x=50, y=120)
    for i in range(len(display_math(idGrade))):
        for j in range(1,6):# widith 13
            e = Entry(can_math, width=13, font=('Arial',8))
            e.grid(row=i, column=j)
            e.insert(END, display_math(idGrade)[i][j])

    #pc
    can_pc = Canvas(main, background='red', width=500, height=20)
    can_pc.place(x=170, y=160)
    math_lb = Label(main, text='pc', fg='#537FE7', bg='#E9F8F9', font='Arial 12 italic')
    math_lb.place(x=50, y=160)
    for i in range(len(display_pc(idGrade))):
        for j in range(1,6):# widith 13
            e = Entry(can_pc, width=13, font=('Arial',8))
            e.grid(row=i, column=j)
            e.insert(END, display_pc(idGrade)[i][j])

    #svt
    can_svt = Canvas(main, background='red', width=500, height=20)
    can_svt.place(x=170, y=200)
    math_lb = Label(main, text='Svt', fg='#537FE7', bg='#E9F8F9', font='Arial 12 italic')
    math_lb.place(x=50, y=200)
    for i in range(len(display_svt(idGrade))):
        for j in range(1,6):# widith 13
            e = Entry(can_svt, width=13, font=('Arial',8))
            e.grid(row=i, column=j)
            e.insert(END, display_svt(idGrade)[i][j])

    #arabic
    can_arabic = Canvas(main, background='red', width=500, height=20)
    can_arabic.place(x=170, y=240)
    math_lb = Label(main, text='Arabic', fg='#537FE7', bg='#E9F8F9', font='Arial 12 italic')
    math_lb.place(x=50, y=240)
    for i in range(len(display_arabic(idGrade))):
        for j in range(1,6):# widith 13
            e = Entry(can_arabic, width=13, font=('Arial',8))
            e.grid(row=i, column=j)
            e.insert(END, display_arabic(idGrade)[i][j])

    #islamic
    can_islamic = Canvas(main, background='red', width=500, height=20)
    can_islamic.place(x=170, y=280)
    math_lb = Label(main, text='Islamic edu', fg='#537FE7', bg='#E9F8F9', font='Arial 12 italic')
    math_lb.place(x=50, y=280)
    for i in range(len(display_islamic(idGrade))):
        for j in range(1,6):# widith 13
            e = Entry(can_islamic, width=13, font=('Arial',8))
            e.grid(row=i, column=j)
            e.insert(END, display_islamic(idGrade)[i][j])

    #english
    can_english = Canvas(main, background='red', width=500, height=20)
    can_english.place(x=170, y=320)
    math_lb = Label(main, text='English', fg='#537FE7', bg='#E9F8F9', font='Arial 12 italic')
    math_lb.place(x=50, y=320)
    for i in range(len(display_english(idGrade))):
        for j in range(1,6):# widith 13
            e = Entry(can_english, width=13, font=('Arial',8))
            e.grid(row=i, column=j)
            e.insert(END, display_english(idGrade)[i][j])

    #french
    can_french = Canvas(main, background='red', width=500, height=20)
    can_french.place(x=170, y=360)
    math_lb = Label(main, text='French', fg='#537FE7', bg='#E9F8F9', font='Arial 12 italic')
    math_lb.place(x=50, y=360)
    for i in range(len(display_french(idGrade))):
        for j in range(1,6):# widith 13
            e = Entry(can_french, width=13, font=('Arial',8))
            e.grid(row=i, column=j)
            e.insert(END, display_french(idGrade)[i][j])

    #Philosophy
    can_philo = Canvas(main, background='red', width=500, height=20)
    can_philo.place(x=170, y=400)
    math_lb = Label(main, text='Philosophy', fg='#537FE7', bg='#E9F8F9', font='Arial 12 italic')
    math_lb.place(x=50, y=400)
    for i in range(len(display_philosophy(idGrade))):
        for j in range(1,6):# widith 13
            e = Entry(can_philo, width=13, font=('Arial',8))
            e.grid(row=i, column=j)
            e.insert(END, display_philosophy(idGrade)[i][j])

    #sport
    can_sport = Canvas(main, background='red', width=500, height=20)
    can_sport.place(x=170, y=440)
    math_lb = Label(main, text='Sport edu', fg='#537FE7', bg='#E9F8F9', font='Arial 12 italic')
    math_lb.place(x=50, y=440)
    for i in range(len(display_sport(idGrade))):
        for j in range(1,6):# widith 13
            e = Entry(can_sport, width=13, font=('Arial',8))
            e.grid(row=i, column=j)
            e.insert(END, display_sport(idGrade)[i][j])

    #Diligence
    can_dab = Canvas(main, background='red', width=500, height=20)
    can_dab.place(x=170, y=480)
    math_lb = Label(main, text='Diligence \nand \nBehaviour', fg='#537FE7', bg='#E9F8F9', font='Arial 12 italic')
    math_lb.place(x=50, y=480)
    for i in range(len(display_dab(idGrade))):
        for j in range(1,6):# widith 13
            e = Entry(can_dab, width=13, font=('Arial',8))
            e.grid(row=i, column=j)
            e.insert(END, display_dab(idGrade)[i][j])

    back_btn = Button(main, text='Back', fg='black', bg='#E9F8F9', width=20, height=2, relief=GROOVE, command=lambda: display_grade_1())
    back_btn.place(x=300, y=530)


# ADD GRADES FOR TEACHER



def stdGrades_1(id=0):
    main.minsize(700,600)
    main.maxsize(700,600)
    main.title('Add Grades')
    can1 = Canvas(main, background='#E9F8F9', width=700, height=600)
    can1.place(x=0, y=0)

    code_lb = Label(main, text='Code', fg='#537FE7', bg='#E9F8F9', font='Arial 12 italic')
    code_lb.place(x=130, y=200)
    code_etr = Entry(main, width=10, font='Arial 15 ')
    code_etr.place(x=100, y=250)

    fname_lb = Label(main, text='First name', fg='#537FE7', bg='#E9F8F9', font='Arial 12 italic')
    fname_lb.place(x=280, y=200)
    fname_etr = Entry(main, width=15, font='Arial 15 ')
    fname_etr.place(x=250, y=250)

    lname_lb = Label(main, text='Last name', fg='#537FE7', bg='#E9F8F9', font='Arial 12 italic')
    lname_lb.place(x=480, y=200)
    lname_etr = Entry(main, width=15, font='Arial 15 ')
    lname_etr.place(x=450, y=250)

    search_btn = Button(main, text='Search', fg='black', bg='#E9F8F9', width=20, height=2, relief=GROOVE, command=lambda: search00())
    search_btn.place(x=100, y=330)
    notes_btn = Button(main, text='Add', fg='white', bg='#537FE7', width=26, height=2, relief=GROOVE, command=lambda: enter00(id))
    notes_btn.place(x=265, y=330)
    back_btn = Button(main, text='Back', fg='black', bg='#E9F8F9', width=20, height=2, relief=GROOVE, command=lambda: teacher_acc(id))
    back_btn.place(x=470, y=330)

    def search00():
        global code_id
        idG = code_etr.get()
        display_edit(idG)
        fname_etr.insert(END, display_edit(idG)[0][1])
        lname_etr.insert(END, display_edit(idG)[0][2])
        code_id = idG

    def enter00(id):
       if (fname_etr.get() != '') and (lname_etr.get() != '') and (code_etr.get() != ''):
          grades_1(id)
       else:
          messagebox.showwarning("Error", "Error")

def grades_1(id=0):
    main.minsize(700,600)
    main.maxsize(700,600)
    main.title('Add Grades')
    can1 = Canvas(main, background='#E9F8F9', width=700, height=600)
    can1.place(x=0, y=0)
      
    back_btn = Button(main, text='Back', relief=GROOVE, command=lambda: stdGrades_1(id))
    back_btn.place(x=650, y=10)

    n_lb = Label(main, text='N1', fg='#537FE7', bg='#E9F8F9', font='Arial 10 italic')
    n_lb.place(x=210, y=10)
    n_lb = Label(main, text='N2', fg='#537FE7', bg='#E9F8F9', font='Arial 10 italic')
    n_lb.place(x=280, y=10)
    n_lb = Label(main, text='N3', fg='#537FE7', bg='#E9F8F9', font='Arial 10 italic')
    n_lb.place(x=350, y=10)
    n_lb = Label(main, text='N4', fg='#537FE7', bg='#E9F8F9', font='Arial 10 italic')
    n_lb.place(x=420, y=10)
    n_lb = Label(main, text='N5', fg='#537FE7', bg='#E9F8F9', font='Arial 10 italic')
    n_lb.place(x=490, y=10)

    math_lb = Label(main, text='Math', fg='#537FE7', bg='#E9F8F9', font='Arial 12 italic')
    math_lb.place(x=100, y=50)
    math1_etr = Entry(main, width=4, font='Arial 15 ')
    math1_etr.place(x=200, y=50)
    math2_etr = Entry(main, width=4, font='Arial 15 ')
    math2_etr.place(x=270, y=50)
    math3_etr = Entry(main, width=4, font='Arial 15 ')
    math3_etr.place(x=340, y=50)
    math4_etr = Entry(main, width=4, font='Arial 15 ')
    math4_etr.place(x=410, y=50)
    math5_etr = Entry(main, width=4, font='Arial 15 ')
    math5_etr.place(x=480, y=50)

    pc_lb = Label(main, text='pc', fg='black', bg='#E9F8F9', font='Arial 12 italic')
    pc_lb.place(x=100, y=100)
    pc_etr1 = Entry(main, width=4, font='Arial 15 ')
    pc_etr1.place(x=200, y=100)
    pc_etr2 = Entry(main, width=4, font='Arial 15 ')
    pc_etr2.place(x=270, y=100)
    pc_etr3 = Entry(main, width=4, font='Arial 15 ')
    pc_etr3.place(x=340, y=100)
    pc_etr4 = Entry(main, width=4, font='Arial 15 ')
    pc_etr4.place(x=410, y=100)
    pc_etr5 = Entry(main, width=4, font='Arial 15 ')
    pc_etr5.place(x=480, y=100)

    svt_lb = Label(main, text='Svt', fg='#537FE7', bg='#E9F8F9', font='Arial 12 italic')
    svt_lb.place(x=100, y=150)
    svt_etr1 = Entry(main, width=4, font='Arial 15 ')
    svt_etr1.place(x=200, y=150)
    svt_etr2 = Entry(main, width=4, font='Arial 15 ')
    svt_etr2.place(x=270, y=150)
    svt_etr3 = Entry(main, width=4, font='Arial 15 ')
    svt_etr3.place(x=340, y=150)
    svt_etr4 = Entry(main, width=4, font='Arial 15 ')
    svt_etr4.place(x=410, y=150)
    svt_etr5 = Entry(main, width=4, font='Arial 15 ')
    svt_etr5.place(x=480, y=150)

    ar_lb = Label(main, text='Arabic', fg='black', bg='#E9F8F9', font='Arial 12 italic')
    ar_lb.place(x=100, y=200)
    ar_etr1 = Entry(main, width=4, font='Arial 15 ')
    ar_etr1.place(x=200, y=200)
    ar_etr2 = Entry(main, width=4, font='Arial 15 ')
    ar_etr2.place(x=270, y=200)
    ar_etr3 = Entry(main, width=4, font='Arial 15 ')
    ar_etr3.place(x=340, y=200)
    ar_etr4 = Entry(main, width=4, font='Arial 15 ')
    ar_etr4.place(x=410, y=200)
    ar_etr5 = Entry(main, width=4, font='Arial 15 ')
    ar_etr5.place(x=480, y=200)

    is_lb = Label(main, text='Islamic edu', fg='#537FE7', bg='#E9F8F9', font='Arial 12 italic')
    is_lb.place(x=100, y=250)
    is_etr1 = Entry(main, width=4, font='Arial 15 ')
    is_etr1.place(x=200, y=250)
    is_etr2 = Entry(main, width=4, font='Arial 15 ')
    is_etr2.place(x=270, y=250)
    is_etr3 = Entry(main, width=4, font='Arial 15 ')
    is_etr3.place(x=340, y=250)
    is_etr4 = Entry(main, width=4, font='Arial 15 ')
    is_etr4.place(x=410, y=250)
    is_etr5 = Entry(main, width=4, font='Arial 15 ')
    is_etr5.place(x=480, y=250)

    eng_lb = Label(main, text='English', fg='black', bg='#E9F8F9', font='Arial 12 italic')
    eng_lb.place(x=100, y=300)
    eng_etr1 = Entry(main, width=4, font='Arial 15 ')
    eng_etr1.place(x=200, y=300)
    eng_etr2 = Entry(main, width=4, font='Arial 15 ')
    eng_etr2.place(x=270, y=300)
    eng_etr3 = Entry(main, width=4, font='Arial 15 ')
    eng_etr3.place(x=340, y=300)
    eng_etr4 = Entry(main, width=4, font='Arial 15 ')
    eng_etr4.place(x=410, y=300)
    eng_etr5 = Entry(main, width=4, font='Arial 15 ')
    eng_etr5.place(x=480, y=300)

    fr_lb = Label(main, text='French', fg='#537FE7', bg='#E9F8F9', font='Arial 12 italic')
    fr_lb.place(x=100, y=350)
    fr_etr1 = Entry(main, width=4, font='Arial 15 ')
    fr_etr1.place(x=200, y=350)
    fr_etr2 = Entry(main, width=4, font='Arial 15 ')
    fr_etr2.place(x=270, y=350)
    fr_etr3 = Entry(main, width=4, font='Arial 15 ')
    fr_etr3.place(x=340, y=350)
    fr_etr4 = Entry(main, width=4, font='Arial 15 ')
    fr_etr4.place(x=410, y=350)
    fr_etr5 = Entry(main, width=4, font='Arial 15 ')
    fr_etr5.place(x=480, y=350)

    philo_lb = Label(main, text='Philosophy', fg='black', bg='#E9F8F9', font='Arial 12 italic')
    philo_lb.place(x=100, y=400)
    philo_etr1 = Entry(main, width=4, font='Arial 15 ')
    philo_etr1.place(x=200, y=400)
    philo_etr2 = Entry(main, width=4, font='Arial 15 ')
    philo_etr2.place(x=270, y=400)
    philo_etr3 = Entry(main, width=4, font='Arial 15 ')
    philo_etr3.place(x=340, y=400)
    philo_etr4 = Entry(main, width=4, font='Arial 15 ')
    philo_etr4.place(x=410, y=400)
    philo_etr5 = Entry(main, width=4, font='Arial 15 ')
    philo_etr5.place(x=480, y=400)

    sport_lb = Label(main, text='Sport edu', fg='#537FE7', bg='#E9F8F9', font='Arial 12 italic')
    sport_lb.place(x=100, y=450)
    sport_etr1 = Entry(main, width=4, font='Arial 15 ')
    sport_etr1.place(x=200, y=450)
    sport_etr2 = Entry(main, width=4, font='Arial 15 ')
    sport_etr2.place(x=270, y=450)
    sport_etr3 = Entry(main, width=4, font='Arial 15 ')
    sport_etr3.place(x=340, y=450)
    sport_etr4 = Entry(main, width=4, font='Arial 15 ')
    sport_etr4.place(x=410, y=450)
    sport_etr5 = Entry(main, width=4, font='Arial 15 ')
    sport_etr5.place(x=480, y=450)

    solok_lb = Label(main, text='Diligence \nand \nBehaviour', fg='black', bg='#E9F8F9', font='Arial 12 italic')
    solok_lb.place(x=100, y=500)
    solok_etr1 = Entry(main, width=4, font='Arial 15 ')
    solok_etr1.place(x=200, y=500)
    solok_etr2 = Entry(main, width=4, font='Arial 15 ')
    solok_etr2.place(x=270, y=500)
    solok_etr3 = Entry(main, width=4, font='Arial 15 ')
    solok_etr3.place(x=340, y=500)
    solok_etr4 = Entry(main, width=4, font='Arial 15 ')
    solok_etr4.place(x=410, y=500)
    solok_etr5 = Entry(main, width=4, font='Arial 15 ')
    solok_etr5.place(x=480, y=500)

    add_btn = Button(main, text='Valid', fg='white', bg='green', width=31, height=2, relief=GROOVE, command= lambda: notes())
    add_btn.place(x=300, y=550)

    def notes():
        dd = code_id
        m1 = math1_etr.get()
        m2 = math2_etr.get()
        m3 = math3_etr.get()
        m4 = math4_etr.get()
        m5 = math5_etr.get()
        add_math(dd, m1 ,m2, m3, m4, m5)

        pc1 = pc_etr1.get()
        pc2 = pc_etr2.get()
        pc3 = pc_etr3.get()
        pc4 = pc_etr4.get()
        pc5 = pc_etr5.get()
        add_pc(dd, pc1, pc2, pc3, pc4, pc5)

        svt1 = svt_etr1.get()
        svt2 = svt_etr2.get()
        svt3 = svt_etr3.get()
        svt4 = svt_etr4.get()
        svt5 = svt_etr5.get()
        add_svt(dd, svt1, svt2, svt3, svt4, svt5)

        ar1 = ar_etr1.get()
        ar2 = ar_etr2.get()
        ar3 = ar_etr3.get()
        ar4 = ar_etr4.get()
        ar5 = ar_etr5.get()
        add_arabic(dd, ar1, ar2, ar3, ar4, ar5)

        is1 = is_etr1.get()
        is2 = is_etr2.get()
        is3 = is_etr3.get()
        is4 = is_etr4.get()
        is5 = is_etr5.get()
        add_islamic(dd, is1, is2, is3, is4, is5)

        eng1 = eng_etr1.get()
        eng2 = eng_etr2.get()
        eng3 = eng_etr3.get()
        eng4 = eng_etr4.get()
        eng5 = eng_etr5.get()
        add_english(dd, eng1, eng2, eng3, eng4, eng5)

        fr1 = fr_etr1.get()
        fr2 = fr_etr2.get()
        fr3 = fr_etr3.get()
        fr4 = fr_etr4.get()
        fr5 = fr_etr5.get()
        add_french(dd, fr1, fr2, fr3, fr4, fr5)

        philo1 = philo_etr1.get()
        philo2 = philo_etr2.get()
        philo3 = philo_etr3.get()
        philo4 = philo_etr4.get()
        philo5 = philo_etr5.get()
        add_philosophy(dd, philo1, philo2, philo3, philo4, philo5)

        sport1 = sport_etr1.get()
        sport2 = sport_etr2.get()
        sport3 = sport_etr3.get()
        sport4 = sport_etr4.get()
        sport5 = sport_etr5.get()
        add_sport(dd, sport1, sport2, sport3, sport4, sport5)

        dab1 = solok_etr1.get()
        dab2 = solok_etr2.get()
        dab3 = solok_etr3.get()
        dab4 = solok_etr4.get()
        dab5 = solok_etr5.get()
        add_dab(dd, dab1, dab2, dab3, dab4, dab5)
        messagebox.showinfo("Successfully", "Successfully")


main.mainloop()