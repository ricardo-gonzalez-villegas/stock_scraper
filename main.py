from stock_scraper import run_stock_scraper
from stock_parser import parse_lines
import os.path

file_exists = os.path.exists('stock_data.txt')

if file_exists:
    with open('stock_data.txt', "r") as f:
        lines = f.readlines()
        symbols, company_names = parse_lines(lines)
else:
    stock_data = run_stock_scraper()
    with open('stock_data.txt', 'w') as f:
        symbols = stock_data[0]
        company_names = stock_data[1]
        for i in range(len(symbols)):
            f.write(f"{symbols[i]}@{company_names[i]}\n")
