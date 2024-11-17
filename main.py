from selenium import webdriver
from time import sleep

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")

driver = webdriver.Chrome(options=chrome_options)
driver.get('https://it.bidoo.com/login_push.php')
wait_for_login = input("Once you are logged in press enter")
print("dess: "+driver.get_cookie('dess')["value"])
copy_and_close = input("Press a key to close the script")
