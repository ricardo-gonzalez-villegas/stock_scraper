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


def scrape_data(symbols: list, company_names: list) -> None:
    # wait for page to load
    time.sleep(2)
    # scrapes symbols & company names
    symbol_elements = driver.find_elements(By.CLASS_NAME, "sym")
    company_name_elements = driver.find_elements(By.CLASS_NAME, "slw")
    # adds scraped data to lists
    for symbol in symbol_elements:
        symbols.append(symbol.text)
    for company_name in company_name_elements:
        company_names.append(company_name.text)


def run_stock_scraper() -> list[list, list]:
    symbols, company_names = list(), list()

    # scrapes page and increases page count
    try:
        scrape_data(symbols=symbols, company_names=company_names)
    # close pop up if it displays
    except Exception as e:
        WebDriverWait(driver, 2).until(
            ec.presence_of_element_located((By.CSS_SELECTOR, "[aria-label='Close']")))
        driver.find_element(By.CSS_SELECTOR, "[aria-label='Close']").click()

    print("Completed scraping stocks")
    return [symbols, company_names]
