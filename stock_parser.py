def parse_lines(lines: list) -> list[list, list]:
    symbols = list()
    company_names = list()
    for i, line in enumerate(lines):
        if i == 0:
            continue
        line = str(line).replace("\n", "")
        line = line.split('@')
        symbols.append(line[0])
        company_names.append(line[1])
    return [symbols, company_names]
