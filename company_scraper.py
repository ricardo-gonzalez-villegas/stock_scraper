from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium import webdriver
import time

# companies are sorted by market cap
URL = "https://stockanalysis.com/list/biggest-companies/"

options = Options()
options.add_experimental_option("detach", True)
options.add_argument('--headless')

driver = webdriver.Chrome(options=options)
driver.get(URL)

total_page_count = int(driver.find_element(By.XPATH, "//nav/div/span").text.split(" ")[3])
page_count = 1

data_cells = list()


def scrape_data() -> None:
    # wait for page to load
    time.sleep(2)
    # scrapes data cell elements in table
    data_cell_elements = driver.find_elements(By.TAG_NAME, "td")
    # adds scraped data to list
    for data_element in data_cell_elements:
        data_cells.append(data_element.text)


# click through all pages and scrape data
while True:
    # checks if on last page and scrapes data before exiting
    if page_count == total_page_count:
        scrape_data()
        break
    # scrapes page and increases page count
    try:
        scrape_data()
        page_count = page_count + 1
        driver.find_element(By.XPATH, "//span[contains(text(),'Next')]").click()
    # close pop up if it displays
    except Exception as e:
        print("pop up")
        WebDriverWait(driver, 2).until(
            ec.presence_of_element_located((By.CSS_SELECTOR, "[aria-label='Close']")))
        driver.find_element(By.CSS_SELECTOR, "[aria-label='Close']").click()
