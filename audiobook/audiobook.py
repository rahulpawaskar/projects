import threading
import pyttsx3
import PyPDF2
import tkinter as tk
import time
class funs:

    def fun(self):
        book = open(et.get(),'rb')
        pdf_reader = PyPDF2.PdfFileReader(book)
        num_pages = pdf_reader.numPages
        self.play = pyttsx3.init()
        frame1.pack()
        time.sleep(3)
        frame1.pack()
       
        print('Playing')

        for num in range(num_pages):
                page = pdf_reader.getPage(num)
                data = page.extractText()

                self.play.say(data)
                self.play.runAndWait()
    def fun2(self):
        
        window.destroy()
        exit()
a=funs()
window=tk.Tk()
frame1=tk.Frame(window)
label1=tk.Label(window,text='paste your book path here')
label2=tk.Label(frame1,text='--------playing--------')
et=tk.Entry(window)
funthread=threading.Thread(target=a.fun)
but=tk.Button(window,text='start',command=funthread.start)
qt=tk.Button(window,text='quit',command=a.fun2)
et.pack()
label1.pack()
but.pack()
qt.pack()
window.mainloop()

        




