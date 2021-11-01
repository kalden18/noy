from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Edge("c:/users/kalden/documents/msedgedriver.exe")
driver.get("https://www.youtube.com/user/peradze94")
assert "Soccer Stories - Oh My Goal - YouTube" in driver.title

continue_link = driver.find_element(By.TAG_NAME,'span')
elem = driver.find_element(By.CLASS_NAME,'style-scope ytd-video-meta-block').text
channel= driver.find_element(By.TAG_NAME,'title').text
v=str(elem)
if "month" in v :
    print("no new videos from"+str(channel))
elif "hour" or"minutes" or"hours" or 'days' in v:
    print("new videos from")  
       
