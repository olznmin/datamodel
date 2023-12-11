import matplotlib.pyplot as plt

months = ['September', 'October', 'November', 'December', 'January', 'February']
sales = [5280000, 5501000, 5469000, 5480000, 5533000, 5554000]

plt.plot(months, sales, marker='o')
plt.xlabel('Month')
plt.ylabel('Total Sales')
plt.title('Monthly Total Sales')
plt.grid(True)

plt.show()