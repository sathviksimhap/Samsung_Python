import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv(r"C:\Users\SIC\Desktop\retail_store_inventory.csv")

print(df.columns)

product_name =[
    "Gulab Jamun",
    "Jalebi",
    "Ladoo",
    "Barfi",
    "Rasgulla",
    "Kheer",
    "Halwa",
    "Peda",
    "Mysore Pak",
    "Sandesh"
]
units_sold = df.iloc[:10, 7]
units_ordered = df.iloc[:10, 8]

bar_width = 0.35

# Create an index for each product
index = range(len(product_name))

# Shift the positions for the second set of bars
plt.figure(figsize=(10, 6))

# Plot the bars, adjusting the positions to show them next to each other
plt.bar(index, units_sold, width=bar_width, label='Units Sold', color='b', align='center')
plt.bar([i + bar_width for i in index], units_ordered, width=bar_width, label='Units Ordered', color='y', align='center')


plt.xlabel('Number of items sold in a day')
plt.ylabel('Number of items ordered in a day')
plt.title('Units Sold vs Units Ordered')

plt.xticks([i + bar_width / 2 for i in index], product_name, rotation=90)

plt.show()