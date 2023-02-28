import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver= webdriver.Chrome()
driver.maximize_window() # For maximizing window
driver.implicitly_wait(20)
driver.get("https://www.automationworld.com/")
driver.implicitly_wait(5)
driver.find_element(By.XPATH,"//div[contains(@class,'close')]").click()
driver.find_element(By.LINK_TEXT,"Subscribe").click()
#driver.implicitly_wait(10)
driver.switch_to.window(driver.window_handles[1])
print(driver.title)
time.sleep(20)
#driver.find_element(By.XPATH,"//input[@name='demo59701']]").click()
driver.find_element(By.XPATH,"//input[@name='demo59703']").send_keys('John')
driver.find_element(By.NAME,'demo59704').send_keys('wign')
driver.find_element(By.NAME,'demo59705').send_keys('QA')
driver.find_element(By.NAME,'demo59707').send_keys('www.Arrow.com')
driver.find_element(By.NAME,'demo59708').send_keys('eInfochips')
driver.find_element(By.XPATH,"//option[text()='INDIA']").click()
#driver.find_element(By.NAME,'demo59713').send_keys('Chennai')

#Javascript
driver.execute_script("document.querySelector('input[name=\"demo59713\"]').value='Chennai'") # before the double quotes we need to add slash

driver.find_element(By.NAME,'demo59693').click()
driver.find_element(By.XPATH,"//input[@type='submit']").click()

driver.implicitly_wait(5)
actual_error=driver.find_element(By.XPATH,"//li[contains(text(),'Email Address is required.')]").text
print(actual_error)

time.sleep(20)
driver.quit()
