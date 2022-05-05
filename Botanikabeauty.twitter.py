from selenium import webdriver

driver = webdriver.Chrome(executable_path='driver/chromedriver.exe')
driver.get("https://botanikabeauty.com/")

#twitter icon
twittericon = driver.find_element_by_xpath("//li[2]/a/i")
twittericon.click()