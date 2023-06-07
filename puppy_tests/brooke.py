from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
import config as cfg
from selenium import webdriver

driver: WebDriver = webdriver.Chrome()
driver.implicitly_wait(30)
driver.maximize_window()
driver.get(cfg.page_config["URL"])
driver.find_element(By.XPATH, ".//*[@action='/puppies/4']").click()
driver.find_element(By.XPATH, ".//input[@value='Adopt Me!']").click()
driver.find_element(By.XPATH, ".//*[@id='toy']").click()
driver.find_element(By.XPATH, ".//*[@id='carrier']").click()
driver.find_element(By.XPATH, ".//input[@value='Complete the Adoption']").click()
driver.find_element(By.XPATH, ".//*[@id='order_name']").send_keys(cfg.page_config["username"])
driver.find_element(By.XPATH, ".//*[@id='order_address']").send_keys(cfg.page_config["address"])
driver.find_element(By.XPATH, ".//*[@id='order_email']").send_keys(cfg.page_config["email"])
driver.find_element(By.XPATH, ".//*[@id='order_pay_type']").click()
driver.find_element(By.XPATH, ".//*[@id='order_pay_type']/option[2]").click()
driver.find_element(By.XPATH, ".//*[@id='new_order']/div[5]/button/input").click()
element = driver.find_element(By.XPATH, ".//*[@id='notice']").text
assert element == 'Thank you for adopting a puppy!'
driver.quit()
