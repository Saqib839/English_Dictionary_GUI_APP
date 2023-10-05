from tkinter import *
import dictionary_backend as be

window = Tk()
window.wm_title('English Dictionary')
inp1 = StringVar()

def value(event=None):
    text1.delete(1.0,END)
    text2.delete(1.0,END)
    text2.insert(END,be.checker(inp1.get()))
    text1.insert(END,be.first_match_func())

label1 = Label(window,text='Enter English World' , width=17, padx=5)
label1.grid(row =0, column = 0)

entry1 = Entry(window, 
                textvariable= inp1,
                font=("Arial", 12, "bold",),
                justify="center",
                width= 17
                )
entry1.grid(row =0 , column = 1)
entry1.bind("<Return>", value)

text1= Text(window,height= 1,  
            width=40, 
            font=("Arial", 10, "bold"), 
            foreground="#191970",
            relief='groove',
            padx =10,
            pady =5,
            bd =3
            )

text1.grid(row= 1, column=0, rowspan=1,columnspan=4)

text2= Text(window, height =10,
            width=55,
            font=("Calibri", 11), 
            padx=10,
            pady=10,
            wrap = WORD
            )
text2.grid(row= 2, column=0,rowspan=3,columnspan=4)

button1 = Button(window, text= 'check', 
            command= value, width=8,
            relief='sunken',
            bd=3,
            activeforeground='Yellow',
            activebackground='Black',
            font=("Arial", 12, "bold")
            )
button1.grid (row=0, column=3,columnspan=1)
window.mainloop()