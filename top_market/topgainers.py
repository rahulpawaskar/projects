import requests
import bs4
import time
import datetime
import csv
import pandas
import win10toast
import tkinter as tk
from tkinter import ttk
import selenium
from selenium.webdriver.common.keys import Keys
from selenium import webdriver

top_gainers=[]
top_open=[]
top_close=[]
length=0
def to_wa():
    
    def sub():
        a=name.get()
        li1.append(a)
        name.delete(0, 'end')
        temp_lab=ttk.Label(popup, text=a)
        temp_lab.pack()
    def go_ahead():
        label.pack()
        name.pack()
        b2.pack()
        b4.pack()
        b5.pack()

    global li1
    li1=[]
    popup = tk.Tk()
    popup.wm_title("whatsapp share")
    label = ttk.Label(popup, text='enter name')
    name=tk.Entry(popup)
    msg_label=ttk.Label(popup, text='wanna share on whatsapp?')
    b1=ttk.Button(popup, text="yes", command =go_ahead)
    b2=ttk.Button(popup, text="no", command =popup.destroy)
    b3=ttk.Button(popup, text="quit/proceed", command = popup.destroy)
    b4=ttk.Button(popup, text="submit", command =sub)
    b5=ttk.Button(popup, text="proceed", command =proceed)
    msg_label.pack()  
    b1.pack()
    b2.pack()
    popup.mainloop()
def proceed():
    popup = tk.Tk()
    popup.wm_title("scan qr and wait")
    driver=webdriver.Chrome()
    driver.get('https://web.whatsapp.com/')
    msg=ttk.Label(popup, text='scan qr within 30 and wait')
    msg.pack()
    time.sleep(30)
    for i in range(len(li1)):
        name_in=driver.find_element_by_xpath("/html/body/div[1]/div/div/div[3]/div/div[1]/div/label/div/div[2]")
        name_in.send_keys('{}'.format(li1[i]))
        name_in.send_keys(Keys.ENTER)
        for j in range(len(top_gainers)):
            msg2=driver.find_element_by_xpath('/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]')
            msg2.send_keys('{} open with {} |||| closed with {}'.format(top_gainers[j],top_open[j],top_close[j]))
            msg2.send_keys(Keys.ENTER)

def pop_up():
    popup = tk.Tk()
    popup.wm_title("!")
    label = ttk.Label(popup, text=msg, font=NORM_FONT)
    label.pack(side="top", fill="x", pady=10)
    B1 = ttk.Button(popup, text="Okay", command = popup.destroy)
    B1.pack()
    popup.mainloop()
def noti():
    toaster = win10toast.ToastNotifier()
    toaster.show_toast("data uploaded in database", "your data is uploaded respond to pop up to share on whatsapp", threaded=True)
def data_of_top():
    rs=requests.get('https://money.rediff.com/gainers/nse/daily/nifty')
    sp=bs4.BeautifulSoup(rs.content,"html5lib")
    tb=sp.find('tbody')
    trs=tb.find_all('tr')

    tb=sp.find('tbody')
    trs=tb.find_all('tr')
    for i in range(len(trs)): # to get names of top gainers
        a=trs[i].find('a').text
        top_gainers.append(a)
    for i in range(len(trs)): # to get top gainers open
        for i in trs[i].find_all('td')[1::3]:
            top_open.append(i.text)
            
    for i in range(len(trs)): # to get top gainers close
        for i in trs[i].find_all('td')[2::2]:
            top_close.append(i.text)
        

    for i in range(len(trs)): #to remove extra tabs and spaces
        top_gainers[i]=top_gainers[i][6:-6]
    global length
    length=len(trs)
    print(top_gainers)
    print(top_open)
    print(top_close)

def check_time(now):
    if now>'16:00':
        print('ala bhava')
        return True
while True:
    n=datetime.datetime.now()
    now=n.strftime("%H:%M") 
    if check_time(now)==True:
        dt=datetime.date.today()
        data_of_top()
        with open('e://desktop/pro/top_market/market.csv','a',
                  newline='') as adder:
            writer=csv.writer(adder)
            for i in range(length):
                writer.writerow([dt,top_gainers[i],top_open[i],top_close[i]])
        noti()
        to_wa()
        break
    else:
        time.sleep(60)

