python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("transaction_data.csv")

print(data.info())

print(data.describe())

print(data.isnull().sum())

plt.figure(figsize=(10, 6))
sns.countplot(x='GRP', data=data, order=data['GRP'].value_counts().index)
plt.title('Most Purchased Product Categories')
plt.xlabel('Product Category')
plt.ylabel('Frequency')
plt.xticks(rotation=45)
plt.show()

plt.figure(figsize=(10, 6))
monthly_sales = data.groupby('MONTH')['VALUE'].sum()
monthly_sales.plot(kind='bar')
plt.title('Total Sales per Month')
plt.xlabel('Month')
plt.ylabel('Total Sales (Value)')
plt.xticks(rotation=0)
plt.show()
