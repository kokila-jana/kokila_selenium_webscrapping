from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
import csv

# -------------------------------
# Browser Setup
# -------------------------------
# options = Options()
# options.add_argument("--start-maximized")

driver = webdriver.Chrome()

# -------------------------------
# Step 1: Open Naukri Website
# -------------------------------
driver.get("https://www.naukri.com")
time.sleep(3)

# -------------------------------
# Step 2: Click Login Button
# -------------------------------
driver.find_element(By.ID, "login_Layer").click()
time.sleep(3)

# -------------------------------
# Step 3: Enter Email
# -------------------------------
driver.find_element(
    By.XPATH,
    "//input[@placeholder='Enter your active Email ID / Username']"
).send_keys("kokilagur2016@gmail.com")

# -------------------------------
# Step 4: Enter Password
# -------------------------------
driver.find_element(
    By.XPATH,
    "//input[@type='password']"
).send_keys("Kokila@100599")

# -------------------------------
# Step 5: Click Login
# -------------------------------
driver.find_element(
    By.XPATH,
    "//button[text()='Login']"
).click()

time.sleep(6)   # wait for login success

# -------------------------------
# Step 6: Search Job
# -------------------------------
search_box = driver.find_element(By.CLASS_NAME, "suggestor-input")
search_box.send_keys("Python Developer")
search_box.send_keys(Keys.RETURN)

time.sleep(5)

# -------------------------------
# Step 7: Scrape Job Details
# -------------------------------
job_titles = driver.find_elements(By.CLASS_NAME, "title")
companies = driver.find_elements(By.CLASS_NAME, "comp-name")
locations = driver.find_elements(By.CLASS_NAME, "locWdth")

# -------------------------------
# Step 8: Save Data to CSV
# -------------------------------
with open("naukri_jobs.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Job Title", "Company", "Location"])

    for i in range(len(job_titles)):
        title = job_titles[i].text
        company = companies[i].text if i < len(companies) else ""
        location = locations[i].text if i < len(locations) else ""

        writer.writerow([title, company, location])

print("✅ Data saved to naukri_jobs.csv")

# -------------------------------
# Step 9: Close Browser
# -------------------------------
driver.quit()
