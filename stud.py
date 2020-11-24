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


INSTA_USER  = os.environ.get('INSTA_USER')
INSTA_PWD 	= os.environ.get('INSTA_PWD')

#assert INSTA_USER
#assert INSTA_PWD

import traceback
try:
    import cStringIO
except ImportError:
    import io as cStringIO
    

if 0:
    username = INSTA_USER.strip("'").strip('"')
    passwd = INSTA_PWD.strip("'").strip('"')
    
driverpath = r".\driver\nt\chromedriver_86.exe"

phototext = """
#finalupload
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

def login(driver):
    driver.get("https://www.instagram.com/accounts/login/?hl=en")
    time.sleep(3)
    driver.find_element_by_xpath("//*[@id='loginForm']/div[1]/div[3]/div/label/input").send_keys(username)
    time.sleep(0.5)
    driver.find_element_by_xpath("//*[@id='loginForm']/div[1]/div[4]/div/label/input").send_keys(passwd)
    time.sleep(0.5)
    driver.find_element_by_xpath("//*[@id='loginForm']/div[1]/div[6]/button/div").click()
    time.sleep(3)
    save_login= None
    #e()
    if 1: 
        try:
            print('--------get app-------------------')
            driver.find_element_by_xpath("//*[@id='react-root']/div/div[2]/a[2]").click()
        except:
            err_log = cStringIO.StringIO()
            traceback.print_exc(file=err_log)
            err = err_log.getvalue()
            print(err)
        
        
        
    if 0:
        try:
            save_login = driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/section/div/div[2]")
            pp(dir(save_login))
        except:
            err_log = cStringIO.StringIO()
            traceback.print_exc(file=err_log)
            err = err_log.getvalue()
            print(err)
    if 0:
        if save_login:
            sli = 'Save Your Login Info?'
            if save_login.text == sli:
                #Not now
                 driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/button').click()
            else:
                raise Exception('Expecting "%s", got "%s".' % (sli, save_login.text))
    #Add Instagram to your Home screen?
    try:
        print('--------Cancel-------------------')
        time.sleep(2)
        driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div[3]/button[2]').click()
        
        #body > div.RnEpo.Yx5HN > div > div > div > div.mt3GC > button.aOOlW.HoLwm
        #<button class="aOOlW   HoLwm " tabindex="0">Cancel</button>
        #driver.findElementByClassName("aOOlW   HoLwm ").click();
    except:
        err_log = cStringIO.StringIO()
        traceback.print_exc(file=err_log)
        err = err_log.getvalue()
        print(err)
    try:
        time.sleep(1)
        driver.find_element_by_xpath("//*[@id='react-root']/div/div[2]/a[2]").click()
    except:
        err_log = cStringIO.StringIO()
        traceback.print_exc(file=err_log)
        err = err_log.getvalue()
        print(err)
    #driver.find_element_by_xpath("//*[@id='react-root']/section/main/article/div/div/div/form/div/div[2]/a[@title = 'Not Now']").click()
    #//*[@id="react-root"]/div/div[2]/a[2
    try:
        time.sleep(1)
        driver.find_element_by_xpath("/html/body/div[2]/div/div/div[3]/button[2]").click()
    except:
        err_log = cStringIO.StringIO()
        traceback.print_exc(file=err_log)
        err = err_log.getvalue()
        print(err)
def upload(driver,phototext, photopath):

    driver.find_element_by_xpath("//div[@role='menuitem']").click()
    time.sleep(1.5)
    
    autoit.win_active("Open") #open can change by your os language if not open change that
    time.sleep(2)
    autoit.control_send("Open", "Edit1", photopath)
    time.sleep(1.5)
    autoit.control_send("Open", "Edit1", "{ENTER}")
    time.sleep(2)
    driver.find_element_by_xpath("//*[@id='react-root']/section/div[1]/header/div/div[2]/button").click()
    time.sleep(1)
    
    ta= driver.find_elements(By.XPATH, '//textarea')
    
    for part in phototext.split('\n'):
        pp (part)
        if part:
            ta[0].send_keys(part)
            ActionChains(driver).key_down(Keys.SHIFT).key_down(Keys.ENTER).key_up(Keys.SHIFT).key_up(Keys.ENTER).perform()
        else:
            pass
    time.sleep(1)
        
    driver.find_element_by_xpath("//*[@id='react-root']/section/div[1]/header/div/div[2]/button").click()
if __name__=="__main__":
    #//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button/span/svg/path
    if 1:
        driver = webdriver.Chrome(executable_path=driverpath,options=options)
        driver.get("https://tinder.com/")
        
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/header/div[1]/div[2]/div/button').click()
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[1]/div/div[3]/span/div[3]/button/span[2]').click()
        time.sleep(1)
        phone=driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[1]/div[2]/div/input')
        phone.click()
        time.sleep(.2)
        phone.send_keys("2125183000")
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[1]/button/span').click()
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
                driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/div/main/div/div[1]/div/div[2]/div[4]/button').click()
                                              
            except:
                try:
                    driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button').click()
                                                  
                except:

                    try:
                        driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/button[2]/span').click()
                    except:
                        print('Passing on "Upgrade Your Like".')
                        try:
                            driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/button[2]/span').click()
                        except:
                            print('Passing on "Add Tinder to your Home Screen".')
                            secs = randrange(10) +1
                            print('Restarting in', secs)
                            time.sleep(randrange(10))
            secs = randrange(60) +5*randrange(10)
            print('Sleep for ', secs)
            time.sleep(secs)

    if 0:
        driver.close()
    if 0:
        login(driver)

        photopath = os.path.join(home, r"images\DSC02225.JPG" )
        upload(driver,phototext, photopath)
    if 0:
        #Turn on notifications
        try:
            
            #Not now 
            time.sleep(5)
            driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[2]").click()
            #time.sleep(10)
            print('Done.')
        except:
            err_log = cStringIO.StringIO()
            traceback.print_exc(file=err_log)
            err = err_log.getvalue()
            print(err)
    
    if 0:
        driver.close()