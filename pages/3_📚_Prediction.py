import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np 
import pickle
from sklearn.preprocessing import LabelEncoder, OrdinalEncoder, StandardScaler

filename = 'best_classification_algorithm.sav'
loaded_model = pickle.load(open(filename, 'rb'))
df = pd.read_csv("data_with_clusters.csv")
st.set_option('deprecation.showPyplotGlobalUse', False)

st.markdown('<style>body{background-color: Blue;}</style>', unsafe_allow_html=True)
st.title("Prediction")

# Mapping dictionaries
marital_status_mapping = {'Single': 1, 'Married': 2, 'Divorced': 3, 'Together': 4, 'Widow': 5}
education_mapping = {'Graduation': 1, 'PhD': 2, 'Master': 3, 'Basic': 4, '2n Cycle': 5}


# Reverse mapping dictionaries for displaying user-selected values
marital_status_reverse_mapping = {v: k for k, v in marital_status_mapping.items()}
education_reverse_mapping = {v: k for k, v in education_mapping.items()}

# Initialize LabelEncoder, OrdinalEncoder, and StandardScaler
lenc = LabelEncoder()
lenc.fit(df['Marital_Status'])  # Fit the LabelEncoder
ore = OrdinalEncoder(categories=[['Basic', 'Graduation', 'Master', '2n Cycle', 'PhD']])
scaler = StandardScaler()
std_scaler = scaler.fit_transform(df[['Income', 'Kidhome', 'Teenhome', 'Recency', 'MntWines', 'MntFruits',
                                      'MntMeatProducts', 'MntFishProducts', 'MntSweetProducts', 'MntGoldProds',
                                      'NumDealsPurchases', 'NumWebPurchases', 'NumCatalogPurchases',
                                      'NumStorePurchases', 'NumWebVisitsMonth', 'Age', 'Years_customer',
                                      'Total_Expenses', 'Total_Acc_Cmp']])

def preprocess_data(income, kidhome, teenhome, recency, mnt_wines, mnt_fruits, mnt_meat_products, mnt_fish_products,
                    mnt_sweet_products, mnt_gold_prods, num_deals_purchases, num_web_purchases,
                    num_catalog_purchases, num_store_purchases, num_web_visits_month, age, years_customer,
                    total_expenses, total_acc_cmp, marital_status_selection, education_selection):
    # Convert user-selected options to numerical values
    marital_status = marital_status_mapping[marital_status_selection]
    education = education_mapping[education_selection]

    data = [[income, kidhome, teenhome, recency, mnt_wines, mnt_fruits, mnt_meat_products, mnt_fish_products,
             mnt_sweet_products, mnt_gold_prods, num_deals_purchases, num_web_purchases, num_catalog_purchases,
             num_store_purchases, num_web_visits_month, age, years_customer, total_expenses, total_acc_cmp,
             marital_status, education]]

    # Apply Label Encoding to Marital_Status
    marital_status_encoded = lenc.transform([marital_status])
    data[0][-2] = marital_status_encoded

    # Apply Label Encoding to Education
    education_encoded = lenc.transform([education])
    data[0][-1] = education_encoded

    # Standardize numerical features
    numerical_features = np.array(data[0][:-2]).reshape(1, -1)
    standardized_features = scaler.transform(numerical_features)
    data[0][:-2] = standardized_features.tolist()[0]

    return data




def display_plots(cluster_df):
    plt.rcParams["figure.figsize"] = (20, 3)

    num_plots = len(cluster_df.columns) - 3  # Number of plots to display (excluding 'ID' and 'Year_Birth' columns)
    num_rows = (num_plots + 2) // 3  # Calculate number of rows for the grid

    plot_counter = 0

    for feature in cluster_df.drop(['Cluster'], axis=1).columns:
        if plot_counter % 3 == 0:
            if plot_counter > 0:
                st.pyplot(fig)  # Display the previous row of plots
            fig, axs = plt.subplots(1, 3)
            fig.suptitle('')

        sns.histplot(data=cluster_df, x=feature, kde=True, ax=axs[plot_counter % 3])
        axs[plot_counter % 3].set_title(feature)

        plot_counter += 1

    st.pyplot(fig)  # Display the last row of plots
    if plot_counter % 3 != 0:
        # If the last row doesn't have 3 plots, display an empty plot to fill the grid
        for i in range(plot_counter % 3, 3):
            axs[i].axis('off')
            axs[i].set_xticks([])
            axs[i].set_yticks([])


with st.form("my_form"):
    col1, col2, col3 = st.columns(3)  # Split the columns into three

    with col1:
        income = st.number_input(label='Income', step=0.001, format="%.6f")
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
        # Preprocess user input
        data = preprocess_data(income, kidhome, teenhome, recency, mnt_wines, mnt_fruits, mnt_meat_products,
                               mnt_fish_products, mnt_sweet_products, mnt_gold_prods, num_deals_purchases,
                               num_web_purchases, num_catalog_purchases, num_store_purchases, num_web_visits_month,
                               age, years_customer, total_expenses, total_acc_cmp, marital_status_selection,
                               education_selection)

        # Obtain the cluster label by predicting with the loaded model
        clust = loaded_model.predict(data)[0]
        st.write('Data belongs to Cluster', clust)

        cluster_df = df[df['Cluster'] == clust]
        #display_plots(cluster_df)
