from selenium import webdriver
import time
class Facebook(object):
    def __init__(self):
        self.Login = ''
        self.Senha = ''
        self.driver = ''
        self.Text = ''
        self.groupID = ''

    def setWebDriver(self, driver):
        self.driver = driver

    def setLogin(self, login, senha):
        self.Login = login
        self.Senha = senha

    def getLogin(self):
        return self.Login

    def setGrouopIds(self, groupsid):
        self.groupID = groupsid

    def setText(self, text):
        self.Text = text

    def start(self):

        import getpass
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--disable-infobars")
        chrome_options.add_argument("start-maximized")
        chrome_options.add_argument("user-data-dir=C:/Users/"+str(getpass.getuser())+"/AppData/Local/Google/Chrome/User Data/Default")

        path = "C:\\Program Files\\ChromeDriver\\chromedriver.exe"


        driver = webdriver.Chrome(executable_path=path, chrome_options=chrome_options)
        #driver.get(url)
        try:
            for id in self.groupID:

                url = 'https://www.facebook.com/groups/' + id
                driver.get(url)

                try:
                    driver.find_element_by_xpath('//*[@id="email"]').send_keys(self.Login)
                    driver.find_element_by_xpath('//*[@id="pass"]').send_keys(self.Senha)
                    driver.find_element_by_xpath('//*[@id="loginbutton"]').click()
                except Exception:
                    pass

                time.sleep(5)
                element = driver.find_element_by_name('xhpc_message_text')
                element.click()
                time.sleep(2)

                element = driver.find_element_by_xpath(
                    '/html/body/div[1]/div[3]/div[1]/div/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div/div[2]/div[1]/div/div/div/div[2]/div/div[1]/div/div[1]/div[2]/div/div/div/div/div/div/div[2]/div')
                element.send_keys(self.Text)

                driver.execute_script("scroll(0, +250);")
                driver.find_element_by_css_selector('._1mf7').click()
                time.sleep(5)

        finally:
            driver.close()