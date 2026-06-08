import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df_cars = pd.read_csv("C:/Users/Chief Larry Samuel/Desktop/DATA E JOURNEY/car_prices.csv")
print(df_cars.head())

# Histogram


# plt.figure(figsize=(10,6))
# df_cars["Make"].value_counts().head(10).plot(kind="bar")
# plt.title("Top 10 Cars Brands in Nigeria")
# plt.xlabel("Brand")
# plt.ylabel("Number of cars")
# plt.tight_layout()
# plt.show()

# plt.figure(figsize=(10,6))
# plt.hist(df_cars["price"], bins = 10, color="blue", edgecolor="black")
# plt.title("Distribution of cars Prices in Nigeria")
# plt.xlabel("Price(naira)")
# plt.ylabel("Number of cars")
# plt.tight_layout()
# plt.show()


# Scatter Plot

# plt.figure(figsize=(10,6))
# plt.scatter(df_cars["Mileage"], df_cars["price"], alpha=0.5)
# plt.title("Car Price vs Mileage in Nigeria")
# plt.xlabel("Mileage")
# plt.ylabel("Price (Naira)")
# plt.tight_layout()
# plt.show()


# Line chart

df_cars.groupby("Year of manufacture")["price"].mean().plot(kind="line")
plt.title("Average Car Price by Year of Manuafacture")
plt.xlabel("Year")
plt.ylabel("Avearge Price (Naira)")
plt.tight_layout()
plt.show()
