import time
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

main_page = 'https://github.com/MKGlowacki'

DRIVER_PATH = r'C:\Users\mkglo\Desktop\chromedriver.exe'
driver = webdriver.Chrome(executable_path=DRIVER_PATH)
driver.get(main_page)

def sub_page(x):
    return '//*[@id="user-profile-frame"]/div/div[1]/div/ol/li['+ str(x) +r']/div/div/div/a/span'

def project_programming_language(x):
    return '//*[@id="user-profile-frame"]/div/div[1]/div/ol/li['+ str(x) +r']/div/div/p[2]/span/span[2]'

title_XPath = '//*[@id="repo-content-pjax-container"]/h1'
issues_page_id = 'issues-tab'
footer_XPath = '/html/body/div[1]/footer/div[1]/div/div/span'
# go_back_XPath = '//*[@id="repository-container-header"]/div[1]/div/div/span[1]/a'
i = 1
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, sub_page(i))))


# print(driver.find_element(By.XPATH ,project_programming_language(i)).text)



while i<=5:

    pLanguage = driver.find_element(By.XPATH ,project_programming_language(i)).text

    #przechodzenie na strone
    driver.find_element(By.XPATH, sub_page(i)).click()
    p = driver.current_window_handle
    chwd = driver.window_handles
    
    for w in chwd:
        if w != p:
            driver.switch_to.window(w)
            
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, issues_page_id)))
    # print("Child window title: " + driver.title)

    if pLanguage == "Java":
        print (driver.find_element(By.XPATH, title_XPath).text)
    elif pLanguage == "Python":
        driver.find_element(By.ID, issues_page_id).click()
        p = driver.current_window_handle
        chwd = driver.window_handles
    
        for w in chwd:
            if w != p:
                driver.switch_to.window(w)

        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="repo-content-turbo-frame"]/div/div[1]/div[2]/details/summary')))
        print (driver.find_element(By.XPATH, footer_XPath).text)
  
        driver.back()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, issues_page_id)))   
    else:
        print('cos') 
    

    driver.back()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, sub_page(i))))
    #powrot

    i+=1

driver.quit()


# //*[@id="user-profile-frame"]/div/div[1]/div/ol/li[1]/div/div/div/a/span
# //*[@id="user-profile-frame"]/div/div[1]/div/ol/li[2]/div/div/div/a/span