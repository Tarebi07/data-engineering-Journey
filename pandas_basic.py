import pandas as pd
data = {
    "name": ["Larry", "Amaka", "Emeka","Fatima"],
    "city":["Lagos","Abuja","Kano","Port Harcourt"],
    "skill":["SQL","Python","Excel","Power BI"],
    "age":[20,25,30,28]
}

df =pd.DataFrame(data)

print(df[df["city"]=="Lagos"])

print(df[df["skill"]=="SQL"])

def explore_df(df):
    print(df.head())
    print(df.shape)
    print(df.columns)
    print(df.dtypes)
    
explore_df(df)    


import pandas as pd

# Load dataset
df_cars = pd.read_csv("car_prices.csv")

# Explore the dataset
def explore_df(df):
    print(df.head())
    print(df.shape)
    print(df.columns)
    print(df.dtypes)

explore_df(df_cars)

# Key insights
print(df_cars["price"].describe())
print(df_cars["Make"].value_counts().head(10))
print(df_cars["Condition"].unique())

# Filters
print(df_cars[df_cars["price"] > 10000000])
print(df_cars[df_cars["Condition"] == "Foreign Used"])




