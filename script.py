import pandas as pd
# Reading files into pandas dataframe
user_visits = pd.read_csv('page_visits.csv')

#Inspecting first few rows of data
print(user_visits.head())

# visits to shoe_fly from different sources
click_source = user_visits.groupby("utm_source").id.count().reset_index()
print(click_source)

# Visits to shoe_fly from different sources by every month
click_source_by_month = user_visits.groupby(["utm_source","month"]).id.count().reset_index()
print(click_source_by_month)

# Using pivot to display in readible tabular data
click_source_by_month_pivot = click_source_by_month.pivot(columns="month", index="utm_source", values="id").reset_index()
print(click_source_by_month_pivot)
