from selenium import webdriver

driver = webdriver.Chrome(executable_path='driver/chromedriver.exe')
driver.get("https://botanikabeauty.com/")

#facebook icon
facebookicon = driver.find_element_by_xpath("//i")
facebookicon.click()