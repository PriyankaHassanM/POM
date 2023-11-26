from selenium.webdriver.common.by import By

class HomePage():
    def __init__(self,driver):
        self.driver=driver
        self.wel_xpath='//p[@class="oxd-userdropdown-name"]'
        self.logout_xpath="//a[normalize-space()='Logout']"

    def click_wel(self):
        self.driver.find_element(By.XPATH,self.wel_xpath).click()

    def click_logout(self):
        self.driver.find_element(By.XPATH,self.logout_xpath).click()
