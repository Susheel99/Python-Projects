from tkinter import *
from tkinter import ttk


class Student:
    def __init__(self, rt):
        self.root = rt
        self.root.title("Student Management System")
        self.root.geometry("700x500")
        title = Label(self.root, text="Student File Management", bd=10, relief=GROOVE, font=("times new roman", 40, "bold"), bg='crimson', fg='grey')
        title.pack(side=TOP, fill=X)

        # Manage frame
        Manage_frame = Frame(self.root, bd=4, relief=RIDGE, bg="CRIMSON")
        Manage_frame.place(x=20, y=100, width=450, height=650)

        m_title = Label(Manage_frame, text="Manage students", font=("times new roman", 30, "bold"),bg="CRIMSON", fg='white')
        m_title.grid(row=0, columnspan=2, pady=20)

        # roll no
        lbl = Label(Manage_frame, text="Roll no.", font=("times new roman", 20, "bold"), bg="CRIMSON",fg='white')
        lbl.grid(row=1, column=0, pady=10, padx=20, sticky='w')

        txt = Entry(Manage_frame, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt.grid(row=1, column=1, pady=10, padx=20, sticky='w')

        # name
        lbl2 = Label(Manage_frame, text="Name", font=("times new roman", 20, "bold"), bg="CRIMSON", fg='white')
        lbl2.grid(row=2, column=0, pady=10, padx=20, sticky='w')

        txt2 = Entry(Manage_frame, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt2.grid(row=2, column=1, pady=10, padx=20, sticky='w')

        # email
        lbl3 = Label(Manage_frame, text="Email", font=("times new roman", 20, "bold"), bg="CRIMSON", fg='white')
        lbl3.grid(row=3, column=0, pady=10, padx=20, sticky='w')

        txt3 = Entry(Manage_frame, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt3.grid(row=3, column=1, pady=10, padx=20, sticky='w')

        # gender
        lbl4 = Label(Manage_frame, text="Gender", font=("times new roman", 20, "bold"), bg="CRIMSON", fg='white')
        lbl4.grid(row=4, column=0, pady=10, padx=20, sticky='w')

        combo_gender = ttk.Combobox(Manage_frame, font=("times new roman", 13, "bold"),state='readonly')
        combo_gender['values'] = ('male', 'female', 'other')
        combo_gender.grid(row=4, column=1,pady=10, padx=20)

        # contact
        lbl5 = Label(Manage_frame, text="Contact", font=("times new roman", 20, "bold"), bg="CRIMSON", fg='white')
        lbl5.grid(row=5, column=0, pady=10, padx=20, sticky='w')

        txt5 = Entry(Manage_frame, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt5.grid(row=5, column=1, pady=10, padx=20, sticky='w')

        # dob
        lbl6 = Label(Manage_frame, text="D.O.B", font=("times new roman", 20, "bold"), bg="CRIMSON", fg='white')
        lbl6.grid(row=6, column=0, pady=10, padx=20, sticky='w')

        txt6 = Entry(Manage_frame, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt6.grid(row=6, column=1, pady=10, padx=20, sticky='w')

        #address
        lbl7 = Label(Manage_frame, text="Address", font=("times new roman", 20, "bold"), bg="CRIMSON", fg='white')
        lbl7.grid(row=7, column=0, pady=10, padx=20, sticky='w')

        txt7 = Text(Manage_frame, width=30, height=4, font=("", 10))
        txt7.grid(row=7, column=1, pady=10, padx=20, sticky='w')

        # **buttons**
        btn_frame = Frame(self.root, bd=4, relief=RIDGE, bg="CRIMSON")
        btn_frame.place(x=30, y=650, width=420)

        addbtn = Button(btn_frame, text='Add', width=10).grid(row=0, column=0, padx=10, pady=10)
        upadatebtn = Button(btn_frame, text='Update', width=10).grid(row=0, column=1, padx=10, pady=10)
        deletebtn = Button(btn_frame, text='Delete', width=10).grid(row=0, column=2, padx=10, pady=10)
        clearbtn = Button(btn_frame, text='Clear', width=10).grid(row=0, column=3, padx=10, pady=10)





        # _______Data frame_______
        data_frame = Frame(self.root, bd=4, relief=RIDGE, bg="CRIMSON")
        data_frame.place(x=500, y=100, width=800, height=560)

        # search
        lbl8 = Label(data_frame, text="Search By", font=("times new roman", 20, "bold"), bg="CRIMSON", fg='white')
        lbl8.grid(row=0, column=0, pady=10, padx=10, sticky='w')

        combo_search = ttk.Combobox(data_frame, font=("times new roman", 13, "bold"), state='readonly')
        combo_search['values'] = ('Roll', 'Name', 'Contact')
        combo_search.grid(row=0, column=1, pady=10, padx=5)

        txt8 = Entry(data_frame, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt8.grid(row=0, column=2, pady=10, padx=10, sticky='w')

        search_btn = Button(data_frame, text='Search', width=10).grid(row=0, column=3, padx=5, pady=10)
        showall_btn = Button(data_frame, text='Show All', width=10).grid(row=0, column=4, padx=5, pady=10)

        # **Table frame**
        table_frame = Frame(data_frame, bd=4, relief=RIDGE, bg="CRIMSON")
        table_frame.place(x=10, y=70, width=760, height=450)

        scroll_x = Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = Scrollbar(table_frame,orient=VERTICAL)
        student_table = ttk.Treeview(table_frame,column=('roll', 'name', 'email', 'gender', 'contact', 'dob', 'address'), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.config(command=student_table.yview)
        scroll_x.config(command=student_table.xview)
        student_table.heading('roll', text='Roll No')
        student_table.heading('name', text='Name')
        student_table.heading('email', text='Email')
        student_table.heading('gender', text='Gender')
        student_table.heading('contact', text='Contact')
        student_table.heading('dob', text='D.O.B')
        student_table.heading('address', text='Address')
        student_table['show'] = 'headings'
        student_table.column('roll', width=50)
        student_table.column('name', width=100)
        student_table.column('email', width=100)
        student_table.column('gender', width=100)
        student_table.column('contact', width=100)
        student_table.column('dob', width=100)
        student_table.column('address', width=150)

        student_table.pack(fill=BOTH, expand=1)





root = Tk()
ob = Student(root)
root.mainloop()
