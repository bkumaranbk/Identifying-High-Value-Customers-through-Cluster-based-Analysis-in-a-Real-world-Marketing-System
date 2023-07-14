from sklearn import preprocessing
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pickle

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
df = pd.read_csv("Clustered_Customer_Data.csv")
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
        mnt_wines = st.number_input(label='MntWines', step=1, min_value=0)
        mnt_fruits = st.number_input(label='MntFruits', step=1, min_value=0)
        mnt_meat_products = st.number_input(label='MntMeatProducts', step=1, min_value=0)

    with col2:
        mnt_fish_products = st.number_input(label='MntFishProducts', step=1, min_value=0)
        mnt_sweet_products = st.number_input(label='MntSweetProducts', step=1, min_value=0)
        mnt_gold_prods = st.number_input(label='MntGoldProds', step=1, min_value=0)
        num_deals_purchases = st.number_input(label='NumDealsPurchases', step=1, min_value=0)
        num_web_purchases = st.number_input(label='NumWebPurchases', step=1, min_value=0)
        num_catalog_purchases = st.number_input(label='NumCatalogPurchases', step=1, min_value=0)
        num_store_purchases = st.number_input(label='NumStorePurchases', step=1, min_value=0)

    with col3:
        num_web_visits_month = st.number_input(label='NumWebVisitsMonth', step=1, min_value=0)
        age = st.number_input(label='Age', step=1, min_value=0)
        years_customer = st.number_input(label='Years_customer', step=1, min_value=0)
        total_expenses = st.number_input(label='Total_Expenses', step=1, min_value=0)
        total_acc_cmp = st.number_input(label='Total_Acc_Cmp', step=1, min_value=0)
        marital_status_selection = st.selectbox(label='Marital_Status', options=list(marital_status_mapping.keys()))
        education_selection = st.selectbox(label='Education', options=list(education_mapping.keys()))

    submitted = st.form_submit_button("Submit")

if submitted:
    # Convert user-selected options to numerical values
    marital_status = marital_status_mapping[marital_status_selection]
    education = education_mapping[education_selection]

    data = [[income, kidhome, teenhome, recency, mnt_wines, mnt_fruits, mnt_meat_products, mnt_fish_products,
                 mnt_sweet_products, mnt_gold_prods, num_deals_purchases, num_web_purchases, num_catalog_purchases,
                 num_store_purchases, num_web_visits_month, age, years_customer, total_expenses, total_acc_cmp,
                 marital_status, education]]

    clust = loaded_model.predict(data)[0]
    st.write('Data belongs to Cluster', clust)
	
	# Cluster Explanation with Color-coded Cards and Average/Below Average Labels
    if clust == 0:
        st.markdown(
            f'<div style="border: 2px solid blue; padding: 10px; border-radius: 5px;"><h3>Cluster 0 - Average</h3>'
            f'<p>This data belongs to Cluster 0.</p>'
            f'<p>This cluster represents the least number of customers, suggesting a smaller customer base.</p>'
            f'<p>Customers in this cluster make a relatively large number of purchases through stores, indicating a preference for in-store shopping.</p>'
            f'<p>They spend a significant amount on wine products, suggesting a potential interest in wine consumption.</p>'
            f'<p>The median income level of this cluster indicates an average income range.</p>'
			f'<p>Customers in this cluster do not make many catalog purchases, indicating a lower engagement with catalog marketing.</p></div>',
            unsafe_allow_html=True
        )

    elif clust == 1:
        st.markdown(
            f'<div style="border: 2px solid red; padding: 10px; border-radius: 5px;"><h3>Cluster 1 - Below Average</h3>'
            f'<p>This data belongs to Cluster 1.</p>'
            f'<p>This cluster has the largest number of customers, indicating a larger customer base.</p>'
            f'<p>Customers in this cluster have the lowest income level, suggesting a lower purchasing power compared to other clusters.</p>'
            f'<p>They are not accustomed to making catalog purchases, indicating a lower interest or engagement with catalog marketing.</p>'
			f'<p>The least amount of money is spent on wine products in this cluster, indicating a lower preference for wine consumption.</p></div>',
            unsafe_allow_html=True
        )

    elif clust == 2:
        st.markdown(
            f'<div style="border: 2px solid green; padding: 10px; border-radius: 5px;"><h3>Cluster 2 - High</h3>'
            f'<p>This data belongs to Cluster 2.</p>'
            f'<p>This cluster represents customers with the highest income level, indicating stronger purchasing power compared to other clusters.</p>'
            f'<p>Customers in this cluster spend the largest amount on all types of products, suggesting a higher level of engagement and willingness to invest in various items.</p>'
            f'<p>The relatively moderate number of customers in this cluster suggests exclusivity and targeted marketing opportunities.</p>'
			f'<p>The cluster includes a relatively moderate number of customers, indicating exclusivity and potentially a more targeted customer segment.</p></div>',
            unsafe_allow_html=True
        )

    elif clust == 3:
        st.markdown(
            f'<div style="border: 2px solid orange; padding: 10px; border-radius: 5px;"><h3>Cluster 3 - Above Average</h3>'
            f'<p>This data belongs to Cluster 3.</p>'
            f'<p>Customers in this cluster spend a large amount on meat and wine products, indicating a preference for these items.</p>'
            f'<p>They also spend a moderate amount on fish products, suggesting a moderate interest in seafood.</p>'
			f'<p>The cluster has a high number of store purchases, indicating a preference for in-store shopping.</p>'
			f'<p>Customers in this cluster have a high income level, suggesting strong purchasing power.</p>'
            f'<p>It has a moderate number of customers, indicating a more targeted segment.</p></div>',
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
        data = pd.read_csv("description_cluster.csv")  # Assuming your file is in CSV format
        return data

    data = load_data()

    # Display the table
    st.write(data)


    # Cluster Summary
    st.header("Cluster Summary")
    cluster_summary = df.groupby("Cluster").mean()
    st.dataframe(cluster_summary)