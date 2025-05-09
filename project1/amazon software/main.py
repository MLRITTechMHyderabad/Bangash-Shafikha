#  Import Libraries 
import pandas as pd
import numpy as np
from sqlalchemy import create_engine
import matplotlib.pyplot as plt
import seaborn as sns

# Visual Style
sns.set(style="whitegrid")
plt.rcParams["figure.figsize"] = (10, 6)

#  Step 1: Load CSV 
file_path = r"C:\\Users\\bshaf\\OneDrive\\Desktop\\Revature\\project1\\amazon software\\best_sellers_data2 (1).csv"
df = pd.read_csv(file_path)

#  Step 2: Clean & Transform 
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

# Clean 'product_price' column
df['product_price'] = df['product_price'].astype(str)
df['product_price'] = df['product_price'].str.replace(r'[\$,€]', '', regex=True)
df['product_price'] = df['product_price'].str.replace(r'\xa0', '', regex=True)
df['product_price'] = df['product_price'].str.strip()
df['product_price'] = pd.to_numeric(df['product_price'], errors='coerce')

# Convert rating and review count
df['product_star_rating'] = pd.to_numeric(df['product_star_rating'], errors='coerce')
df['product_num_ratings'] = pd.to_numeric(df['product_num_ratings'], errors='coerce')

# Remove duplicates and missing essential info
df = df.drop_duplicates()
df = df.dropna(subset=['product_title', 'product_price', 'product_star_rating', 'product_num_ratings'])

# Step 3: Store in MySQL
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'shaffu',  # Replace with your MySQL password
    'database': 'amazon_software'
}

engine = create_engine(
    f"mysql+mysqlconnector://{db_config['user']}:{db_config['password']}@{db_config['host']}/{db_config['database']}"
)

table_name = "best_sellers"
df.to_sql(table_name, con=engine, if_exists='replace', index=False)

#  Step 4: Data Analysis 
top_rated = df.sort_values(by='product_star_rating', ascending=False).head(10)
most_reviewed = df.sort_values(by='product_num_ratings', ascending=False).head(10)

avg_rating = df['product_star_rating'].mean()
avg_reviews = df['product_num_ratings'].mean()

avg_price_per_rank = df.groupby('rank')['product_price'].mean().reset_index()

df['is_free'] = df['product_price'] == 0
paid_vs_free = df.groupby('is_free')[['product_star_rating', 'product_num_ratings']].mean().reset_index()

correlation = df['product_star_rating'].corr(df['product_num_ratings'])

Q1 = df['product_price'].quantile(0.25)
Q3 = df['product_price'].quantile(0.75)
IQR = Q3 - Q1
outliers = df[(df['product_price'] < Q1 - 1.5 * IQR) | (df['product_price'] > Q3 + 1.5 * IQR)]

# Step 5: Console Output 
print("\n Top 10 Best-Rated Software:")
print(top_rated[['product_title', 'product_star_rating']])

print("\n Most Reviewed Software:")
print(most_reviewed[['product_title', 'product_num_ratings']])

print(f"\n Average Rating: {avg_rating:.2f}")
print(f" Average Number of Reviews: {avg_reviews:.2f}")

print("\n Average Price per Rank:")
print(avg_price_per_rank)

print("\n Paid vs Free Software Performance:")
print(paid_vs_free)

print(f"\n Correlation between Rating and Reviews: {correlation:.2f}")

print("\n Price Outliers Detected:")
print(outliers[['product_title', 'product_price']])

#  Step 6: Visualizations 

# 1. Top 10 Best-Rated Software
plt.figure()
sns.barplot(data=top_rated, x='product_star_rating', y='product_title', hue='product_title', palette="viridis", legend=False)
plt.title("Top 10 Best-Rated Software")
plt.xlabel("Star Rating")
plt.ylabel("Product Title")
plt.tight_layout()
plt.show()

# 2. Most Reviewed Products
plt.figure()
sns.barplot(data=most_reviewed, x='product_num_ratings', y='product_title', hue='product_title', palette="magma", legend=False)
plt.title("Top 10 Most Reviewed Software")
plt.xlabel("Number of Reviews")
plt.ylabel("Product Title")
plt.tight_layout()
plt.show()

# 4. Paid vs Free: Avg Rating & Review Count
fig, ax1 = plt.subplots(1, 2, figsize=(14, 5))

sns.barplot(data=paid_vs_free, x='is_free', y='product_star_rating', hue='is_free', ax=ax1[0], palette="coolwarm", legend=False)
ax1[0].set_title("Avg Rating: Free vs Paid")
ax1[0].set_xticks([0, 1])
ax1[0].set_xticklabels(['Paid', 'Free'])

sns.barplot(data=paid_vs_free, x='is_free', y='product_num_ratings', hue='is_free', ax=ax1[1], palette="coolwarm", legend=False)
ax1[1].set_title("Avg Reviews: Free vs Paid")
ax1[1].set_xticks([0, 1])
ax1[1].set_xticklabels(['Paid', 'Free'])

plt.tight_layout()
plt.show()
