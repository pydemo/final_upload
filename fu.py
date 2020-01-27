import sys
from selenium import webdriver
from selenium.webdriver.chrome.options import *
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from pprint import pprint as pp
import autoit
import time
e=sys.exit

home = os.path.dirname(sys.argv[0])
if not home or not home.strip('.'):
	home = os.path.dirname(os.path.abspath(__file__))


INSTA_USER  = os.environ.get('INSTA_USER')
INSTA_PWD 	= os.environ.get('INSTA_PWD')

assert INSTA_USER
assert INSTA_PWD


if 1:
	username = INSTA_USER.strip("'").strip('"')
	passwd = INSTA_PWD.strip("'").strip('"')
	
driverpath = r".\driver\chromedriver.exe"

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
driver = webdriver.Chrome(executable_path=driverpath,options=options)
def login(driver):
	driver.get("https://www.instagram.com/accounts/login/?hl=en")
	time.sleep(3)
	driver.find_element_by_xpath("//*[@id='react-root']/section/main/article/div/div/div/form/div[4]/div/label/input").send_keys(username)
	time.sleep(0.5)
	driver.find_element_by_xpath("//*[@id='react-root']/section/main/article/div/div/div/form/div[5]/div/label/input").send_keys(passwd)
	time.sleep(0.5)
	driver.find_element_by_xpath("//*[@id='react-root']/section/main/article/div/div/div/form/div[7]/button/div").click()
	time.sleep(3)
	driver.find_element_by_xpath("//*[@id='react-root']/div/div[2]/a[2]").click()
	#driver.find_element_by_xpath("//*[@id='react-root']/section/main/article/div/div/div/form/div/div[2]/a[@title = 'Not Now']").click()
	#//*[@id="react-root"]/div/div[2]/a[2
	time.sleep(3)
	driver.find_element_by_xpath("/html/body/div[2]/div/div/div[3]/button[2]").click()
	
	if 0:
		while 1:
			time.sleep(1)
			print(1)
			try:
				driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/button").click()
				break
			except:
				pass
		while 1:
			time.sleep(1)
			print(2)
			try:
				driver.find_element_by_xpath("/html/body/div[3]/div/div/div[3]/button[2]").click()
				break
			except:
				pass
		while 1:
			time.sleep(1)
			print(3)
			driver.find_element_by_css_selector('body').send_keys(Keys.PAGE_DOWN)
			try:
				driver.find_element_by_xpath("/html/body/div[3]/div/div/div[3]/button[2]").click()
				break
			except:
				pass
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
	if 0:
		driver.find_element_by_xpath("//*[@id='react-root']/section/div[2]/section[1]/div[2]/textarea").send_keys(phototext)
		time.sleep(1)
		
	driver.find_element_by_xpath("//*[@id='react-root']/section/div[1]/header/div/div[2]/button").click()
if __name__=="__main__":
	login(driver)

	photopath = os.path.join(home, r"images\DSC02225.JPG" )
	upload(driver,phototext, photopath)
	time.sleep(30)
	driver.close()