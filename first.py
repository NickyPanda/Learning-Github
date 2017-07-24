stocks = {
    'GOOG':434,
    'APPL':325,
    'ABC':54,
    'AMZN':623,
}

print(min(zip(stocks.values(), stocks.keys())))
print(sorted(zip(stocks.values(), stocks.keys())))
print(min(zip(stocks.keys(), stocks.values())))
print(sorted(zip(stocks.keys(), stocks.values())))