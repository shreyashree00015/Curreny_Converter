import tkinter as tk
from tkinter import ttk
import requests


def money_conv(m, from_curr, to_curr):
    # https://exchangeratesapi.io/
    api_url = r"http://api.exchangeratesapi.io/v1/latest?access_key=7f3d13cab24a015e2e379bd82b19995b"
    result = requests.get(api_url).json()
    new_m= m /(float(result['rates'][from_curr]))
    rate = float(result['rates'][to_curr])
    return new_m * rate


def convert():
    m = int(from_curr_txt.get())
    from_curr = from_drop.get()
    to_curr = to_drop.get()
    conv_m = money_conv(m, from_curr, to_curr)

    to_curr_txt.set(round(conv_m, 2))


top = tk.Tk()
top.geometry("400x400")
top.title("Currency Convertor")
title = tk.Label(top, text="The Currency Convertor")
title.config(font=("CommercialScript BT", 50))

icon = tk.Label(top, text="Shreya's converter!", fg="purple")
icon.config(font=("Georgia",20,'underline'))

from_curr_txt = tk.StringVar()
from_curr_label = tk.Label(top, text='Enter your from Currency here:',fg="maroon",  font=('Book Antiqua', 17,'italic'))
from_curr_entry = tk.Entry(top, textvariable=from_curr_txt, font=('Book Antiqua', 18, 'normal'),bg="light grey")

to_curr_txt = tk.StringVar()
to_curr_label = tk.Label(top, text='And here it is! Your converted Currency:', fg="maroon", font=('Book Antiqua', 17, 'italic'))
to_curr_entry = tk.Entry(top, state='readonly', textvariable=to_curr_txt, font=('Book Antiqua', 18, 'normal'),bg="light grey")


conv_but = tk.Button(top, text='Let us Convert it!', command=convert, bg="navy blue", fg='white',  font=('Times New Roman', 20))

conv_opt = [ "USD","INR", "CAD", "CNY", "DKK", "EUR", "SGD","MYR","AUD","KRW","JPY"]
from_drop = ttk.Combobox(top, values=conv_opt, width=8, state="readonly")
to_drop = ttk.Combobox(top, values=conv_opt, width=8, state="readonly")

from_drop.current(0)
to_drop.current(1)

title.place(relx=0.475, rely=0.15, anchor='center')
icon.place(relx=0.85, rely=0.075, anchor='center')
from_curr_label.place(relx=0.1, rely=0.525, anchor='center')
from_curr_entry.place(in_=from_curr_label, relx=1.1)
from_drop.place(in_=from_curr_entry, relx=1.1)

to_curr_label.place(relx=0.625, rely=0.525, anchor='center')
to_curr_entry.place(in_=to_curr_label, relx=1.1)
to_drop.place(in_=to_curr_entry, relx=1.1)

conv_but.place(relx=0.49, rely=0.75, anchor='center')


top.state('zoomed')

top.mainloop()