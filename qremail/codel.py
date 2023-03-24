import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_excel('C:\Users\Laptop\Downloads\Team CODE Minutes and Actions 2023.xlsx')

plt.plot(data['x'], data['y'])
plt.xlabel('X Values')
plt.ylabel('Y Values')
plt.title('My Plot')
plt.grid(True)
plt.show()


