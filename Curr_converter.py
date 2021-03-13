from forex_python.converter import CurrencyRates
c = CurrencyRates()
from_currency = input("From Currency: ").upper()
to_currency = input("To Currency: ").upper()
amount = int(input("Enter the amount: "))
print(from_currency, " To ", to_currency, amount)
result = c.convert(from_currency, to_currency, amount)
print(result)
