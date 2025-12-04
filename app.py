import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime

# Configuration de la page
st.set_page_config(
    page_title="E-commerce Analytics Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Styles CSS personnalisés
st.markdown("""
    <style>
    .main {
        padding: 0rem 1rem;
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
    }
    h1 {
        color: #1f77b4;
    }
    </style>
    """, unsafe_allow_html=True)

# Titre principal
st.title("📊 E-commerce Analytics Dashboard")
st.markdown("---")

# Chargement des données avec cache
@st.cache_data
def load_data():
    """Charge toutes les données nécessaires"""
    try:
        transactions = pd.read_csv('data/transactions_cleaned.csv')
        transactions['order_date'] = pd.to_datetime(transactions['order_date'])
        
        products = pd.read_csv('data/sales_by_product.csv')
        monthly = pd.read_csv('data/sales_by_month.csv')
        customers = pd.read_csv('data/top_customers.csv')
        countries = pd.read_csv('data/sales_by_country.csv')
        
        return transactions, products, monthly, customers, countries
    except Exception as e:
        st.error(f"Erreur lors du chargement des données: {e}")
        return None, None, None, None, None

# Charger les données
transactions, products, monthly, customers, countries = load_data()

if transactions is not None:
    
    # Sidebar - Filtres
    st.sidebar.header("🔍 Filtres")
    
    # Filtre par pays
    all_countries = ['Tous'] + list(transactions['country'].unique())
    selected_country = st.sidebar.selectbox("Pays", all_countries)
    
    # Filtre par catégorie
    all_categories = ['Toutes'] + list(transactions['category'].unique())
    selected_category = st.sidebar.selectbox("Catégorie", all_categories)
    
    # Filtre par période
    date_range = st.sidebar.date_input(
        "Période",
        value=(transactions['order_date'].min(), transactions['order_date'].max()),
        min_value=transactions['order_date'].min(),
        max_value=transactions['order_date'].max()
    )
    
    # Appliquer les filtres
    filtered_df = transactions.copy()
    
    if selected_country != 'Tous':
        filtered_df = filtered_df[filtered_df['country'] == selected_country]
    
    if selected_category != 'Toutes':
        filtered_df = filtered_df[filtered_df['category'] == selected_category]
    
    if len(date_range) == 2:
        filtered_df = filtered_df[
            (filtered_df['order_date'] >= pd.to_datetime(date_range[0])) &
            (filtered_df['order_date'] <= pd.to_datetime(date_range[1]))
        ]
    
    st.sidebar.markdown("---")
    st.sidebar.info(f"📦 {len(filtered_df)} transactions affichées")
    
    # === SECTION 1: KPIs PRINCIPAUX ===
    st.header("📈 Vue d'ensemble")
    
    # Calcul des KPIs
    total_revenue = filtered_df['total_amount'].sum()
    total_orders = len(filtered_df)
    avg_basket = filtered_df['total_amount'].mean()
    unique_customers = filtered_df['customer_id'].nunique()
    
    # Affichage des KPIs en colonnes
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(
            label="💰 Chiffre d'Affaires",
            value=f"{total_revenue:,.0f} €",
            delta=f"+{(total_revenue/5000000)*100:.1f}% vs objectif"
        )
    
    with col2:
        st.metric(
            label="📦 Nombre de Commandes",
            value=f"{total_orders:,}",
            delta=f"{total_orders} transactions"
        )
    
    with col3:
        st.metric(
            label="🛒 Panier Moyen",
            value=f"{avg_basket:,.2f} €",
            delta="Par commande"
        )
    
    with col4:
        st.metric(
            label="👥 Clients Uniques",
            value=f"{unique_customers}",
            delta=f"{(total_orders/unique_customers):.1f} cmd/client"
        )
    
    st.markdown("---")
    
    # === SECTION 2: GRAPHIQUES TEMPORELS ===
    st.header("📅 Évolution Temporelle")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # CA mensuel
        monthly_data = filtered_df.groupby(filtered_df['order_date'].dt.to_period('M')).agg({
            'total_amount': 'sum',
            'transaction_id': 'count'
        }).reset_index()
        monthly_data['order_date'] = monthly_data['order_date'].astype(str)
        
        fig_monthly = px.line(
            monthly_data,
            x='order_date',
            y='total_amount',
            title="📊 Chiffre d'Affaires Mensuel",
            labels={'order_date': 'Mois', 'total_amount': 'CA (€)'},
            markers=True
        )
        fig_monthly.update_traces(line_color='#1f77b4', line_width=3)
        st.plotly_chart(fig_monthly, use_container_width=True)
    
    with col2:
        # Commandes par jour de semaine
        filtered_df['day_name'] = pd.to_datetime(filtered_df['order_date']).dt.day_name()
        day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        day_sales = filtered_df.groupby('day_name')['total_amount'].sum().reindex(day_order)
        
        fig_weekday = px.bar(
            x=day_sales.index,
            y=day_sales.values,
            title="📆 Ventes par Jour de la Semaine",
            labels={'x': 'Jour', 'y': 'CA (€)'},
            color=day_sales.values,
            color_continuous_scale='Blues'
        )
        st.plotly_chart(fig_weekday, use_container_width=True)
    
    st.markdown("---")
    
    # === SECTION 3: ANALYSE PRODUITS ===
    st.header("🏆 Performance Produits")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Top 10 produits
        top_products = filtered_df.groupby('product_name')['total_amount'].sum().sort_values(ascending=False).head(10)
        
        fig_products = px.bar(
            x=top_products.values,
            y=top_products.index,
            orientation='h',
            title="🥇 Top 10 Produits par CA",
            labels={'x': 'CA (€)', 'y': 'Produit'},
            color=top_products.values,
            color_continuous_scale='Viridis'
        )
        fig_products.update_layout(showlegend=False, yaxis={'categoryorder':'total ascending'})
        st.plotly_chart(fig_products, use_container_width=True)
    
    with col2:
        # Répartition par catégorie
        category_sales = filtered_df.groupby('category')['total_amount'].sum()
        
        fig_category = px.pie(
            values=category_sales.values,
            names=category_sales.index,
            title="📦 Répartition CA par Catégorie",
            hole=0.4,
            color_discrete_sequence=px.colors.qualitative.Set3
        )
        st.plotly_chart(fig_category, use_container_width=True)
    
    st.markdown("---")
    
    # === SECTION 4: ANALYSE GÉOGRAPHIQUE ===
    st.header("🌍 Analyse Géographique")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Ventes par pays
        country_sales = filtered_df.groupby('country').agg({
            'total_amount': 'sum',
            'customer_id': 'nunique'
        }).sort_values('total_amount', ascending=False)
        
        fig_countries = px.bar(
            country_sales,
            y=country_sales.index,
            x='total_amount',
            orientation='h',
            title="🗺️ CA par Pays",
            labels={'total_amount': 'CA (€)', 'index': 'Pays'},
            color='total_amount',
            color_continuous_scale='RdYlGn'
        )
        st.plotly_chart(fig_countries, use_container_width=True)
    
    with col2:
        # Segmentation clients
        segment_sales = filtered_df.groupby('customer_segment').agg({
            'total_amount': 'sum',
            'customer_id': 'nunique'
        })
        
        fig_segments = px.bar(
            segment_sales,
            x=segment_sales.index,
            y='total_amount',
            title="💎 CA par Segment Client",
            labels={'total_amount': 'CA (€)', 'index': 'Segment'},
            color=segment_sales.index,
            color_discrete_map={'VIP': '#FFD700', 'Premium': '#C0C0C0', 'Standard': '#CD7F32'}
        )
        st.plotly_chart(fig_segments, use_container_width=True)
    
    st.markdown("---")
    
    # === SECTION 5: TABLEAU DE DONNÉES ===
    st.header("📋 Données Détaillées")
    
    # Options d'affichage
    show_data = st.checkbox("Afficher les données brutes")
    
    if show_data:
        st.dataframe(
            filtered_df[['transaction_id', 'order_date', 'product_name', 'category', 
                        'quantity', 'unit_price', 'total_amount', 'country', 'customer_segment']].head(100),
            use_container_width=True
        )
    
    # Footer
    st.markdown("---")
    st.markdown("**📊 E-commerce Analytics Dashboard** | Développé par Oussama Marzouk | Données mises à jour automatiquement")

else:
    st.error("❌ Impossible de charger les données. Vérifiez que les fichiers CSV sont dans le dossier 'data/'")
