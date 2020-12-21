from tkinter import *
import time

# Window Setup
root = Tk()
root.title('Digital Clock')
root.geometry('1350x750+0+0')
root.config(bg='#081923')


# Functions
def clock():
    h = str(time.strftime("%H"))
    m = str(time.strftime("%M"))
    s = str(time.strftime("%S"))
    print(h, m, s)

    if int(h) > 12:
        l_state.config(text='PM')

    if (int(h) > 3) and (int(h) <= 12):
        l_state2.config(text='MORNING')

    elif (int(h) > 12) and (int(h) < 4):
        l_state2.config(text='NOON')
    elif (int(h) > 4) and (int(h) < 10):
        l_state2.config(text='EVENING')
    else:
        l_state2.config(text='NIGHT')

    if int(h) > 12:
        h = str((int(h)-12))
    l_hr.config(text=h)
    l_mt.config(text=m)
    l_s.config(text=s)

    l_s.after(200, clock)


# Hour
l_hr = Label(root, text='12', font=('times new roman', 50, 'bold'), bg='#7f8708', fg='white')
l_hr.place(x=350, y=200, width=150, height=150)

l_hr2 = Label(root, text='HOUR', font=('times new roman', 20, 'bold'), bg='#7f8708', fg='white')
l_hr2.place(x=350, y=360, width=150, height=50)

# Minute
l_mt = Label(root, text='60', font=('times new roman', 50, 'bold'), bg='#008EA4', fg='white')
l_mt.place(x=520, y=200, width=150, height=150)

l_mt2 = Label(root, text='MINUTE', font=('times new roman', 20, 'bold'), bg='#008EA4', fg='white')
l_mt2.place(x=520, y=360, width=150, height=50)

# Second
l_s = Label(root, text='60', font=('times new roman', 50, 'bold'), bg='#088767', fg='white')
l_s.place(x=690, y=200, width=150, height=150)

l_s2 = Label(root, text='SECOND', font=('times new roman', 20, 'bold'), bg='#088767', fg='white')
l_s2.place(x=690, y=360, width=150, height=50)

# AM-PM
l_state = Label(root, text='AM', font=('times new roman', 35, 'bold'), bg='#540887', fg='white')
l_state.place(x=860, y=200, width=150, height=150)

l_state2 = Label(root, text='NOON', font=('times new roman', 20, 'bold'), bg='#540887', fg='white')
l_state2.place(x=860, y=360, width=150, height=50)

clock()

root.mainloop()
