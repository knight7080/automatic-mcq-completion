from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()
chrome_options.add_argument('--headless')


def connect():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("https://lms2.ai.saveetha.in/login/index.php")

    rno = "21003975"
    pas = "h85153"
    u_btn = driver.find_element(By.NAME, "username")
    u_btn.send_keys(rno)
    p_btn = driver.find_element(By.NAME, "password")
    p_btn.send_keys(pas)
    time.sleep(4)
    driver.find_element(By.ID, "loginbtn").click()
    time.sleep(10)

    return driver
