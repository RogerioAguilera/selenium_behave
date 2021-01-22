import requests
from selenium.webdriver import DesiredCapabilities
from selenium import webdriver

def instanciar_driver():
    caps = DesiredCapabilities.CHROME
    caps["marionete"] = True
    caps["binary"]
    driver = webdriver.Chrome(capabilities=caps)

def carregando_url(webdriver,url):
    webdriver.set_page_load_timeout(30)
    webdriver.get(url)
    url = requests.get(url)
    print(url.status_code)

webdriver = instanciar_driver
teste = carregando_url(webdriver, "http://reinaldorossetti.blogspot.com.br/")
assert teste == 200, "Erro ao carregar a página"