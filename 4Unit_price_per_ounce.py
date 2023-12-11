import matplotlib.pyplot as plt

months = ['September', 'October', 'November', 'December', 'January', 'February']
unit_prices = [2.0, 2.0, 2.0, 1.9, 1.9, 1.9]

plt.plot(months, unit_prices, marker='o')
plt.xlabel('Month')
plt.ylabel('Unit Price ($)')
plt.title('Unit Price per Ounce from September to February')
plt.grid(True)

plt.show()