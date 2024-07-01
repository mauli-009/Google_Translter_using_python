from tkinter import *
from tkinter import ttk  # combo box
from googletrans import Translator, LANGUAGES

def ch(text="type", src="English", dest="Hindi"):
    trans = Translator()
    tr1 = trans.translate(text, src=src, dest=dest)
    return tr1.text

def data():
    s = comb_sor.get()
    d = comb_dest.get()
    msg = src_txt.get(1.0, END).strip()
    textget = ch(text=msg, src=s, dest=d)
    dest_txt.delete(1.0, END)
    dest_txt.insert(END, textget)

win = Tk()
win.title("Translator")
win.geometry("500x700")
win.config(bg="red")

lab_txt = Label(win, text="Translator", font=("Times New Roman", 40, "bold"), bg="red", fg="black")
lab_txt.place(x=100, y=40, height=50, width=300)

lab_txt_src = Label(win, text="Source", font=("Times New Roman", 20, "bold"), bg="red", fg="black")
lab_txt_src.place(x=100, y=100, height=20, width=300)

src_txt = Text(win, font=("Times New Roman", 20, "bold"), wrap=WORD)
src_txt.place(x=10, y=130, height=200, width=480)

list_text = list(LANGUAGES.values())
comb_sor = ttk.Combobox(win, value=list_text)
comb_sor.place(x=10, y=340, height=20, width=100)
comb_sor.set("english")  # Setting default source language

button_ch = Button(win, text="Translate", relief=RAISED, command=data)
button_ch.place(x=120, y=340, height=40, width=100)

comb_dest = ttk.Combobox(win, values=list_text)
comb_dest.place(x=230, y=340, height=20, width=100)
comb_dest.set("hindi")  # Setting default destination language

lab_txt_dest = Label(win, text="Destination", font=("Times New Roman", 20, "bold"), bg="red", fg="black")
lab_txt_dest.place(x=100, y=380, height=20, width=300)

dest_txt = Text(win, font=("Times New Roman", 20, "bold"), wrap=WORD)
dest_txt.place(x=10, y=400, height=200, width=480)

win.mainloop()
