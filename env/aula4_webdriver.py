from selenium import webdriver
from selenium.webdriver.common.by import By


class LoginIn:

    def __init__(self,driver):
        self.NOME = (By.ID, "name123")
        self.PASS = (By.ID, "pass123")
        self.SUBMIT = (By.CSS_SELECTOR, "button[class='form_submit'][type='submit']")
        self.RESULT = (By.CSS_SELECTOR,"div.w3-border")


    def login(self,user,password):

        elem = driver.find_element(*self.NOME).send_keys(user)

        elem02 = driver.find_element(*self.PASS).send_keys(password)

        elem03 = driver.find_element(*self.SUBMIT).click()


    def validar(self,value):

        elem04 = driver.find_element(*self.RESULT)

        assert value in elem04.text

driver = webdriver.Chrome()
driver.get("file:///home/rogerio.ribeiro/Documentos/selenium-python/env/html/login.html")
driver.implicitly_wait(20)
test = LoginIn(driver)
test.login("Reinaldo","12345")
test.validar("uname=Reinaldo&psw=12345")
driver.quit()