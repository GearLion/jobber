# This is Jobber, the LinkedIn Application Bot
from selenium import webdriver
from selenium.webdriver.common.by import By
from credentials import linkedin_password, linkedin_email
from time import sleep # For testing, so I can space out and see what the comp is doing.

linkedin_with_requirements = "https://www.linkedin.com/jobs/search/?f_AL=true&f_E=2&f_I=4&f_WT=2&geoId=103644278"
chrome_driver_path = "C:/Users/LinguaManiac/Dropbox/Writings/Code/chromedriver.exe"
jobber = webdriver.Chrome(executable_path=chrome_driver_path)


jobber.get(linkedin_with_requirements)
login = jobber.find_element(By.CLASS_NAME, "nav__button-secondary")
login.click()

username = jobber.find_element(By.ID, "username")
password = jobber.find_element(By.ID, "password")
username.send_keys(linkedin_email)
password.send_keys(linkedin_password)

signin = jobber.find_element(By.CLASS_NAME, "login__form_action_container ")
signin.click()

job = jobber.find_element(By.CLASS_NAME, "job-card-container__metadata-wrapper")
job.click()

sleep(3)  # To allow the easy-apply button to load.
easy_apply = job.find_element(By.XPATH, "/html/body/div[6]/div[3]/div[3]/div[2]/div/section[2]/div/div/div[1]/div/div[1]/div/div[2]/div[3]/div/div/div/button/span")
easy_apply.click()

next_button = jobber.find_element(By.XPATH, "/html/body/div[3]/div/div/div[2]/div/form/footer/div[2]/button/span")
next_button.click()

next_button = jobber.find_element(By.XPATH, "/html/body/div[3]/div/div/div[2]/div/form/footer/div[2]/button[2]/span")
next_button.click()

