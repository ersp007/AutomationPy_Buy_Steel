from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Specify the path to your ChromeDriver
chrome_driver_path = "C:\\Program Files\\WebDriver\\chromedriver.exe"

# Create a Service object
service = Service(chrome_driver_path)

# Set Chrome options (optional, but good to have for configuring behavior)
chrome_options = Options()
chrome_options.add_argument("--start-maximized")  # Example option to maximize the window

# Pass the Service and options object to the Chrome WebDriver
driver = webdriver.Chrome(service=service, options=chrome_options)

# Set an implicit wait time (e.g., 10 seconds)
driver.implicitly_wait(10)

# Navigate to the Tata Nexarc form
driver.get("https://www.tatanexarc.com/buy/inquiry-form/")

try:
    # Step 1: Enter mobile number
    mobile_input = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.ID, "userMobileNum"))
    )
    mobile_input.send_keys("9000000000")  # Enter your mobile number

    # Step 2: Trigger OTP
    otp_button = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@class='nexarc-primary-btn' and @type='button']"))
    )
    driver.execute_script("arguments[0].click();", otp_button)

    # Wait for manual OTP entry
    print("Please enter the OTP manually in the browser.")
    time.sleep(30)  # Adjust this time as needed for entering OTP

    # Step 3: Enter the pincode
    pincode_input = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.ID, "userPinCode"))
    )
    pincode_input.send_keys("751030")  # Enter pincode

    # Step 4: Click "Continue" button
    continue_button = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.ID, "continueBtn"))
    )
    continue_button.click()

    # Buffer time to wait for page transition or other events
    time.sleep(5)


    # Step 5: Handle the "Fill Form" toggle
    def select_toggle():
        fill_form_toggle = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.ID, "fill-form-toggle"))
        )
        driver.execute_script("arguments[0].checked = true;", fill_form_toggle)
        driver.execute_script("arguments[0].click();", fill_form_toggle)
        print("Fill a form toggle selected.")


    select_toggle()

    # Step 6: Select Product Grade
    product_grade_button = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH,
                                    "//div[@class='ms-parent single-select single-select-product-grade']//button[@class='ms-choice']"))
    )
    driver.execute_script("arguments[0].scrollIntoView(true);", product_grade_button)
    time.sleep(1)
    driver.execute_script("arguments[0].click();", product_grade_button)
    time.sleep(2)

    desired_option = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, "//span[text()='Angles IS 2062:2011 E250A']"))
    )
    desired_option.click()
    time.sleep(5)

    # Step 7: Select Dimension
    dimension_button = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//div[@class='ms-parent single-select single-select-product-dia']//button"))
    )
    driver.execute_script("arguments[0].scrollIntoView(true);", dimension_button)
    time.sleep(1)
    driver.execute_script("arguments[0].click();", dimension_button)
    time.sleep(2)

    desired_dimension = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, "//span[text()='ISA 100x100x10, Sec Wt- 14.9xOTHER']"))
    )
    desired_dimension.click()
    time.sleep(5)

    # Step 8: Scroll to and click the Brand dropdown button
    brand_button = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@class='ms-choice']/span[@class='placeholder']"))
    )

    driver.execute_script("arguments[0].scrollIntoView(true);", brand_button)
    time.sleep(1)  # Allow brief pause after scrolling

    driver.execute_script("arguments[0].click();", brand_button)
    time.sleep(2)  # Allow dropdown to open

    # Step 9: Select the "Select All" option in the brand dropdown
    select_all_checkbox = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, "//input[@data-name='selectAll']/parent::label"))
    )

    driver.execute_script("arguments[0].click();", select_all_checkbox)
    time.sleep(5)  # Wait to inspect results

    ### Step 10: Click outside the dropdown (clicking on the body to close dropdown)
    body_element = driver.find_element(By.TAG_NAME, "body")
    driver.execute_script("arguments[0].click();", body_element)
    time.sleep(2)

    ### Step 11: Enter quantity in the quantity field
    quantity_input = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.ID, "quantity-mt-input"))
    )
    driver.execute_script("arguments[0].click();", quantity_input)  # Click on the quantity input
    time.sleep(1)  # Allow brief pause

    quantity_input.send_keys("1000")  # Enter random quantity value
    time.sleep(2)

    ### Step 12: Click outside the quantity field
    driver.execute_script("arguments[0].click();", body_element)
    time.sleep(2)

    ### Step 13: Click the "Add Product" CTA button
    add_product_button = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.ID, "daCustomerAddInquiry"))
    )
    driver.execute_script("arguments[0].click();", add_product_button)
    time.sleep(5)  # Wait to inspect results

    ### Step 14: Enter Business Name
    business_name_input = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.ID, "businessName"))
    )
    business_name_input.send_keys("Testing")  # Enter business name
    time.sleep(2)

    ### Step 15: Enter Email Address
    email_input = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.ID, "emailId"))
    )
    email_input.send_keys("test@nexrac.in")  # Enter email address
    time.sleep(2)

    ### Step 16: Enter Comment in Comment Field
    comment_field = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.ID, "textarea"))
    )
    comment_field.send_keys("Testing, Ignore")  # Add comment
    time.sleep(2)

    ### Step 17: Click outside the comment field
    driver.execute_script("arguments[0].click();", body_element)
    time.sleep(2)

    ### Step 18: Click the "Submit" button
    submit_button = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//button[@class='nexarc-primary-btn mp-activity-modal-link' and @type='button']"))
    )
    driver.execute_script("arguments[0].click();", submit_button)

    # Allow 40 seconds buffer after clicking "Submit"
    time.sleep(40)

finally:
    # Quit the driver after use
    driver.quit()
