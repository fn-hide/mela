from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException

from time import sleep

driver = webdriver.Chrome('chromedriver.exe')
driver.maximize_window()

visit_link = 'https://app.roboflow.com/huda-febrianto-nurrohman'
myuser = 'fn-hide'
mypass = '893Hudff12'
driver.get(visit_link)

driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div/div[1]/form/ul/li[2]/button').click()
driver.find_element_by_name('login').send_keys(myuser)
driver.find_element_by_name('password').send_keys(mypass)
driver.find_element_by_name('commit').click()

driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[2]/div/div[3]/a[2]/div[2]').click()

for span in driver.find_elements_by_xpath('(.//span)'):
    if span.text == 'Annotate':
        span.click()

for h3 in driver.find_elements_by_xpath('(.//h3)'):
    if h3.text == 'Job 6':
        h3.click()
        
driver.find_element_by_xpath('.//div[@class="image"]').click()

def take_action(element):
    while True:
        try:
            element.click()
            break
        except ElementClickInterceptedException:
            pass
    return 'Berhasil'

def take_danger(element):
    while True:
        try:
            element.click()
            break
        except NoSuchElementException:
            print('Danger!')
    return 'Berhasil'
    
for i in range(1000):
    take_danger(driver.find_element_by_id('dropdownMenuLink'))
    sleep(1)
    take_danger(driver.find_element_by_link_text('Remove from Project'))
    sleep(3)
    take_danger(driver.find_element_by_class_name('swal2-confirm'))
    sleep(3)
        
        


