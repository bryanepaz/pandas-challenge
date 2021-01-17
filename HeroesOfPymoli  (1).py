#!/usr/bin/env python
# coding: utf-8

# ### Note
# * Instructions have been included for each segment. You do not have to follow them exactly, but they are included to help you think through the steps.

# In[56]:


import pandas as pd
import numpy as np


file_to_load = "Resources/purchase_data.csv"


purchase_data = pd.read_csv(file_to_load)
purchase_data_df = pd.DataFrame(purchase_data)
purchase_data_df.head()


# ## Player Count

# * Display the total number of players
# 

# In[32]:


total_players = purchase_data_df["SN"].count()
total_players


# ## Purchasing Analysis (Total)

# * Run basic calculations to obtain number of unique items, average price, etc.
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display the summary data frame
# 

# In[33]:


unique_items = len(purchase_data_df["Item ID"].unique())
unique_items

total_purchases = purchase_data_df["Purchase ID"].count()
total_purchases

total_revenue = purchase_data_df["Price"].sum()
total_revenue

average_price1 = purchase_data_df["Price"].mean()
average_price1

average_price2 = total_revenue/total_purchases
average_price2


purchase_analysis_df = pd.DataFrame([{"Number of Unique Items": unique_items, "Average Price": average_price1,
                                      "Number of Purchases": total_purchases, "Total Revenue": total_revenue}])
purchase_analysis_df["Average Price"] = purchase_analysis_df["Average Price"].map("${:,.2f}".format)
purchase_analysis_df["Total Revenue"] = purchase_analysis_df["Total Revenue"].map("${:,.2f}".format)
purchase_analysis_df

org_purchase_analysis_df = purchase_analysis_df[["Number of Unique Items","Average Price","Number of Purchases", "Total Revenue" ]]
org_purchase_analysis_df



# ## Gender Demographics

# * Percentage and Count of Male Players
# 
# 
# * Percentage and Count of Female Players
# 
# 
# * Percentage and Count of Other / Non-Disclosed
# 
# 
# 

# In[34]:


gender_demo_df = pd.DataFrame(purchase_data_df["Gender"].value_counts())
gender_demo_df

percentage_of_players = (purchase_data_df["Gender"].value_counts()/total_players)*100
percentage_of_players


gender_demo_df["Percentage of Players"] = percentage_of_players
gender_demo_df["Percentage of Players"] = gender_demo_df["Percentage of Players"].map("{:,.2f}%".format)
gender_demo_df

 
org_gender_demo_df = gender_demo_df[["Percentage of Players", "Gender"]]
org_gender_demo_df


fin_gender_demo_df = org_gender_demo_df.rename(columns={"Gender":"Total Count"})
fin_gender_demo_df


# 
# ## Purchasing Analysis (Gender)

# * Run basic calculations to obtain purchase count, avg. purchase price, avg. purchase total per person etc. by gender
# 
# 
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display the summary data frame

# In[55]:




gender_grouped_purchased_data_df = purchase_data_df.groupby(["Gender"])

gender_grouped_purchased_data_df["Purchase ID"].count().head(10)

total_purchase_value = gender_grouped_purchased_data_df["Price"].sum()
total_purchase_value.head()
dlr_total_purchase_value = total_purchase_value.map("${:,.2f}".format)
dlr_total_purchase_value.head()

avg_purchase_price = gender_grouped_purchased_data_df["Price"].mean()
avg_purchase_price.head()
dlr_avg_purchase_price = avg_purchase_price.map("${:,.2f}".format)
dlr_avg_purchase_price.head()

normalized_totals = total_purchase_value/gender_grouped_purchased_data_df["Purchase ID"].count()
dlr_normalized_totals = normalized_totals.map("${:,.2f}".format)
dlr_normalized_totals.head()

org_gender_purchased_data_df = pd.DataFrame(gender_grouped_purchased_data_df["Purchase ID"].count())
org_gender_purchased_data_df["Average Purchase Price"] = dlr_avg_purchase_price  
org_gender_purchased_data_df["Total Purchase Value"] = dlr_total_purchase_value 
org_gender_purchased_data_df["Normalized Totals"] = dlr_normalized_totals 
org_gender_purchased_data_df

summary_gender_purchased_data_df = org_gender_purchased_data_df.rename(columns={"Purchase ID":"Purchase Count"})
summary_gender_purchased_data_df


# ## Age Demographics

# * Establish bins for ages
# 
# 
# * Categorize the existing players using the age bins. Hint: use pd.cut()
# 
# 
# * Calculate the numbers and percentages by age group
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: round the percentage column to two decimal points
# 
# 
# * Display Age Demographics Table
# 

# In[58]:



age_bins = [0, 9.90, 14.90, 19.90, 24.90, 29.90, 34.90, 39.90, 99999]
group_names = ["<10", "10-14", "15-19", "20-24", "25-29", "30-34", "35-39", "40+"]

grp_by_age_purchase_data_df = purchase_data_df
grp_by_age_purchase_data_df["Age Summary"] = pd.cut(grp_by_age_purchase_data_df["Age"], age_bins, labels=group_names)
grp_by_age_purchase_data_df

grp_by_age_purchase_data_df = grp_by_age_purchase_data_df.groupby("Age Summary")
grp_by_age_purchase_data_df.count()
summary_by_age_df = pd.DataFrame(grp_by_age_purchase_data_df.count())
summary_by_age_df 

summary_by_age_df["Purchase ID"] = (summary_by_age_df["Purchase ID"]/total_players)*100
summary_by_age_df 

summary_by_age_df["Purchase ID"] = summary_by_age_df["Purchase ID"].map("{:,.2f}%".format)
summary_by_age_df
org_summary_by_age_df = summary_by_age_df[["Purchase ID","SN"]]
org_summary_by_age_df

fin_grp_by_age_summary_df = org_summary_by_age_df.rename(columns={"Purchase ID":"Percentage of Players", "SN":"Total Count"})
fin_grp_by_age_summary_df



# ## Purchasing Analysis (Age)

# * Bin the purchase_data data frame by age
# 
# 
# * Run basic calculations to obtain purchase count, avg. purchase price, avg. purchase total per person etc. in the table below
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display the summary data frame

# In[59]:


analysis_by_age_df = pd.DataFrame(grp_by_age_purchase_data_df["Purchase ID"].count())
analysis_by_age_df
total_purchase_value_age = grp_by_age_purchase_data_df["Price"].sum()
total_purchase_value_age
dlr_total_purchase_value_age = total_purchase_value_age.map("${:,.2f}".format)
dlr_total_purchase_value_age

avg_purchase_price_age = grp_by_age_purchase_data_df["Price"].mean()
avg_purchase_price_age
dlr_avg_purchase_price_age = avg_purchase_price_age.map("${:,.2f}".format)
dlr_avg_purchase_price_age


normalized_totals_age = total_purchase_value_age/grp_by_age_purchase_data_df["Purchase ID"].count()
dlr_normalized_totals_age = normalized_totals_age.map("${:,.2f}".format)
dlr_normalized_totals_age

analysis_by_age_df["Average Purchase Price"] = dlr_avg_purchase_price_age  
analysis_by_age_df["Total Purchase Value"] = dlr_total_purchase_value_age 
analysis_by_age_df["Normalized Totals"] = dlr_normalized_totals_age 
analysis_by_age_df
data_df = org_gender_purchased_data_df.rename(columns={"Purchase ID":"Purchase Count"})
summary_age_purchased_data_df = analysis_by_age_df.rename(columns={"Purchase ID":"Purchase Count"})
summary_age_purchased_data_df


# ## Top Spenders

# * Run basic calculations to obtain the results in the table below
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Sort the total purchase value column in descending order
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display a preview of the summary data frame
# 
# 

# In[60]:


orig_purchase_data_df = pd.DataFrame(purchase_data)
orig_purchase_data_df.head()

grp_SN_top_spendor_df = orig_purchase_data_df.groupby("SN")
grp_SN_top_spendor_df.count()

analysis_by_SPENDOR_df = pd.DataFrame(grp_SN_top_spendor_df["Purchase ID"].count())
analysis_by_SPENDOR_df

total_purchase_value_SN = grp_SN_top_spendor_df["Price"].sum()
total_purchase_value_SN

avg_purchase_price_SN = grp_SN_top_spendor_df["Price"].mean()
avg_purchase_price_SN
dlr_avg_purchase_price_SN = avg_purchase_price_SN.map("${:,.2f}".format)
dlr_avg_purchase_price_SN
analysis_by_SPENDOR_df["Average Purchase Price"] = dlr_avg_purchase_price_SN
analysis_by_SPENDOR_df["Total Purchase Value"] = total_purchase_value_SN 
analysis_by_SPENDOR_df
SUM_SN_purchased_data_df = analysis_by_SPENDOR_df.rename(columns={"Purchase ID":"Purchase Count"})
TOP5_spendors_df=SUM_SN_purchased_data_df.sort_values("Total Purchase Value", ascending=False)
TOP5_spendors_df.head()

dlr_total_purchase_value_SN = total_purchase_value_SN.map("${:,.2f}".format)
TOP5_spendors_df["Total Purchase Value"] = dlr_total_purchase_value_SN
TOP5_spendors_df.head()


# ## Most Popular Items

# * Retrieve the Item ID, Item Name, and Item Price columns
# 
# 
# * Group by Item ID and Item Name. Perform calculations to obtain purchase count, average item price, and total purchase value
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Sort the purchase count column in descending order
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display a preview of the summary data frame
# 
# 

# In[61]:




grp_top_item_df = orig_purchase_data_df.groupby(["Item ID", "Item Name"])
grp_top_item_df.count()

analysis_by_ITEM_df = pd.DataFrame(grp_top_item_df["Purchase ID"].count())
analysis_by_ITEM_df


total_purchase_value_ITEM = grp_top_item_df["Price"].sum()
total_purchase_value_ITEM
dlr_total_purchase_value_ITEM = total_purchase_value_ITEM.map("${:,.2f}".format)
dlr_total_purchase_value_ITEM

purchase_price_ITEM = grp_top_item_df["Price"].mean()
purchase_price_ITEM
dlr_purchase_price_ITEM = purchase_price_ITEM.map("${:,.2f}".format)
dlr_purchase_price_ITEM

analysis_by_ITEM_df["Item Price"] = dlr_purchase_price_ITEM
analysis_by_ITEM_df["Total Purchase Value"] = dlr_total_purchase_value_ITEM
analysis_by_ITEM_df
SUM_ITEM_purchased_data_df = analysis_by_ITEM_df.rename(columns={"Purchase ID":"Purchase Count"})
TOP5_ITEMS_df=SUM_ITEM_purchased_data_df.sort_values("Purchase Count", ascending=False)
TOP5_ITEMS_df.head()


# ## Most Profitable Items

# * Sort the above table by total purchase value in descending order
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display a preview of the data frame
# 
# 

# In[62]:



SUM_ITEM_purchased_data_df["Total Purchase Value"] = grp_top_item_df["Price"].sum()
SUM_ITEM_purchased_data_df


TOP5_ITEMS_df=SUM_ITEM_purchased_data_df.sort_values("Total Purchase Value", ascending=False)


dlr_total_purchase_value_ITEM = total_purchase_value_ITEM.map("${:,.2f}".format)
TOP5_ITEMS_df["Total Purchase Value"] = dlr_total_purchase_value_ITEM
TOP5_ITEMS_df.head()


# In[ ]:





# In[ ]:




