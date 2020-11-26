from selenium import webdriver
import botengine

chromedriver_path = r'C:\Users\user\Downloads/chromedriver.exe' 
webdriver = webdriver.Chrome(executable_path=chromedriver_path)

botengine.init(webdriver)
botengine.follow_people(webdriver)

webdriver.close()