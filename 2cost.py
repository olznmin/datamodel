import matplotlib.pyplot as plt

months = ['September', 'October', 'November', 'December', 'January', 'February']
advertising_costs = [1056000, 950400, 739200, 528000, 316800, 316800]
social_network_costs = [0, 105600, 316800, 528000, 739200, 739200]

plt.plot(months, advertising_costs, marker='o', label='Advertising Costs')
plt.plot(months, social_network_costs, marker='o', label='Social Network Costs')
plt.xlabel('Month')
plt.ylabel('Cost ($)')
plt.title('Advertising Costs and Social Network Costs from September to February')
plt.legend()
plt.grid(True)

plt.show()