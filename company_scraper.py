from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium import webdriver
import time

URL = "https://stockanalysis.com/list/biggest-companies/"

options = Options()
options.add_experimental_option("detach", True)
options.add_argument('--headless')

driver = webdriver.Chrome(options=options)
driver.get(URL)

total_page_count = int(driver.find_element(By.XPATH, "//nav/div/span").text.split(" ")[3])
page_count = 1


# rank - symbol - name
def scrape_data() -> None:
    # wait for page to load
    time.sleep(2)
    # scrapes stock symbols
    symbols = driver.find_elements(By.CLASS_NAME, "sym")
    for symbol in symbols:
        print(symbol.text)


# click through all pages and scape data
while True:
    # checks if on last page and scrapes data before exiting
    if page_count == total_page_count:
        scrape_data()
        break
    # scrapes page and increases page count
    try:
        scrape_data()
        driver.find_element(By.XPATH, "//span[contains(text(),'Next')]").click()
        page_count = page_count + 1
    # close pop up if it displays
    except:
        WebDriverWait(driver, 2).until(
            ec.presence_of_element_located((By.CSS_SELECTOR, "[aria-label='Close']")))
        driver.find_element(By.CSS_SELECTOR, "[aria-label='Close']").click()
