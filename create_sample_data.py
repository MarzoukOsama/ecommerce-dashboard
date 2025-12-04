import pandas as pd

print("🔄 Création des fichiers sample pour déploiement...")

# Charger les données complètes
transactions = pd.read_csv('data/transactions_cleaned.csv')

# Créer un sample de 100 transactions
sample_transactions = transactions.sample(n=100, random_state=42)
sample_transactions.to_csv('data/transactions_cleaned.csv', index=False)
print(f"✅ transactions_cleaned.csv : {len(sample_transactions)} lignes")

# Recalculer les agrégats basés sur le sample
# Sales by product
products = sample_transactions.groupby(['product_name', 'category']).agg({
    'total_amount': 'sum',
    'quantity': 'sum',
    'transaction_id': 'count'
}).rename(columns={'transaction_id': 'nb_orders'}).reset_index()
products.to_csv('data/sales_by_product.csv', index=False)
print(f"✅ sales_by_product.csv : {len(products)} lignes")

# Sales by month
sample_transactions['order_date'] = pd.to_datetime(sample_transactions['order_date'])
monthly = sample_transactions.groupby([
    sample_transactions['order_date'].dt.year.rename('year'),
    sample_transactions['order_date'].dt.month.rename('month')
]).agg({
    'total_amount': 'sum',
    'transaction_id': 'count',
    'customer_id': lambda x: x.nunique()
}).rename(columns={
    'transaction_id': 'nb_orders',
    'customer_id': 'unique_customers'
}).reset_index()
monthly.to_csv('data/sales_by_month.csv', index=False)
print(f"✅ sales_by_month.csv : {len(monthly)} lignes")

# Top customers
customers = sample_transactions.groupby('customer_id').agg({
    'total_amount': 'sum',
    'transaction_id': 'count',
    'customer_segment': 'first'
}).rename(columns={'transaction_id': 'nb_orders'}).sort_values('total_amount', ascending=False).head(20).reset_index()
customers.to_csv('data/top_customers.csv', index=False)
print(f"✅ top_customers.csv : {len(customers)} lignes")

# Sales by country
countries = sample_transactions.groupby('country').agg({
    'total_amount': 'sum',
    'transaction_id': 'count',
    'customer_id': lambda x: x.nunique()
}).rename(columns={
    'transaction_id': 'nb_orders',
    'customer_id': 'unique_customers'
}).sort_values('total_amount', ascending=False).reset_index()
countries.to_csv('data/sales_by_country.csv', index=False)
print(f"✅ sales_by_country.csv : {len(countries)} lignes")

print("\n✨ Fichiers sample créés avec succès !")
print("📦 Prêt pour le déploiement Streamlit Cloud")
