from selenium import webdriver

driver = webdriver.Chrome(executable_path='driver/chromedriver.exe')
driver.get("https://botanikabeauty.com/")

#return policy
returnpolicybtn = driver.find_element_by_xpath("//a[contains(@href, '/pages/return-policy')]")
returnpolicybtn.click()