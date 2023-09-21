from stock_scraper import run_stock_scraper
import os.path

file_exists = os.path.exists('stock_data.txt')

if file_exists:
    with open('stock_data.txt', "r") as f:
        print(f.read())
else:
    table_rows = run_stock_scraper()
    with open('stock_data.txt', 'w') as f:
        for table_row in table_rows:
            f.write(f"{table_row}")
