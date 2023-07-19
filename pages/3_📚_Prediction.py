import os
os.environ["OMP_NUM_THREADS"] = "1"

from sklearn import preprocessing
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pickle
import threadpoolctl
threadpoolctl.threadpool_limits(0)


def hide_menu():
    hide_css = """
        <style>
        #MainMenu {visibility: hidden;}
        </style>
        """
    st.markdown(hide_css, unsafe_allow_html=True)

hide_menu()


filename = 'final_model.sav'
loaded_model = pickle.load(open(filename, 'rb'))
df = pd.read_csv("data_with_clusters.csv")
st.set_option('deprecation.showPyplotGlobalUse', False)

# Mapping dictionaries
marital_status_mapping = {'Single': 1, 'Married': 2, 'Divorced': 3, 'Together': 4, 'Widow': 5}
education_mapping = {'Graduation': 1, 'PhD': 2, 'Master': 3, 'Basic': 4, '2n Cycle': 5}

# Reverse mapping dictionaries for displaying user-selected values
marital_status_reverse_mapping = {v: k for k, v in marital_status_mapping.items()}
education_reverse_mapping = {v: k for k, v in education_mapping.items()}

st.markdown('<style>body{background-color: Blue;}</style>', unsafe_allow_html=True)
st.title("Prediction")

with st.form("my_form"):
    col1, col2, col3 = st.columns(3)  # Split the columns into three

    with col1:
        income = st.number_input(label='Income', step=0.001, format="%.2f")
        kidhome = st.number_input(label='Kidhome', step=1, min_value=0)
        teenhome = st.number_input(label='Teenhome', step=1, min_value=0)
        recency = st.number_input(label='Recency', step=1, min_value=0)
        mnt_wines = st.number_input(label='Wines', step=1, min_value=0)
        mnt_fruits = st.number_input(label='Fruits', step=1, min_value=0)
        mnt_meat_products = st.number_input(label='Meat Products', step=1, min_value=0)

    with col2:
        mnt_fish_products = st.number_input(label='Fish Products', step=1, min_value=0)
        mnt_sweet_products = st.number_input(label='Sweet Products', step=1, min_value=0)
        mnt_gold_prods = st.number_input(label='Gold Products', step=1, min_value=0)
        num_deals_purchases = st.number_input(label='Number of Deals Purchases', step=1, min_value=0)
        num_web_purchases = st.number_input(label='Number of Web Purchases', step=1, min_value=0)
        num_catalog_purchases = st.number_input(label='Number of Catalog Purchases', step=1, min_value=0)
        num_store_purchases = st.number_input(label='Number of Store Purchases', step=1, min_value=0)

    with col3:
        num_web_visits_month = st.number_input(label='Number of Web Visits Month', step=1, min_value=0)
        age = st.number_input(label='Age', step=1, min_value=0)
        years_customer = st.number_input(label='Years customer', step=1, min_value=0)
        total_expenses = st.number_input(label='Total Expenses', step=1, min_value=0)
        total_acc_cmp = st.number_input(label='Total Acc_Cmp', step=1, min_value=0)
        marital_status_selection = st.selectbox(label='Marital Status', options=list(marital_status_mapping.keys()))
        education_selection = st.selectbox(label='Education', options=list(education_mapping.keys()))

    submitted = st.form_submit_button("Submit")

if submitted:
    # Convert user-selected options to numerical values
    marital_status = marital_status_mapping[marital_status_selection]
    education = education_mapping[education_selection]

    # Prepare the new data point(s)
    data = pd.DataFrame({
    'Education': [education],
    'Marital_Status': [marital_status],
    'Income': [income],
    'Kidhome': [kidhome],
    'Teenhome': [teenhome],
    'Recency': [recency],
    'MntWines': [mnt_wines],
    'MntFruits': [mnt_fruits],
    'MntMeatProducts': [mnt_meat_products],
    'MntFishProducts': [mnt_fish_products],
    'MntSweetProducts': [mnt_sweet_products],
    'MntGoldProds': [mnt_gold_prods],
    'NumDealsPurchases': [num_deals_purchases],
    'NumWebPurchases': [num_web_purchases],
    'NumCatalogPurchases': [num_catalog_purchases],
    'NumStorePurchases': [num_store_purchases],
    'NumWebVisitsMonth': [num_web_visits_month],
    'Age': [age],
    'Years_customer': [years_customer],
    'Total_Expenses': [total_expenses],
    'Total_Acc_Cmp': [total_acc_cmp]
    })
    new_data_features = data
    clust = loaded_model.predict(new_data_features)
	
    #st.write('Data belongs to Cluster', clust)
	
	# Cluster Explanation with Color-coded Cards and Average/Below Average Labels
    if clust == 0:
        st.markdown(
            f'<div style="border: 2px solid red; padding: 10px; border-radius: 5px;"><h3>Cluster 0 - Below Average</h3>'
            f'<p>This data belongs to Cluster 0.</p>'
            f'<p>This cluster represents the least number of customers. They have a relatively high income level and spend a significant amount on wine products. Customers in this cluster make a larger number of purchases through stores compared to other clusters. However, they do not make many catalog purchases.</p></div>',
            unsafe_allow_html=True
        )

    elif clust == 1:
        st.markdown(
            f'<div style="border: 2px solid orange; padding: 10px; border-radius: 5px;"><h3>Cluster 1 - Average</h3>'
            f'<p>This data belongs to Cluster 1.</p>'
            f'<p>This cluster has the largest number of customers. They have the lowest income level among the clusters and are not accustomed to making catalog purchases. The amount spent on wine products in this cluster is relatively low..</p></div>',
            unsafe_allow_html=True
        )

    elif clust == 2:
        st.markdown(
            f'<div style="border: 2px solid blue; padding: 10px; border-radius: 5px;"><h3>Above Average</h3>'
            f'<p>This data belongs to Cluster 2.</p>'
            f'<p>This cluster comprises customers with the highest income level. They spend the largest amount on all types of products and make a significant number of purchases. Despite having a relatively moderate number of customers, they are the highest spenders.</p></div>',
            unsafe_allow_html=True
        )

    elif clust == 3:
        st.markdown(
            f'<div style="border: 2px solid green; padding: 10px; border-radius: 5px;"><h3>Cluster 3 - High</h3>'
            f'<p>This data belongs to Cluster 3.</p>'
            f'<p>Customers in this cluster spend a large amount on meat and wine products. They also spend a moderate amount on fish products. This cluster has a high number of store purchases. Customers in this cluster have a high income level. It has a moderate number of customers compared to other clusters.</p></div>',
            unsafe_allow_html=True
        )

    else:
        st.markdown(
            f'<div style="border: 2px solid gray; padding: 10px; border-radius: 5px;"><h3>Unknown Cluster</h3>'
            f'<p>This data does not belong to any specific cluster.</p></div>',
            unsafe_allow_html=True
        )


    #cluster_df1 = df[df['Cluster'] == clust]
    #plt.rcParams["figure.figsize"] = (20, 3)
    #for c in cluster_df1.drop(['Cluster'], axis=1):
        #fig, ax = plt.subplots()
        #grid = sns.FacetGrid(cluster_df1, col='Cluster')
        #grid = grid.map(plt.hist, c)
        #plt.show()
        #st.pyplot(figsize=(5, 5))

    st.header("Description With Cluster Summary")
    def load_data():
        data = pd.read_csv("profile_customer.csv")  # Assuming your file is in CSV format
        return data

    data = load_data()

    # Display the table
    st.write(data)


    # Cluster Summary
    st.header("Cluster Summary")
    cluster_summary = df.groupby("Cluster").mean()
    st.dataframe(cluster_summary)