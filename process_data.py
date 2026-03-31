import pandas as pd

# Contcatenate the three CSV files into a single DataFrame
morsel_df = pd.concat([pd.read_csv('data/daily_sales_data_0.csv'),
          pd.read_csv('data/daily_sales_data_1.csv'),
          pd.read_csv('data/daily_sales_data_2.csv')], ignore_index=True)

# Remove rows where the product is not 'pink morsel'
morsel_df = morsel_df[morsel_df['product'] == 'pink morsel']

# Strip currcency symbols from price, and consolidate price and quantity into a single sales column
morsel_df['price'] = morsel_df['price'].str.replace('$', '').astype(float)
morsel_df['sales'] = morsel_df['price'] * morsel_df['quantity']

# Select final columns for output
output_df = morsel_df[['sales', 'date', 'region']]

# Convert dataframe to CSV
output_df.to_csv('data/pink_morsel_data.csv', index=False)
print("Data processing complete. Output saved to 'data/pink_morsel_data.csv'.")
