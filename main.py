from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

def wait_for_element(driver, by, value, timeout=10):
    try:
        element = WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((by, value))
        )
        return element
    except Exception as e:
        print(f"Error: {e}")
        return None

def wikipedia_search(query, headless=True, dockerised=True):
    options = webdriver.ChromeOptions()
    options.add_argument("start-maximized")

    if headless and dockerised:
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--headless")
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
    
    if headless and (not dockerised):
        options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3")
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--headless")
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")

    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)

    driver = webdriver.Chrome(options=options)

    driver.get("https://www.wikipedia.org/")

    search_box = wait_for_element(driver, By.XPATH, "/html/body/main/div[2]/form/fieldset/div/input")
    search_box.send_keys(query)

    search_btn = wait_for_element(driver, By.XPATH, "/html/body/main/div[2]/form/fieldset/button")
    search_btn.click()

    time.sleep(5)

    try:
        first_result = wait_for_element(driver, By.XPATH, "/html/body/div[2]/div/div[3]/main/div[3]/div[3]/div[1]/p[2]")
        print(first_result.text)
    except Exception as e:
        print("Error:", e)
        driver.quit()
        return

    driver.quit()

while True:
    user_query = input("Enter your Wikipedia search query (type 'exit' to quit): ")
    if user_query.lower() == 'exit':
        break
    wikipedia_search(user_query)
