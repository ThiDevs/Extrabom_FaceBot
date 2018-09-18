from selenium import webdriver
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--disable-infobars")
chrome_options.add_argument("start-maximized")
chrome_options.add_argument("user-data-dir=C:/Users/thiago.alves/AppData/Local/Google/Chrome/User Data/Default")

groupID = ['1889352911359628','1157882024305526']
for id in groupID:

    url = 'https://www.facebook.com/groups/' + id
    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.get(url)

    try:
        try:
            driver.find_element_by_xpath('//*[@id="email"]').send_keys('thiagofelicio@hotmail.com')
            driver.find_element_by_xpath('//*[@id="pass"]').send_keys('Thiago&991010')
            driver.find_element_by_xpath('//*[@id="loginbutton"]').click()
        except Exception:
            pass

        time.sleep(5)
        element = driver.find_element_by_name('xhpc_message_text')
        element.click()
        time.sleep(2)#js_1us

        element = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[1]/div/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div/div[2]/div[1]/div/div/div/div[2]/div/div[1]/div/div[1]/div[2]/div/div/div/div/div/div/div[2]/div')
        element.send_keys('teste')

        driver.execute_script("scroll(0, +250);")
        driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[1]/div/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div/div[2]/div[1]/div/div/div/div[2]/div/div[3]/div[3]/div/div[2]/div/div[2]/span/button').click()




        time.sleep(5)
    finally:
        driver.close()
