import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import datetime
def fun():    
    driver=webdriver.Chrome()
    driver.get('https://web.whatsapp.com/')
    time.sleep(30)
    name_in=driver.find_element_by_xpath("/html/body/div[1]/div/div/div[3]/div/div[1]/div/label/div/div[2]")
    name_in.send_keys(name)
    name_in.send_keys(Keys.ENTER)
    msg=driver.find_element_by_xpath('/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]')
    msg.send_keys(msg_msg)
    msg.send_keys(Keys.ENTER)
    for i in range(1000):
        msg=driver.find_element_by_xpath('/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]')
        msg.send_keys(msg_msg)
        msg.send_keys(Keys.ENTER)
def fun2():
    driver=webdriver.Chrome()
    driver.get('https://web.whatsapp.com/')
    time.sleep(30)
    name_in=driver.find_element_by_xpath("/html/body/div[1]/div/div/div[3]/div/div[1]/div/label/div/div[2]")
    name_in.send_keys(name)
    name_in.send_keys(Keys.ENTER)
    while True:
        time.sleep(20)
        if datetime.datetime.now().strftime("%H:%M")==ti:
            msg=driver.find_element_by_xpath('/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]')
            msg.send_keys(msg_msg)
            msg.send_keys(Keys.ENTER)
            break
        

#########################################
print('''
enter choise:
1.for repeated msges
2.automatic msg sender
''')
c=int(input())
if c==1:
    name=input('enter name who you want to send repeated msges')
    msg_msg=input('enter msg here')
    fun()
elif c==2:
    name=input('enter name who you want to send repeated msges')
    msg_msg=input('enter msg here')
    ti=input('in format hr:mm')

    fun2()





