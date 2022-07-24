from ast import Bytes
import selenium
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import csv
from csv import reader

def Connecting_To_Browser(id_str, pass_str):
    if id_str != "" and pass_str != "":
        browser = webdriver.Chrome("chromedriver.exe")
        # browser = "chromedriver.exe"
        # brave_path = "C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--incognito")
        # browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        browser = webdriver.Chrome(chrome_options=chrome_options)
        try:
            browser.get('https://www.gmail.com/')

            # email_field = browser.find_element_by_id("identifierId")
            email_field = browser.find_element(By.ID,"identifierId")
            email_field.clear()


            time.sleep(1)

            email_field.send_keys(id_str)
            

            # email_next_button = browser.find_element_by_id("identifierNext")
            email_next_button = browser.find_element(By.ID,"identifierNext")
            email_next_button.click()
            

            time.sleep(2)
            
        

            # password_field = browser.find_element_by_name("password")
            password_field = browser.find_element(By.NAME,"password")


            password_field.clear()
            

            time.sleep(1)
            

            password_field.send_keys(pass_str)
            

            # password_next_button = browser.find_element_by_id("passwordNext")
            password_next_button = browser.find_element(By.ID,"passwordNext")
            password_next_button.click()

            

            time.sleep(2)

            browser.get('https://www.youtube.com/channel/UC2mphzwDhNQqwa02GxhPTXw/videos')

            
            # subscribe_next_button = browser.find_element_by_class_name("style-scope ytd-subscribe-button-renderer")
            subscribe_next_button = browser.find_element(By.CLASS_NAME,"style-scope ytd-subscribe-button-renderer")

            subscribe_next_button.click()

            time.sleep(1)

            notification_btn = browser.find_element(By.CLASS_NAME,"style-scope ytd-subscription-notification-toggle-button-renderer")
            notification_btn.click()

            time.sleep(1)

            all_noti_btn = browser.find_element(By.CLASS_NAME,"style-scope ytd-menu-service-item-renderer")
            all_noti_btn.click()

            time.sleep(3)
            browser.quit()
        except:
            print("not Success")
            browser.quit()
    else:
        print("Either ID or PASSWORD is null")

    


with open('idpass1.csv', 'r') as read_obj:
   
    # pass the file object to reader() to get the reader object
    csv_reader = reader(read_obj)

    # Pass reader object to list() to get a list of lists
    list_of_rows = list(csv_reader)
    

print("Total Ids and Passwords: ", len(list_of_rows))
total_Len = len(list_of_rows)

ids_pass_list = list_of_rows

for i in range(len(ids_pass_list)):
    id_str = ids_pass_list[i][0]
    id_pass = ids_pass_list[i][1]
    print(i)
    print("Login Id: ", id_str)
#     print("Login Password: ", id_pass)
    Connecting_To_Browser(id_str, id_pass)