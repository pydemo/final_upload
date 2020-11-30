"""python 3/ Windows OS
Usage:
    set INSTA_USER='****@gmail.com'
    set INSTA_PWD='***'
    python fu.py
"""
import sys
from selenium import webdriver
from selenium.webdriver.chrome.options import *
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from pprint import pprint as pp
import autoit
import time
from random import randrange


e=sys.exit

home = os.path.dirname(sys.argv[0])
if not home or not home.strip('.'):
    home = os.path.dirname(os.path.abspath(__file__))


driverpath = r".\driver\nt\chromedriver_86.exe"

phototext = """
#ifinite swipe right for Tinder
"""

options = Options()
options.add_argument("--log-level=3")
options.add_argument("--silent")
#options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-logging")
options.add_argument("--mute-audio")
#mobile_emulation = {"deviceName": "Nexus 5"}
#options.add_experimental_option("mobileEmulation", mobile_emulation)
options.add_argument('--user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1')


if __name__=="__main__":
    #//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button/span/svg/path
    if 1:
        driver = webdriver.Chrome(executable_path=driverpath,options=options)
        driver.get("https://tinder.com/")
        
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/button').click()
        time.sleep(2)
        if 0:
            driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[1]/div/div[3]/span/div[3]/button/span[2]').click()
            time.sleep(1)
            phone=driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[1]/div[2]/div/input')
            phone.click()
            time.sleep(.2)
            phone.send_keys("2125183000")
            time.sleep(2)
            driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[1]/div/div[3]/span/div[1]/div/button/span[2]').click()
        
        driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[1]/div/div[3]/span/div[1]/div/button').click()
        time.sleep(2)
        if 0:
            email=driver.find_element_by_xpath('//*[@id="identifierId"]')
            email.click()
            time.sleep(.2)
            email.send_keys("olek.buzu@gmail.com")
        if 0:
            email=driver.find_elements_by_class_name("whsOnd zHQkBf");
            print(email)
            print(dir(email[0]))
            email.click()
            time.sleep(.2)
            email.send_keys("olek.buzu@gmail.com")
        #time.sleep(2)
        go = input("Continue?")
        if go=='y':
            pass
        else:
            exit(1)
        try:  #allow location
            driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]/span').click()
            time.sleep(1)
        except:
            print('Ignoring location.')
        try: #allow message notifications
            driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]/span').click()
            time.sleep(1)
        except:
            print('Ignoring message notifications.')
        try:  #accept cookies
            driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/div/div[1]/button/span').click()
            time.sleep(1)
        except:
            print('Ignoring cookies.')
        #swipe right
        time.sleep(1)
        while True:
            try:    
                print('Trying: "Upgrade Your Like"')
                driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/button[2]/span').click()
                print('Done.')
            except:
                print('Passing on "Upgrade Your Like".')
            try:
                print('Trying: "Add Tinder to your Home Screen"')
                driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/button[2]').click()
                print('Done.')
            except:
                print('Passing on "Add Tinder to your Home Screen".')

            try:
                print('Trying: #say something nice')
                add=[]
                add.append('//*[@id="modal-manager"]/div/div/div[2]/button[2]')
                add.append('//*[@id="modal-manager-canvas"]/div/div/div[1]/div/div[4]/button')
                for aid, a in enumerate(add):
                    try:
                        driver.find_element_by_xpath(a).click()
                        break
                    except:
                        print('Passing on %d' % aid)
            except:
                print('Passing on "say something nice".')
                
                        
            try: #swipe right
                driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div[2]/div[4]/button').click()
                                              
            except:
                try:
                    driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/div/main/div/div[1]/div/div[2]/div[4]/button').click()
                                                  
                except:

                    if 1:
                        go = input("Restart?")
                        if go=='y':
                            pass
                        else:
                            exit(1)
            secs = randrange(5,10) +randrange(2,10)
            print('Sleep for ', secs)
            time.sleep(secs)
            if 1: # get name
                sp=[]
                sp.append('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[1]/div[3]/div[4]/div/div[1]/div/div/span')
                sp.append('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[1]/div[3]/div[3]/div/div[1]/div/div[1]/span')
                for sid,s in enumerate(sp):
                    try:
                        span=driver.find_element_by_xpath(s)
                        print('%d: Name: %s' %  (sid,span.text))
                        break
                    except:
                        print("Passing on name: %d" % sid)
            if 1: # get age
                sp=[]
                sp.append('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[1]/div[3]/div[3]/div/div[1]/div/span[2]')
                
                for sid,s in enumerate(sp):
                    try:
                        span=driver.find_element_by_xpath(s)
                        print('%d: Age: %s' % (sid,span.text))
                        break
                    except:
                        print("Passing on age: %d" % sid)
                        
            if 1: #inspect
                b='//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[1]/div[3]/div[3]/button'
                driver.find_element_by_xpath(b).click()
                time.sleep(.5)
                b='//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[2]/div/div/div[2]/div[1]/div[2]'
                country= driver.find_element_by_xpath(b)
                print('Country:', country.text)
                
                if 1: #uninspect
                    b='//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[1]/span/a'
                    driver.find_element_by_xpath(b).click()
                    
            
            tid=2
            tabs={2:'//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[1]/div[3]/div[1]/div[2]/button[2]',
            3:'//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[1]/div[3]/div[1]/div[2]/button[3]',
            4:'//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[1]/div[3]/div[1]/div[2]/button[4]',
            5:'//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[1]/div[3]/div[1]/div[2]/button[5]',
            6:'//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[1]/div[3]/div[1]/div[2]/button[6]',
            7:'//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[1]/div[3]/div[1]/div[2]/button[7]',
            8:'//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[1]/div[3]/div[1]/div[2]/button[8]',
            9:'//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[1]/div[3]/div[1]/div[2]/button[9]',
            10:'//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[1]/div[3]/div[1]/div[2]/button[10]'}
            while True:
                try:
                    print('Trying left: %d' % tid)
                    driver.find_element_by_xpath(tabs[tid]).click()
                    print('Left ok: %d' % tid)
                    try: #try video
                        
                        driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[1]/div[3]/div[1]/div[1]/span[3]/div[2]/div').click()
                    except:
                        print('Not a video: %d' % tid)
                    tid +=1
                    time.sleep(5)
                except:
                    print('Pass on left: %d' % tid)
                    break
            time.sleep(.5)
            if 0:
                go = input("Continue?")
                if go=='y':
                    pass
                else:
                    exit(1)
