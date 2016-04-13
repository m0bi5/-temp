# .----------------.  .----------------.  .----------------.  .----------------.  .----------------. 
#| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |
#| |     ____     | || |  _________   | || |  _________   | || | ____    ____ | || |   ______     | |
#| |   .' __ \    | || | |  _   _  |  | || | |_   ___  |  | || ||_   \  /   _|| || |  |_   __ \   | |
#| |  / .'  \ |   | || | |_/ | | \_|  | || |   | |_  \_|  | || |  |   \/   |  | || |    | |__) |  | |
#| |  | | (_/ |   | || |     | |      | || |   |  _|  _   | || |  | |\  /| |  | || |    |  ___/   | |
#| |  \ `.__.'\   | || |    _| |_     | || |  _| |___/ |  | || | _| |_\/_| |_ | || |   _| |_      | |
#| |   `.___ .'   | || |   |_____|    | || | |_________|  | || ||_____||_____|| || |  |_____|     | |
#| |              | || |              | || |              | || |              | || |              | |
#| '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |
# '----------------'  '----------------'  '----------------'  '----------------'  '----------------' 


#Headers
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

#Login Credentials
email=""
password=""

#Browser for facebook access
browser=webdriver.Chrome(executable_path="C:\chromedriver.exe")                                  
browser.set_window_position(-1000,-1000)#........................................................Hide the window

def getTemp():
    temp=webdriver.Chrome(executable_path="C:\chromedriver.exe")
    temp.set_window_position(-1000,-1000)#.......................................................Hide the window
    temp.get("http://google.com/#q=weather")
    time.sleep(2)#...............................................................................Wait for element to load
    weather=temp.find_element_by_id("wob_tm")
    response=weather.text+" °C"
    temp.quit()
    return response

def login():
    browser.get("https://facebook.com")
    inputs=browser.find_elements_by_tag_name('input')
    inputs[1].send_keys(email)
    inputs[2].send_keys(password)
    time.sleep(2)#...............................................................................Wait for element to load
    inputs[3].click()
    browser.get("https://messenger.com")
    time.sleep(2)
    browser.find_elements_by_tag_name("button")[0].click()
    
def getLatestMessage():
    while True:
        time.sleep(1)#............................................................................Wait for element to load
        browser.find_elements_by_tag_name("a")[3].click()
        time.sleep(1)#............................................................................Wait for element to load
        msg=browser.find_elements_by_class_name("_o46")[-1]#......................................Get Last message
        print(msg.text)
        if (msg.text)=="@temp":
            response=getTemp()
            browser.find_elements_by_class_name("_5rpu")[0].send_keys(response)
            browser.find_elements_by_class_name("_5rpu")[0].send_keys(Keys.RETURN)#...............Send response

#Function calls
login()
getLatestMessage()
