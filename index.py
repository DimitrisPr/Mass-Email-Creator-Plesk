import string
import time
import random
from selenium import webdriver
driver = webdriver.Chrome('./chromedriver')  # Optional argument, if not specified will search path.

plesk_username = 'your_plesk_username' #Delete this immediately after using the script
plesk_password = 'your_plesk_password' #Delete this immediately after using the script
domain = 'your_domain' # example.com
plesk_port = '8443' #default plesk port, dont change this
plesk_login_url = domain + ":" + plesk_port
num_of_emails_to_create = 10 #num of emails to create on the session


def main():
    driver.get(plesk_login_url)
    login_to_plesk()
    
    #async calls or threading would be the optimal solutions for production apps. Use this at home, for fun, only.
    for x in range(1, num_of_emails_to_create): 
        credentials = create_email()
        save_credentials(credentials)

def login_to_plesk():
    login_form = driver.find_element_by_name('login_name')
    login_form.send_keys(plesk_username)
    login_form = driver.find_element_by_name('passwd')
    login_form.send_keys(plesk_password)
    login_form.submit()
    driver.get(plesk_login_url+"/smb/email-address/create")

def random_string_generator(type):

    chars = string.ascii_uppercase + string.digits + string.ascii_lowercase
    
    if type == "password":
        rand_string = ''.join(random.choice(chars) for _ in range(20)) + "@#"
    else:
        rand_string = ''.join(random.choice(chars) for _ in range(7)) 

    return rand_string

def save_credentials(credentials):
    with open("credentials.txt", "a") as c:
        c.write(credentials + "\n")

def create_email():

    #email field
    email_name = random_string_generator("name")
    email_field = driver.find_element_by_id('general-generalSection-name')
    email_field.send_keys(email_name)

    #password field
    email_password = random_string_generator("password")

    password_field = driver.find_element_by_id('general-generalSection-password')
    password_field.send_keys(email_password)

    password_confirmation_field = driver.find_element_by_id('general-generalSection-passwordConfirmation')
    password_confirmation_field.send_keys(email_password)

    password_confirmation_field.submit()
    
    time.sleep(2) #make sure submission was made

    driver.get(plesk_login_url+"/smb/email-address/create") #redirect to email creation panel
    
    return email_name + "@" + domain + ":" + email_password
    
main()
driver.quit()






