import logging
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

# Configure logging to display detailed logs in terminal
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger()

# Set up WebDriver
def setup_driver():
    driver_path = r"C:\Users\ibrah\Downloads\chromedriver.exe"
    chrome_options = Options()
    chrome_options.add_argument("--disable-gpu")
    service = Service(driver_path)
    driver = webdriver.Chrome(service=service)
    logger.info("WebDriver setup completed")
    return driver

# Test Case 1: Login Test - Valid Credentials
def test_login_valid_credentials():
    driver = setup_driver()
    logger.info("Test started: test_login_valid_credentials")
    
    try:
        # Open the login page
        driver.get("https://app.vwo.com/#/login")
        logger.info("Navigated to the login page")

        # Wait for the email input field and enter email
        email_field = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@type='email']"))
        )
        email_field.send_keys("test2002@gmail.com")
        logger.info("Entered email: test2002@gmail.com")
        
        # Wait for the password field and enter password
        password_field = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@type='password']"))
        )
        password_field.send_keys("tnB!p5Ce@qXCyLq")
        logger.info("Entered password: tnB!p5Ce@qXCyLq")
        
        # Wait for the sign-in button to be clickable and click it
        login_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.ID, "js-login-btn"))
        )
        login_button.click()
        logger.info("Clicked the Sign-In button")
        
        # Wait for the dashboard or next page to load
        dashboard_element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "main-page"))  # Replace with actual element ID
        )
        if dashboard_element:
            logger.info("Test passed: Successfully navigated to the dashboard")

    except Exception as e:
        logger.error(f"Test failed: {str(e)}")

    finally:
        driver.quit()
        logger.info("WebDriver session ended")


        # Test Case 2: Login Test - Invalid Credentials (Incorrect Email)
def test_login_invalid_email():
    driver = setup_driver()
    logger.info("Test started: test_login_invalid_email")
    
    try:
        # Open the login page
        driver.get("https://app.vwo.com/#/login")
        logger.info("Navigated to the login page")

        # Wait for the email input field and enter invalid email
        email_field = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@type='email']"))
        )
        email_field.send_keys("wrongemail@gmail.com")
        logger.info("Entered email: wrongemail@gmail.com")
        
        # Wait for the password field and enter valid password
        password_field = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@type='password']"))
        )
        password_field.send_keys("tnB!p5Ce@qXCyLq")
        logger.info("Entered password: tnB!p5Ce@qXCyLq")
        
        # Wait for the sign-in button to be clickable and click it
        login_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.ID, "js-login-btn"))
        )
        login_button.click()
        logger.info("Clicked the Sign-In button")
        
        # Wait for the error message to appear
        error_message = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.ID, "js-notification-box-msg"))
        )
        error_text = error_message.text.strip()
        
        # Verify the error message text
        expected_error = "Your email, password, IP address or location did not match"
        if error_text == expected_error:
            logger.info(f"Test passed: Correct error message displayed - '{error_text}'")
        else:
            logger.error(f"Test failed: Unexpected error message - '{error_text}'")
    
    except Exception as e:
        logger.error(f"Test failed: {str(e)}")
    
    finally:
        driver.quit()
        logger.info("WebDriver session ended")

# Test Case 3: Invalid Login - Incorrect Password
def test_login_invalid_password():
    driver = setup_driver()
    logger.info("Test started: test_login_invalid_password")

    try:
        # Open the login page
        driver.get("https://app.vwo.com/#/login")
        logger.info("Navigated to the login page")

        # Enter valid email and incorrect password
        email_field = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@type='email']"))
        )
        email_field.send_keys("test2002@gmail.com")
        logger.info("Entered valid email: test2002@gmail.com")

        password_field = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@type='password']"))
        )
        password_field.send_keys("wrongpassword")
        logger.info("Entered invalid password: wrongpassword")

        login_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.ID, "js-login-btn"))
        )
        login_button.click()
        logger.info("Clicked the Sign-In button")
        
       # Wait for the error message to appear
        error_message = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.ID, "js-notification-box-msg"))
        )
        error_text = error_message.text.strip()
        
        # Verify the error message text
        expected_error = "Your email, password, IP address or location did not match"
        if error_text == expected_error:
            logger.info(f"Test passed: Correct error message displayed - '{error_text}'")
        else:
            logger.error(f"Test failed: Unexpected error message - '{error_text}'")

    except Exception as e:
        logger.error(f"Test failed: {str(e)}")

    finally:
        driver.quit()
        logger.info("WebDriver session ended")

# Test Case 4: Empty Fields
def test_login_empty_fields():
    driver = setup_driver()
    logger.info("Test started: test_login_empty_fields")

    try:
        # Open the login page
        driver.get("https://app.vwo.com/#/login")
        logger.info("Navigated to the login page")

        # Leave fields empty and click the login button
        login_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.ID, "js-login-btn"))
        )
        login_button.click()
        logger.info("Clicked the Sign-In button without entering credentials")
        
        # Wait for the error message to appear
        error_message = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.ID, "js-notification-box-msg"))
        )
        error_text = error_message.text.strip()
        
        # Verify the error message text
        expected_error = "Your email, password, IP address or location did not match"
        if error_text == expected_error:
            logger.info(f"Test passed: Correct error message displayed - '{error_text}'")
        else:
            logger.error(f"Test failed: Unexpected error message - '{error_text}'")
    except Exception as e:
        logger.error(f"Test failed: {str(e)}")

    finally:
        driver.quit()
        logger.info("WebDriver session ended")

# Running all tests
if __name__ == "__main__":
    logger.info("Starting test execution...")
    test_login_valid_credentials()
    test_login_invalid_email()
    test_login_invalid_password()
    test_login_empty_fields()
    logger.info("Test execution completed.")
