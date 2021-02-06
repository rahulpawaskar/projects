import pyshorteners as s
import tkinter as tk
def fun():
    obj=s.Shortener()
    short_url=obj.tinyurl.short(entry1.get())
    print(short_url)
    ent=tk.Entry(window)
    ent.insert(tk.END,short_url)
    ent.pack()
window=tk.Tk()
entry1=tk.Entry(window)
label1=tk.Label(window, text='enter url')
but=tk.Button(window, text='create', command=fun)
entry1.pack()
label1.pack()
but.pack()
