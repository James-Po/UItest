from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()

url = "https://his-test.dahuangf.com/#/login"

driver.get(url)

def login():
    driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/form/div[1]/div/div/div[2]/input').send_keys('杨江坡')

    driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/form/div[2]/div/div[1]/div[2]/input").send_keys('123456')

    driver.find_element(By.XPATH, "//input[@name='code']").send_keys('123456')

    driver.find_element(By.XPATH, "//button").click()

    sleep(10)

if __name__ == '__main__':
    login()