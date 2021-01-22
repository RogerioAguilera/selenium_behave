from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://www.google.com.br/")

element = driver.find_element_by_tag_name("input[name=\"btnI\"]")

value_button = element.get_attribute('value')

assert "estou com sorte" == value_button.lower()

driver.quit()

