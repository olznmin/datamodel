import matplotlib.pyplot as plt

months = ['September', 'October', 'November', 'December', 'January', 'February']
total_sales = [5280000, 5501000, 5469000, 5480000, 5533000, 5554000]
target_sales = [5280000, 5500000, 5729000, 5968000, 6217000, 6476000]

plt.plot(months, total_sales, marker='o', label='Total Sales')
plt.plot(months, target_sales, marker='o', label='Target Sales')
plt.xlabel('Month')
plt.ylabel('Sales ($)')
plt.title('Total Sales and Target Sales from September to February')
plt.legend()
plt.grid(True)

plt.show()