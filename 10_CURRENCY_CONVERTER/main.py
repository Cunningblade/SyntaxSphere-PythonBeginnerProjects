print("Welcome to Indian Currency Converter")
value = int(input("Enter a Value : "))
print("The Converted Values are\n ")

russian = lambda val : val / 1.07
us = lambda val : val / 83.47
print(f"{value}₹ is {round(russian(value),2)}₽ (Russian Ruble)")
print('-'*100)
print(f"{value}₹ is {round(us(value),2)}$ (US DOllARS)")