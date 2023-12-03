from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginTestCase(TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)
        
    def tearDown(self):
        self.driver.quit()
    def test_login(self):
        self.driver.get('http://127.0.0.1:8000/login_form/')
        
        email_input = self.driver.find_element(By.ID,'email')
        password_input = self.driver.find_element(By.ID,'password')
        login_button = self.driver.find_element(By.ID,'login')
        
        
        email_input.send_keys('sharipriya531@gmail.com')
        password_input.send_keys('sreekutty@23')
        login_button.click()     
         

# Create your tests here.
