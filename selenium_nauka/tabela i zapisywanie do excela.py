import time
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import pandas as pd

# main_page = 'https://bulbapedia.bulbagarden.net/wiki/Bulbasaur_(Pokémon)'

# DRIVER_PATH = r'C:\Users\mkglo\Desktop\chromedriver.exe'
# driver = webdriver.Chrome(executable_path=DRIVER_PATH)
# driver.get(main_page)



# driver.quit()


a = ['a', 'b', 'c']
b = [1, 2, 3]
c = ['raz', 'dwa', 'trzy']
d = []

i = 0

while i<3:
    d.append([a[i], b[i], c[i]])
    i+=1

print(d)
df = pd.DataFrame(d, index=['litery', 'liczby', 'liczby ale słownie']).T
df.to_excel(r"C:\Users\MGlowacki\Desktop\raportwynik\raport.xlsx")

