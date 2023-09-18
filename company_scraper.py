from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium import webdriver
import time
URL = "https://stockanalysis.com/list/biggest-companies/"
options = Options()
options.add_argument("--disable-popup-blocking")
options.add_experimental_option("detach", True)
# options.add_argument('--headless')
driver = webdriver.Chrome(options=options)
driver.get(URL)
pages = int(driver.find_element(By.XPATH, "//nav/div/span").text.split(" ")[3])

# click through all pages and scrape data
for i in range(pages):
    symbols = driver.find_elements(By.CLASS_NAME, "sym")
    for sym in symbols:
        print(sym.text)

    if i != pages:
        driver.find_element(By.XPATH, "//span[contains(text(),'Next')]").click()
        # driver.switch_to.alert.dismiss()
        time.sleep(1)

