from selenium import webdriver
import time

chrome_browser=webdriver.Chrome(executable_path='E:\chromedriver')
chrome_browser.get('https://web.whatsapp.com/')

time.sleep(15)

user_name = 'Mesajı iletmek istediğiniz kişinin whatsapptaki adı'

user = chrome_browser.find_element_by_xpath('//span[@title="{}"]'.format(user_name))
user.click()

message_box = chrome_browser.find_element_by_xpath('//div[@class="DuUXI"]')
message_box.send_keys('Mesajınız')

message_box=chrome_browser.find_element_by_xpath('//button[@class="_2Ujuu"]')
message_box.click()