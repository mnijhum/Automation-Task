
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re


class AutomationTest(unittest.TestCase):



    def __init__(self):
        s = Service('C:/Users/Mushfikunnabi Nijhum/Desktop/Automation_Task/chromedriver.exe')
        self.driver = webdriver.Chrome(service=s)
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def create_account(self, emails):
        driver = self.driver
        driver.get("http://automationpractice.com/index.php")
        for email in emails:
            driver.find_element(By.LINK_TEXT,"Sign in").click()
            driver.find_element(By.ID,"email_create").click()
            driver.find_element(By.ID,"email_create").clear()
            driver.find_element(By.ID,"email_create").send_keys(email)
            driver.find_element(By.XPATH,"//button[@id='SubmitCreate']/span").click()
            driver.find_element(By.ID,"id_gender1").click()
            driver.find_element(By.ID,"customer_firstname").click()
            driver.find_element(By.ID,"customer_firstname").clear()
            driver.find_element(By.ID,"customer_firstname").send_keys("M")
            driver.find_element(By.ID,"customer_lastname").click()
            driver.find_element(By.ID,"customer_lastname").clear()
            driver.find_element(By.ID,"customer_lastname").send_keys("Nijhum")
            driver.find_element(By.ID,"passwd").clear()
            driver.find_element(By.ID,"passwd").send_keys("123456789")
            driver.find_element(By.ID,"address1").click()
            driver.find_element(By.ID,"address1").clear()
            driver.find_element(By.ID,"address1").send_keys("Texas")
            driver.find_element(By.ID,"city").click()
            driver.find_element(By.ID,"city").clear()
            driver.find_element(By.ID,"city").send_keys("Texas")
            driver.find_element(By.ID,"id_state").click()
            Select(driver.find_element(By.ID,"id_state")).select_by_visible_text("Texas")
            driver.find_element(By.ID,"postcode").click()
            driver.find_element(By.ID,"postcode").clear()
            driver.find_element(By.ID,"postcode").send_keys("75216")
            driver.find_element(By.ID,"id_country").click()
            driver.find_element(By.ID,"id_country").click()
            driver.find_element(By.ID,"phone_mobile").click()
            driver.find_element(By.ID,"phone_mobile").clear()
            driver.find_element(By.ID,"phone_mobile").send_keys("01716833177")
            driver.find_element(By.XPATH,"//form[@id='account-creation_form']/div[2]/p[13]").click()
            driver.find_element(By.ID,"alias").click()
            driver.find_element(By.ID,"alias").clear()
            driver.find_element(By.ID,"alias").send_keys("Test Address")
            driver.find_element(By.XPATH,"//button[@id='submitAccount']/span").click()
            driver.find_element(By.LINK_TEXT, "Sign out").click()
            driver.find_element(By.XPATH, "//img[@alt='My Store']").click()
            time.sleep(3)
    def order(self, emails):
        driver = self.driver

        for email in emails:
            driver.find_element(By.LINK_TEXT,"Sign in").click()
            driver.find_element(By.ID,"email").click()
            driver.find_element(By.ID,"email").clear()
            driver.find_element(By.ID,"email").send_keys(email)
            driver.find_element(By.ID,"passwd").click()
            driver.find_element(By.ID,"passwd").clear()
            driver.find_element(By.ID,"passwd").send_keys("123456789")
            time.sleep(3)
            driver.find_element(By.XPATH,"//button[@id='SubmitLogin']/span").click()
            driver.find_element(By.XPATH,"//div[@id='block_top_menu']/ul/li[2]/a").click()
            driver.find_element(By.XPATH,"//div[@id='subcategories']/ul/li/h5/a").click()
            driver.find_element(By.XPATH,"//img[@alt='Printed Dress']").click()
            driver.find_element(By.XPATH,"//p[@id='add_to_cart']/button/span").click()
            driver.find_element(By.XPATH,"//div[@id='layer_cart']/div/div[2]/div[4]/span/span").click()
            driver.find_element(By.XPATH,"//div[@id='block_top_menu']/ul/li[3]/a").click()
            driver.find_element(By.ID,"layered_id_attribute_group_14").click()
            driver.find_element(By.XPATH,"//img[@alt='Faded Short Sleeve T-shirts']").click()
            driver.find_element(By.ID,"color_14").click()
            driver.find_element(By.XPATH,"//p[@id='add_to_cart']/button/span").click()
            driver.find_element(By.XPATH,"//div[@id='layer_cart']/div/div[2]/div[4]/a/span").click()
            driver.find_element(By.XPATH,"//div[@id='center_column']/p[2]/a/span").click()
            driver.find_element(By.XPATH,"//div[@id='center_column']/form/p/button/span").click()
            driver.find_element(By.ID,"cgv").click()
            driver.find_element(By.XPATH,"//form[@id='form']/p/button/span").click()
            driver.find_element(By.XPATH,"//div[@id='HOOK_PAYMENT']/div[2]/div/p/a/span").click()
            driver.find_element(By.LINK_TEXT,"Sign out").click()
            driver.find_element(By.XPATH,"//img[@alt='My Store']").click()
            time.sleep(3)

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
        


emails = ['testemail300mn@gmail.com', 'testemail400mn@gmail.com'] #please give any two email if already registered
at = AutomationTest()
at.create_account(emails)
at.order(emails)

