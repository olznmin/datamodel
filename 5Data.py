import matplotlib.pyplot as plt


months = ['September', 'October', 'November', 'December', 'January', 'February']
total_sales = [5280000, 5501000, 5469000, 5480000, 5533000, 5554000]
target_sales = [5280000, 5500000, 5729000, 5968000, 6217000, 6476000]
advertising_costs = [1056000, 950400, 739200, 528000, 316800, 316800]
social_network_costs = [0, 105600, 316800, 528000, 739200, 739200]
unit_prices = [2.0, 2.0, 2.0, 1.9, 1.9, 1.9]


plt.plot(months, total_sales, marker='o', label='Total Sales')
plt.plot(months, target_sales, marker='o', label='Target Sales')
plt.plot(months, advertising_costs, marker='o', label='Advertising Costs')
plt.plot(months, social_network_costs, marker='o', label='Social Network Costs')
plt.plot(months, unit_prices, marker='o', label='Unit Price per Ounce')
plt.xlabel('Month')
plt.ylabel('Amount ($)')
plt.title('Data from September to February')
plt.legend()
plt.grid(True)


plt.show()