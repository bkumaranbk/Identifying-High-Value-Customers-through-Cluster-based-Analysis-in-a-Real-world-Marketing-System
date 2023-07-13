import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pickle
from sklearn.preprocessing import LabelEncoder, StandardScaler

# Load the preprocessed data
df = pd.read_csv("data_with_clusters.csv")

# Mapping dictionaries
marital_status_mapping = {'Single': 1, 'Married': 2, 'Divorced': 3, 'Together': 4, 'Widow': 5}
education_mapping = {'Graduation': 1, 'PhD': 2, 'Master': 3, 'Basic': 4, '2n Cycle': 5}

# Reverse mapping dictionaries for displaying user-selected values
marital_status_reverse_mapping = {v: k for k, v in marital_status_mapping.items()}
education_reverse_mapping = {v: k for k, v in education_mapping.items()}

def preprocess_data(income, kidhome, teenhome, recency, mnt_wines, mnt_fruits, mnt_meat_products, mnt_fish_products,
                    mnt_sweet_products, mnt_gold_prods, num_deals_purchases, num_web_purchases,
                    num_catalog_purchases, num_store_purchases, num_web_visits_month, age, years_customer,
                    total_expenses, total_acc_cmp, marital_status_selection, education_selection):
    # Convert user-selected options to numerical values
    marital_status = marital_status_mapping[marital_status_selection]
    education = education_mapping[education_selection]
	
    if marital_status is None or education is None:
        st.error("Invalid marital status or education selected. Please try again.")
        return None
		
    # Perform preprocessing steps
    data_prep = pd.DataFrame({'Income': [income],
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
                              'Total_Acc_Cmp': [total_acc_cmp],
                              'Marital_Status': [marital_status],
                              'Education': [education]})

    lenc = LabelEncoder()
    lenc.fit(data_prep['Marital_Status'])
    data_prep['Marital_Status'] = lenc.transform(data_prep['Marital_Status'])

    lenc_edu = LabelEncoder()
    lenc_edu.fit(data_prep['Education'])
    data_prep['Education'] = lenc_edu.transform(data_prep['Education'])

    data_proc = data_prep.copy()

    scaler = StandardScaler()
    std_scaler = np.array(data_proc[['Income', 'Kidhome', 'Teenhome', 'Recency', 'MntWines', 'MntFruits',
                                     'MntMeatProducts', 'MntFishProducts', 'MntSweetProducts', 'MntGoldProds',
                                     'NumDealsPurchases', 'NumWebPurchases', 'NumCatalogPurchases',
                                     'NumStorePurchases', 'NumWebVisitsMonth', 'Age', 'Years_customer',
                                     'Total_Expenses', 'Total_Acc_Cmp']]).reshape(-1, 19)
    scaler.fit(std_scaler)
    data_proc[['Income', 'Kidhome', 'Teenhome', 'Recency', 'MntWines', 'MntFruits', 'MntMeatProducts',
               'MntFishProducts', 'MntSweetProducts', 'MntGoldProds', 'NumDealsPurchases', 'NumWebPurchases',
               'NumCatalogPurchases', 'NumStorePurchases', 'NumWebVisitsMonth', 'Age', 'Years_customer',
               'Total_Expenses', 'Total_Acc_Cmp']] = scaler.transform(std_scaler)
			   

    return data_proc.values.tolist()

def display_plots(cluster_df):
    plt.rcParams["figure.figsize"] = (20, 3)
    num_plots = len(cluster_df.columns) - 3
    num_rows = (num_plots + 2) // 3

    plot_counter = 0

    for feature in cluster_df.drop(['Cluster'], axis=1).columns:
        if plot_counter % 3 == 0:
            if plot_counter > 0:
                st.pyplot(fig)
            fig, axs = plt.subplots(1, 3)
            fig.suptitle('')

        sns.histplot(data=cluster_df, x=feature, kde=True, ax=axs[plot_counter % 3])
        axs[plot_counter % 3].set_title(feature)

        plot_counter += 1

    st.pyplot(fig)
    if plot_counter % 3 != 0:
        for i in range(plot_counter % 3, 3):
            axs[i].axis('off')
            axs[i].set_xticks([])
            axs[i].set_yticks([])

# Load the saved model
filename = 'best_algorithm.sav'
loaded_object = pickle.load(open(filename, 'rb'))

print(type(loaded_object))  # Print the type of the loaded object

st.set_option('deprecation.showPyplotGlobalUse', False)
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
        # Preprocess user input
        data = preprocess_data(income, kidhome, teenhome, recency, mnt_wines, mnt_fruits, mnt_meat_products,
                               mnt_fish_products, mnt_sweet_products, mnt_gold_prods, num_deals_purchases,
                               num_web_purchases, num_catalog_purchases, num_store_purchases, num_web_visits_month,
                               age, years_customer, total_expenses, total_acc_cmp, marital_status_selection,
                               education_selection)

        # Obtain the cluster label by predicting with the loaded model
        clust = loaded_object.predict(data)[0]
        st.write('Data belongs to Cluster', clust)

        cluster_df = df[df['Cluster'] == clust]
        #display_plots(cluster_df)


st.header("Description With Cluster Summary")
def load_data():
    data = pd.read_csv("description_with_cluster.csv")  # Assuming your file is in CSV format
    return data

data = load_data()

# Display the table
st.write(data)

# Cluster Summary
st.header("Cluster Summary")
cluster_summary = df.groupby("Cluster").mean()
st.dataframe(cluster_summary)



# ... (rest of your Streamlit code)
