def decode_month(month):
    month_dict = {
        'JAN': 1, 'FEB': 2, 'MAR': 3, 'APR': 4, 'MAY': 5, 'JUN': 6,
        'JUL': 7, 'AUG': 8, 'SEP': 9, 'OCT': 10, 'NOV': 11, 'DEC': 12
    }
    
    return month_dict.get(month.upper(), 1)

def parse_date(date_str):
    parts = date_str.split("-")
    
    if len(parts) != 3:
        raise ValueError("Invalid date format")
    
    day = int(parts[0])
    month = decode_month(parts[1])
    
    year = int(parts[2])
    if year >= 0 and year <= 49:
        year += 2000
    else:
        year += 1900
    
    return (day, month, year)

test = parse_date('12-APR-90')
print(test) 
