from selenium import webdriver

driver = webdriver.Chrome(executable_path='driver/chromedriver.exe')
driver.get("https://botanikabeauty.com/")

#instagram icon
instagramicon = driver.find_element_by_xpath("//li[3]/a/i")
instagramicon.click()