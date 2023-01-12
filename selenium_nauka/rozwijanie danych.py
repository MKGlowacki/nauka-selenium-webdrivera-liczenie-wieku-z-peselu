import time
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

main_page = 'https://www.gov.pl/web/gov/uslugi-dla-obywatela'

DRIVER_PATH = r'C:\Users\mkglo\Desktop\chromedriver.exe'
driver = webdriver.Chrome(executable_path=DRIVER_PATH)
driver.get(main_page)


WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'dokumenty-i-dane-osobowe')))   

driver.find_element(By.ID,'dokumenty-i-dane-osobowe').click()
WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH,'//*[@id="body"]/main/section/section/div/ul/li[1]/div/div[1]/div[1]/a')))
print(driver.find_element(By.XPATH, '//*[@id="body"]/main/section/section/div/ul/li[1]/div/div[1]/div[1]/a').text)



driver.quit()