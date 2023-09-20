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


# scrape table rows
def scrape_data(table_rows: list) -> None:
    # wait for page to load
    time.sleep(2)
    # scrapes table row elements in table
    table_row_elements = driver.find_elements(By.TAG_NAME, "tr")
    # adds scraped data to list
    for table_row in table_row_elements:
        table_rows.append(table_row.text)


# click through all pages and scrape data
def run_stock_scraper() -> list:
    table_rows = list()
    page_count = 0

    while page_count != total_page_count:
        # scrapes page and increases page count
        try:
            scrape_data(table_rows)
            driver.find_element(By.XPATH, "//span[contains(text(),'Next')]").click()
            page_count = page_count + 1
        # close pop up if it displays
        except Exception as e:
            WebDriverWait(driver, 2).until(
                ec.presence_of_element_located((By.CSS_SELECTOR, "[aria-label='Close']")))
            driver.find_element(By.CSS_SELECTOR, "[aria-label='Close']").click()

    return table_rows
