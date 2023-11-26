from selenium.webdriver.common.by import By

class LoginPage():
    def __init__(self, driver):
        self.driver = driver
        self.user_tb_xpath ="//input[@placeholder='Username']"
        self.pwd_tb_xpath="//input[@placeholder='Password']"
        self.login_button_xpath="//button[@type='submit']"
        self.war_msg_xpath="//p[@class='oxd-text oxd-text--p oxd-alert-content-text']"

    def enter_username(self,un):
        self.driver.find_element(By.XPATH,self.user_tb_xpath).clear()
        self.driver.find_element(By.XPATH,self.user_tb_xpath).send_keys(un)
      
    def enter_pwd(self,password):
        self.driver.find_element(By.XPATH,self.pwd_tb_xpath).clear()
        self.driver.find_element(By.XPATH,self.pwd_tb_xpath).send_keys(password)
      
    def click_login(self):
        self.driver.find_element(By.XPATH,self.login_button_xpath).click()

    def check_invalid_user(self):
        msg=self.driver.find_element(By.XPATH,self.war_msg_xpath).text
        return msg


