from selenium import webdriver

driver = webdriver.Chrome(executable_path='driver/chromedriver.exe')
driver.get("https://botanikabeauty.com/")

#about us
aboutusbtn = driver.find_element_by_xpath("//a[contains(text(),'About Us')]")
aboutusbtn.click()

