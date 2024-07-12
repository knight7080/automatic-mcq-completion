from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import google.generativeai as genai
import time
import os

key = os.getenv('API_KEY')
print(key)


def gemini(question):
    genai.configure(api_key=key)
    model = genai.GenerativeModel('gemini-1.5-pro')
    chat = model.start_chat(history=[])
    response = chat.send_message(question + "just give me the answer no extra explanation needed")
    time.sleep(8)
    answer = response.text
    return answer


def process(driver):
    quiz_url = input("Enter the Url for the MCQ: ")
    driver.get(quiz_url)
    try:
        driver.find_element(By.XPATH, "//button[text()='" + "Attempt quiz" + "']").click()
    except:
        driver.find_element(By.XPATH, "//button[text()='" + "Continue your attempt" + "']").click()
    while True:
        time.sleep(5)
        question = driver.find_element(By.CLASS_NAME, "qtext").text
        option = driver.find_element(By.CLASS_NAME, "answer").text

        ans = gemini(question + option)
        ans = ans[0:3]
        print(ans, len(ans))
        try:
            driver.find_element(By.XPATH, "//span[text()='" + ans + "']").click()
        except:
            driver.find_element(By.XPATH, f"//label[contains(text(), '{ans}')]").click()
        time.sleep(1)
        try:
            driver.find_element(By.XPATH, '//input[@value="Next page"]').click()
        except:
            driver.find_element(By.XPATH, '//input[@value="Finish attempt ..."]').click()
            time.sleep(5)
            driver.find_element(By.XPATH, "//button[text()='" + "Submit all and finish" + "']").click()
            time.sleep(3)

            wait = WebDriverWait(driver, 10)
            modal = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='modal-dialog modal-dialog-scrollable']")))

            submit_button = modal.find_element(By.XPATH, "//button[@data-action='save']")
            submit_button.click()
            break
