from tkinter import *
from tkinter.ttk import Combobox
from currency_converter import CurrencyConverter
from PIL import Image,ImageTk

def converter():
    c = CurrencyConverter()
    result = c.convert(Amount.get(),str(from_string.get()),str(to_string.get()))
    Amount.set("")
    Amount.set(result)

root = Tk()
root.title("Currency Converter")
root.geometry("500x500+100+100")
root.config(bg='white')

background = ImageTk.PhotoImage(Image.open('Background2.png'))
lbl_bg = Label(root,image = background,bg='white')
lbl_bg.place(x=120,y=0)

from_lbl = Label(root,text="From",bg="white",font=('Times new roman',15))
from_lbl.place(x=20,y=220)

from_string = StringVar()
fromchoosen = Combobox(root, width=14, textvariable=from_string)
fromchoosen['values'] = ('INR','AUD','GBP','AFN')
fromchoosen.place(x=150,y=225)
fromchoosen.current(0)

to_lbl = Label(root,text="To",bg="white",font=('Times new roman',15))
to_lbl.place(x=20,y=260)

to_string = StringVar()
tochoosen = Combobox(root, width=14, textvariable=to_string)
tochoosen['values'] = ('USD','INR','AUD','GBP','AFN')
tochoosen.place(x=150,y=265)
tochoosen.current(0)

lbl_amount = Label(root,text="Amount",bg="white",font=('Times new roman',15))
lbl_amount.place(x=20,y=300)

Amount = StringVar()
entry_amount = Entry(root,bg="white",width=17,textvariable=Amount)
entry_amount.place(x=150,y=305)

convert_btn=Button(root,text="Convert",bg="white",font=('Times new roman',18),width=14,relief=FLAT,command=converter,fg="green")
convert_btn.place(x=80,y=340)

root.mainloop()


