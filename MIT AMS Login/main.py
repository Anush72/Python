from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


# making chrome open after the process has ended, as quit command is not send to driver
options = webdriver.ChromeOptions()
options.add_experimental_option("detach",True)

# making driver and login to ams of MIT
driver = webdriver.Chrome(options=options)
driver.get('https://ams.mit.edu.au/')


# login to ams
username = input('Write Username of AMS:\t')
password = input('Write Password of AMS:\t')
user_element = driver.find_element(By.ID,value="Username")
user_element.send_keys(username)
password_element = driver.find_element(By.ID,value='Password')
password_element.send_keys(password)
password_element.send_keys(Keys.ENTER)
time.sleep(3)

print('Use short form  of options as mentioned')
user_seletion = input("Where  you want to go to :\n ['Time Table(TT)','Assignment Details'(AD),'Attendance'(A) or 'Course Units'(CU)]\n")

# Navigating the browser as user said
if user_seletion == 'TT':
    timetable = driver.find_element(By.LINK_TEXT,value='View all timetables')
    timetable.click()
elif user_seletion =='AD':
    academics = driver.find_element(By.XPATH,value='//*[@id="accordionFlush"]/div[2]/button')
    academics.click()
    assignment = driver.find_element(By.XPATH,value='//*[@id="academics-flush"]/div/a[1]')
    time.sleep(3)
    assignment.click()
elif user_seletion == 'A':
    timetable = driver.find_element(By.XPATH, value='//*[@id="accordionFlush"]/div[3]/button')
    timetable.click()
    time.sleep(3)
    attendance = driver.find_element(By.XPATH,value='//*[@id="timetables-flush"]/div/a[2]')
    attendance.click()
elif user_seletion == 'CU':
    academics = driver.find_element(By.XPATH, value='//*[@id="accordionFlush"]/div[2]/button')
    academics.click()
    time.sleep(3)
    course = driver.find_element(By.XPATH,value = '//*[@id="academics-flush"]/div/a[2]')
    course.click()





