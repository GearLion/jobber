# This is Jobber, the LinkedIn Application Bot
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from credentials import linkedin_password, linkedin_email

linkedin_with_requirements = "https://www.linkedin.com/jobs/search/?f_AL=true&f_E=2&f_I=4&f_WT=2&geoId=103644278"
chrome_driver_path = "C:/Users/LinguaManiac/Dropbox/Writings/Code/chromedriver.exe"
jobber = webdriver.Chrome(executable_path=chrome_driver_path)


def login():
    jobber.get(linkedin_with_requirements)
    login = jobber.find_element(By.CLASS_NAME, "nav__button-secondary")
    login.click()

    username = jobber.find_element(By.ID, "username")
    password = jobber.find_element(By.ID, "password")
    username.send_keys(linkedin_email)
    password.send_keys(linkedin_password)

    signin = jobber.find_element(By.CLASS_NAME, "login__form_action_container ")
    signin.click()


def find_job():
    job = jobber.find_element(By.CLASS_NAME, "job-card-container__metadata-wrapper")
    job.click()

    apply_button = False
    tries = 0
    while not apply_button:
        try:
            easy_apply = jobber.find_element(By.XPATH, "/html/body/div[6]/div[3]/div[3]/div[2]/div/section[2]/div/div/div[1]/div/div[1]/div/div[2]/div[3]/div/div/div/button/span")
        except NoSuchElementException:
            try:
                hide = jobber.find_element(By.XPATH, "/html/body/div[6]/div[3]/div[3]/div[2]/div/section[1]/div/div/ul/li[1]/div/div/div/div[3]/div/button")
            except NoSuchElementException:
                try:
                    hide = jobber.find_element(By.XPATH, "/html/body/div[5]/div[3]/div[3]/div[2]/div/section[1]/div/div/ul/li[1]/div/div/div/div[3]/div/button")
                except NoSuchElementException:
                    try:
                        hide = jobber.find_element(By.XPATH, "/html/body/div[6]/div[3]/div[3]/div[2]/div/section[1]/div/div/ul/li[1]/div/div/div[1]/div[3]/div/button")
                    except NoSuchElementException:
                        hide = jobber.find_element(By.XPATH, "/html/body/div[5]/div[3]/div[3]/div[2]/div/section[1]/div/div/ul/li[1]/div/div/div[1]/div[3]/div/button")
            hide.click()
            jobber.refresh()
        else:
            easy_apply.click()
            return True
        finally:
            tries += 1
            if tries > 10:
                return False


def check_questions(num):
    try:
        notification_button = jobber.find_element(By.XPATH, "/html/body/div[3]/div/div/div[2]/div/div[2]/footer/div[1]/label")
    except NoSuchElementException:
        try:
            next_button = jobber.find_element(By.XPATH,"/html/body/div[3]/div/div/div[2]/div/form/footer/div[2]/button[2]")
        except NoSuchElementException:
            next_button = jobber.find_element(By.XPATH, "/html/body/div[3]/div/div/div[2]/div/form/footer/div[2]/button")
        next_button.click()
        num += 1
        if num < 5:  # To make sure Selenium doesn't just keep hitting the next button when there's unanswered questions.
            check_questions(num)
        else:
            print("There's a question Jobber can't answer.")
    else:
        WebDriverWait(jobber, 10).until(expected_conditions.element_to_be_clickable(notification_button))
        notification_button.click()
        submit_application = jobber.find_element(By.XPATH, "/html/body/div[3]/div/div/div[2]/div/div[2]/footer/div[3]/button[2]")
        submit_application.click()


login()
for n in range(5):
    if find_job():
        check_questions(0)
    else:
        break
