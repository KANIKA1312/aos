import sys
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import datetime
import aos_locators as locators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import random

s = Service(executable_path='C:\Capstone Project\chromedriver.exe')
driver = webdriver.Chrome(service=s)


def setUp():
    print(f'This AOS Test Start at : {datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")}'
          f' on {datetime.datetime.today().strftime("%A")}')
    print('-----------------~~~~~~-------------------')
    driver.maximize_window()
    driver.implicitly_wait(30)
    driver.get(locators.web_url)
    assert driver.current_url == locators.web_url
    assert driver.title == locators.web_title
    print('Advantage Online Shopping Launched Successfully!!')
    print('')
    sleep(1)

def create_new_user():
    driver.find_element(By.ID, 'menuUser').click()
    sleep(3)
    driver.find_element(By.LINK_TEXT, 'CREATE NEW ACCOUNT').click()
    sleep(1)
    driver.find_element(By.NAME, 'usernameRegisterPage').send_keys(locators.username)
    sleep(0.25)
    driver.find_element(By.NAME, 'emailRegisterPage').send_keys(locators.email)
    sleep(0.25)
    driver.find_element(By.NAME, 'passwordRegisterPage').send_keys(locators.password)
    sleep(0.25)
    driver.find_element(By.NAME, 'confirm_passwordRegisterPage').send_keys(locators.password)
    sleep(0.25)
    driver.find_element(By.NAME, 'first_nameRegisterPage').send_keys(locators.first_name)
    sleep(0.25)
    driver.find_element(By.NAME, 'last_nameRegisterPage').send_keys(locators.last_name)
    sleep(0.25)
    driver.find_element(By.NAME, 'phone_numberRegisterPage').send_keys(locators.phone_number)
    sleep(0.25)
    Select(driver.find_element(By.NAME, 'countryListboxRegisterPage')).select_by_visible_text(locators.country)
    sleep(0.25)
    driver.find_element(By.NAME, 'cityRegisterPage').send_keys(locators.city)
    sleep(0.25)
    driver.find_element(By.NAME, 'addressRegisterPage').send_keys(locators.address)
    sleep(0.25)
    if locators.country == 'Canada':
        pr_list = ['BC', 'AB', 'SK', 'MB', 'ON', 'QC', 'NB', 'PB', 'NL', 'NS']
        for li in pr_list:
            rand_pr = random.choice(pr_list)
            driver.find_element(By.NAME, 'state_/_province_/_regionRegisterPage').send_keys(rand_pr)
            break
    sleep(0.25)
    if locators.country == 'United States':
        pr_list = ['AK', 'AL', 'AZ', 'AR', 'DC', 'DE', 'FL', 'ID', 'IL', 'IN']
        for li in pr_list:
            rand_pr = random.choice(pr_list)
            driver.find_element(By.NAME, 'state_/_province_/_regionRegisterPage').send_keys(rand_pr)
            break
    driver.find_element(By.NAME, 'postal_codeRegisterPage').send_keys(locators.postal_code)
    sleep(0.25)
    driver.find_element(By.NAME, 'i_agree').click()
    sleep(0.25)
    driver.find_element(By.ID, 'register_btnundefined').click()
    sleep(0.25)
    print(f'New account now exist for {locators.first_name} {locators.last_name}. '
          f'Username is {locators.username} & associated Email ID for account is {locators.email}')
    print('')
    logger('created')

def log_in(username,password):

    driver.find_element(By.ID, 'menuUser').click()
    sleep(2)
    driver.find_element(By.NAME, 'username').send_keys(username)
    sleep(0.25)
    driver.find_element(By.NAME, 'password').send_keys(password)
    sleep(0.25)
    driver.find_element(By.ID, 'sign_in_btnundefined').click()
    print(f'{locators.first_name} {locators.last_name}. Logged in '
          f'with username {locators.username} ')
    print('')

def log_out():
    assert driver.find_element(By.ID, 'menuUserLink').is_displayed()
    sleep(0.25)
    driver.find_element(By.ID, 'hrefUserIcon').click()
    sleep(0.25)
    driver.find_element(By.XPATH, '//*[@id="loginMiniTitle"]/label[contains(.,"Sign out")]').click()
    print('Logout Successful!!!')
    print('')
    sleep(0.25)

def tearDown():
    if driver is not None:
        print('-----------------~~~~~~-------------------')
        print(f'This AOS Test Complete at : {datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")}'
              f' on {datetime.datetime.today().strftime("%A")}')
        sleep(0.25)
        driver.close()
        driver.quit()

def logger(action):
    # create variable to store the file content
    old_instance = sys.stdout
    log_file = open('message.log', 'a')  # open log file and append a record
    sys.stdout = log_file
    print(f'{locators.email}\t'
          f'{locators.username}\t'
          f'{locators.password}\t'
          f'{locators.username}\t'
          f'{datetime.datetime.now()}\t'
          f'{action}')
    sys.stdout = old_instance
    log_file.close()

