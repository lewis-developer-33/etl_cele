import streamlit as st
import time
import pandas as pd
import matplotlib.pyplot as plt

with st.sidebar:
    st.markdown('## ETL Process')

    page = st.selectbox(
    "Which step are you at",
    ("Extract", "Load","Analyze" )
    )

if page == 'Extract':
    with st.spinner("Loading..."):
        time.sleep(5)
    st.markdown('# Data was extracted from a Brazillian ecommerce dataset')
    st.link_button("Check out data source", "https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce")

    st.markdown('## Data breakdown')
    st.write('Dataset had several csv files. Here are a couple of them ')

    df_customers = pd.read_csv('input/olist_customers_dataset.csv')
    df_orders = pd.read_csv('input/olist_orders_dataset.csv')
    df_sellers = pd.read_csv('input/olist_sellers_dataset.csv')
    df_products = pd.read_csv('input/olist_products_dataset.csv')
    df_payments = pd.read_csv('input/olist_order_payments_dataset.csv')

    selected = st.selectbox(
    "Choose csv file to check out",
    ("Customers", "Orders", "Sellers","Products",'Payments'))

    if selected == 'Customers':
        st.dataframe(df_customers)
    if selected == 'Sellers':
        st.dataframe(df_sellers)
    if selected == 'Products':
        st.dataframe(df_products)
    if selected == 'Orders':
        st.dataframe(df_orders)
    if selected == 'Payments':
        st.dataframe(df_payments)

if page == 'Load':
    with st.spinner("Loading..."):
        time.sleep(5)
    st.markdown('# Data was transformed from csv format to sql format using sqlite')
    
    with open("etl.db", "rb") as file:
        st.download_button(
            label="Download database",
            data=file,
            file_name="etl.db",
            mime="text/db"
          )
        
if page == 'Analyze':
    with st.spinner("Loading..."):
        time.sleep(5)
    st.markdown('# Analyzing the dataset, to gain some insights')
    
    df_merged = pd.merge(df_customers,df_orders,on='customer_id',how='left')

    # Dropped null values and duplicates
    df_merged = df_merged.dropna()
    df_merged = df_merged.drop_duplicates()
    df_group = df_merged.groupby(['customer_state'])
    st.write(df_group)

    



