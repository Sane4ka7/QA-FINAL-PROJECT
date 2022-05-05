from selenium import webdriver

driver = webdriver.Chrome(executable_path='driver/chromedriver.exe')
driver.get("https://botanikabeauty.com/")

#terms of service
termsofservicebtn = driver.find_element_by_xpath("//a[contains(@href, '/pages/terms-of-service')]")
termsofservicebtn.click()



