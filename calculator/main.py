from tkinter import *
from tkinter.messagebox import *

# variables
font = ('Blinkstar', 30, 'bold')


# functions
def clear(event):
    ex = text_field.get()
    ex = ex[0:len(ex)-1]
    text_field.delete(0, END)
    text_field.insert(0, ex)


def all_clear(event):
    text_field.delete(0, END)


def click_btn_function(event):
    print('button-clicked')
    b = event.widget
    text = b['text']
    print(text)

    if text == '=':
        try:
            exp = text_field.get()
            ans = eval(exp)
            text_field.delete(0, END)
            text_field.insert(0, ans)
        except Exception as e:
            print("Error...", e)
            showerror("Error", e)
        return

    text_field.insert(END, text)


window = Tk()
window.title("Calculator")
window.geometry('600x700')

# Image label
pic = PhotoImage(file='images/cal2.png')
image_label = Label(window, image=pic)
image_label.pack(side=TOP, pady=15)

# Heading label
heading_label = Label(window, text='Calculator', font=font)
heading_label.pack(side=TOP, pady=5)

# text field
text_field = Entry(window, font=font, justify=CENTER)
text_field.pack(side=TOP, pady=20, fill=X, padx=10)

# buttons
button_frame = Frame(window)
button_frame.pack(side=TOP, pady=5)

# adding buttons
temp = 1
for i in range(0, 3):
    for j in range(0, 3):
        btn = Button(button_frame, text=str(temp), font=font, width=5, relief='ridge', activebackground='orange',
                     activeforeground='white')
        btn.grid(row=i, column=j, padx=1, pady=1)
        temp += 1
        btn.bind('<Button-1>', click_btn_function)

zero_btn = Button(button_frame, text=str(0), font=font, width=5, relief='ridge', activebackground='orange',
                  activeforeground='white')
zero_btn.grid(row=3, column=1, padx=1, pady=1)
zero_btn.bind('<Button-1>', click_btn_function)

dot_btn = Button(button_frame, text='.', font=font, width=5, relief='ridge', activebackground='orange',
                 activeforeground='white')
dot_btn.grid(row=3, column=0, padx=1, pady=1)
dot_btn.bind('<Button-1>', click_btn_function)

equal_btn = Button(button_frame, text='=', font=font, width=5, relief='ridge', activebackground='orange',
                   activeforeground='white')
equal_btn.grid(row=3, column=2, padx=1, pady=1)
equal_btn.bind('<Button-1>', click_btn_function)

plus_btn = Button(button_frame, text='+', font=font, width=5, relief='ridge', activebackground='orange',
                  activeforeground='white')
plus_btn.grid(row=0, column=3, padx=1, pady=1)
plus_btn.bind('<Button-1>', click_btn_function)

minus_btn = Button(button_frame, text='-', font=font, width=5, relief='ridge', activebackground='orange',
                   activeforeground='white')
minus_btn.grid(row=1, column=3, padx=1, pady=1)
minus_btn.bind('<Button-1>', click_btn_function)

mul_btn = Button(button_frame, text='*', font=font, width=5, relief='ridge', activebackground='orange',
                 activeforeground='white')
mul_btn.grid(row=2, column=3, padx=1, pady=1)
mul_btn.bind('<Button-1>', click_btn_function)

div_btn = Button(button_frame, text='/', font=font, width=5, relief='ridge', activebackground='orange',
                 activeforeground='white')
div_btn.grid(row=3, column=3, padx=1, pady=1)
div_btn.bind('<Button-1>', click_btn_function)

clear_btn = Button(button_frame, text='<--', font=font, width=11, relief='ridge', activebackground='orange',
                   activeforeground='white')
clear_btn.grid(row=4, column=0, padx=1, pady=1, columnspan=2)
clear_btn.bind('<Button-1>', clear)

allclear_btn = Button(button_frame, text='AC', font=font, width=11, relief='ridge', activebackground='orange',
                      activeforeground='white')
allclear_btn.grid(row=4, column=2, padx=1, pady=1, columnspan=2)
allclear_btn.bind('<Button-1>', all_clear)

window.mainloop()
