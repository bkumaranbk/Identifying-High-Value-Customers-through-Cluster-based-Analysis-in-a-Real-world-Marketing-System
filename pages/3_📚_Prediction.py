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
marital_status_mapping = {'Single': 0, 'Married': 1, 'Divorced': 2, 'Together': 3, 'Widow': 4}
education_mapping = {'Graduation': 0, 'PhD': 1, 'Master': 2, 'Basic': 3, '2n Cycle': 4}

# Reverse mapping dictionaries for displaying user-selected values
marital_status_reverse_mapping = {v: k for k, v in marital_status_mapping.items()}
education_reverse_mapping = {v: k for k, v in education_mapping.items()}


default_marital_status0 = 'Single'
default_education0 = 'Graduation'
default_marital_status1 = 'Single'
default_education1 = 'Basic'
default_marital_status2 = 'Married'
default_education2 = 'PhD'
default_marital_status3 = 'Single'
default_education3 = 'Graduation'
# Define default values for each button
default_values_1 = {
    'Income': 35790.00,
    'Kidhome': 1,
    'Teenhome': 0,
    'Recency': 54,
    'Wines':12,
    'Fruits': 6,
    'Meat': 20,
    'Response': 0,
    'Fish':30,
    'Sweet': 1,
    'Gold': 3,
    'Deals':2,
    'Web':2,
    'Catalog':0,
    'Store': 3,
    'Age':46,
    'Web_Visits':7,
    'Years':10,
    'Expenses':72,
    'Acc_Cmp':0,
    'Marital': marital_status_mapping[default_marital_status0],
    'Education': education_mapping[default_education0],
}

default_values_2 = {
    'Income': 88194.00,
    'Kidhome': 0,
    'Teenhome': 1,
    'Recency': 19,
    'Wines':688,
    'Fruits': 14,
    'Meat': 309,
    'Response': 1,
    'Fish':201,
    'Sweet': 24,
    'Gold': 38,
    'Deals':1,
    'Web':11,
    'Catalog':10,
    'Store': 10,
    'Age':44,
    'Web_Visits':5,
    'Years':9,
    'Expenses':1274,
    'Acc_Cmp':3,
    'Marital': marital_status_mapping[default_marital_status1],
    'Education': education_mapping[default_education1],
}

default_values_3 = {
    'Income': 52247.25,
    'Kidhome': 2,
    'Teenhome': 1,
    'Recency': 4,
    'Wines':230,
    'Fruits': 42,
    'Meat': 192,
    'Response': 0,
    'Fish':49,
    'Sweet': 37,
    'Gold': 53,
    'Deals':12,
    'Web':7,
    'Catalog':2,
    'Store': 8,
    'Age':66,
    'Web_Visits':9,
    'Years':11,
    'Expenses':603,
    'Acc_Cmp':0,
    'Marital': marital_status_mapping[default_marital_status2],
    'Education': education_mapping[default_education2],
}

default_values_4 = {
    'Income': 30630.00,
    'Kidhome': 1,
    'Teenhome': 1,
    'Recency': 67,
    'Wines':27,
    'Fruits': 1,
    'Meat': 12,
    'Response': 0,
    'Fish':2,
    'Sweet': 0,
    'Gold': 10,
    'Deals':2,
    'Web':2,
    'Catalog':0,
    'Store': 3,
    'Age':58,
    'Web_Visits':7,
    'Years':9,
    'Expenses':52,
    'Acc_Cmp':0,
    'Marital': marital_status_mapping[default_marital_status3],
    'Education': education_mapping[default_education3],
}
st.title("Prediction")

st.subheader("Random Test Cases")
# Arrange the "Test" buttons side by side
button_1, button_2, button_3, button_4 = st.columns(4)
with button_1:
    if st.button("Test case 1 (54th Record)"):
        # st.write("Setting Cluster 0")
        for col, value in default_values_1.items():
            st.session_state[col] = value

with button_2:
    if st.button("Test case 2 (69th Record)"):
        # st.write("Setting Cluster 1")
        for col, value in default_values_2.items():
            st.session_state[col] = value

with button_3:
    if st.button("Test case 3 (92th Record)"):
        # st.write("Setting Cluster 2")
        for col, value in default_values_3.items():
            st.session_state[col] = value

with button_4:
    if st.button("Test case 4 (519th Record)"):
        # st.write("Setting Cluster 3")
        for col, value in default_values_4.items():
            st.session_state[col] = value
        

st.markdown('<style>body{background-color: Blue;}</style>', unsafe_allow_html=True)
# Define a function for form validation
def validate_form():
    required_fields = [income, kidhome, teenhome, recency, mnt_wines, mnt_fruits, mnt_meat_products,
                       mnt_fish_products, mnt_sweet_products, mnt_gold_prods, num_deals_purchases,
                       num_web_purchases, num_catalog_purchases, num_store_purchases,
                       num_web_visits_month, response, age, years_customer, total_expenses, total_acc_cmp]
    
    for field in required_fields:
        if field is None:
            return False
    return True
	


with st.form("my_form"):
    col1, col2, col3 = st.columns(3)  # Split the columns into four

    with col1:
        income = st.number_input(label='Income *', format="%.2f", value=st.session_state.get('Income', 0.00))
        kidhome = st.number_input(label='Kidhome *', step=1, min_value=0, value=st.session_state.get('Kidhome', 0))
        teenhome = st.number_input(label='Teenhome *', step=1, min_value=0, value=st.session_state.get('Teenhome', 0))
        recency = st.number_input(label='Recency *', step=1, min_value=0, value=st.session_state.get('Recency', 0))
        mnt_wines = st.number_input(label='Wines *', step=1, min_value=0, value=st.session_state.get('Wines', 0))
        mnt_fruits = st.number_input(label='Fruits *', step=1, min_value=0, value=st.session_state.get('Fruits', 0))
        mnt_meat_products = st.number_input(label='Meat Products *', step=1, min_value=0, value=st.session_state.get('Meat', 0))
        response = st.number_input(label='Response (1 or 0) *', step=1, min_value=0, max_value=1, value=st.session_state.get('Response', 0))

    with col2:
        mnt_fish_products = st.number_input(label='Fish Products *', step=1, min_value=0, value=st.session_state.get('Fish', 0))
        mnt_sweet_products = st.number_input(label='Sweet Products *', step=1, min_value=0, value=st.session_state.get('Sweet', 0))
        mnt_gold_prods = st.number_input(label='Gold Products*', step=1, min_value=0, value=st.session_state.get('Gold', 0))
        num_deals_purchases = st.number_input(label='Number of Deals Purchases *', step=1, min_value=0, value=st.session_state.get('Deals', 0))
        num_web_purchases = st.number_input(label='Number of Web Purchases *', step=1, min_value=0, value=st.session_state.get('Web', 0))
        num_catalog_purchases = st.number_input(label='Number of Catalog Purchases *', step=1, min_value=0, value=st.session_state.get('Catalog', 0))
        num_store_purchases = st.number_input(label='Number of Store Purchases *', step=1, min_value=0, value=st.session_state.get('Store', 0))

    with col3:
        num_web_visits_month = st.number_input(label='Number of Web Visits Month *', step=1, min_value=0, value=st.session_state.get('Web_Visits', 0))
        age = st.number_input(label='Age *', step=1, min_value=0, value=st.session_state.get('Age', 0))
        years_customer = st.number_input(label='Years customer *', step=1, min_value=0, value=st.session_state.get('Years', 0))
        total_expenses = st.number_input(label='Total Expenses *', step=1, min_value=0, value=st.session_state.get('Expenses', 0))
        total_acc_cmp = st.number_input(label='Total Acc_Cmp *', step=1, min_value=0, value=st.session_state.get('Acc_Cmp', 0))
        marital_status_selection = st.selectbox(label='Marital Status *', options=list(marital_status_mapping.keys()), index=st.session_state.get('Marital', 0))
        education_selection = st.selectbox(label='Education *', options=list(education_mapping.keys()), index=st.session_state.get('Education', 0))

    submitted = st.form_submit_button("Submit")

# Add a "Clear" button
clear_button = st.button("Clear Form")

# Handle clear button click
if clear_button:
    st.session_state.clear()  # Clear all input field values


if submitted:
    if validate_form():
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
		'Response': [response],
        'Age': [age],
        'Years_customer': [years_customer],
        'Total_Expenses': [total_expenses],
        'Total_Acc_Cmp': [total_acc_cmp]
        })
        new_data_features = data
        clust = loaded_model.predict(new_data_features)
    else:
        st.error("Please fill in all the mandatory fields (*) before submitting.")
	
	# Cluster Explanation with Color-coded Cards and Average/Below Average Labels
    if clust == 0:
        st.markdown(
            f'<div style="border: 2px solid orange; padding: 10px; border-radius: 5px;"><h3>Cluster 0 - Average</h3>'
            f'<p>This data belongs to Cluster 1: Budget-Conscious Families</p>'
            f'<p>This cluster is the largest segment, consisting of average-income families. They are not accustomed to making catalog purchases and have the lowest spending on wine products among the clusters. Their focus is on essentials rather than luxury items. With a balanced number of kids and teenagers at home, their expenses might be primarily directed towards family needs. They show moderate recency in purchases, suggesting a careful approach to spending. Despite their lower income, they are responsible consumers who prioritize family well-being.</p></div>',
            unsafe_allow_html=True
        )
        

    elif clust == 1:
        st.markdown(
            f'<div style="border: 2px solid green; padding: 10px; border-radius: 5px;"><h3>Cluster 1 - High</h3>'
            f'<p>This data belongs to Cluster 3: Gourmet Enthusiasts</p>'
            f'<p>Customers in this cluster exhibit specific preferences for premium food products, especially meat and wine. They have a high income level and are willing to invest in gourmet experiences. Although they have a moderate number of customers, they spend generously on their favorite items. Store purchases are common, suggesting that they value personal interactions and expertise while shopping. They might be food enthusiasts who enjoy cooking and exploring unique flavors. With moderate recency, they are likely to be discerning customers who seek quality and variety in their purchases.</p></div>',
            unsafe_allow_html=True
        )
        
    elif clust == 2:
        st.markdown(
            f'<div style="border: 2px solid blue; padding: 10px; border-radius: 5px;"><h3>Cluster 2 - Above Average</h3>'
            f'<p>This data belongs to Cluster 2: Affluent Spenders</p>'
            f'<p>Customers in this cluster have the highest income level and represent the most financially robust segment. They are the highest spenders across all product categories and make frequent purchases. With a moderate number of customers, they are an exclusive group. Their spending on wine products is reflective of their luxurious lifestyle. They are comfortable with all types of purchasing methods, including web, catalog, and in-store purchases. This cluster consists of high-income individuals who are willing to indulge in premium products and services.</p></div>',
            unsafe_allow_html=True
        )

    elif clust == 3:
        st.markdown(
            f'<div style="border: 2px solid red; padding: 10px; border-radius: 5px;"><h3>Cluster 3 - Below Average</h3>'
            f'<p>This data belongs to Cluster 0: Frugal Professionals</p>'
            f'<p>Customers in this cluster represent the smallest segment with below-average numbers. They have a relatively high income level and are career-focused professionals. While they spend a significant amount on wine products, they are cautious spenders in other areas. They make a larger number of purchases through stores, possibly due to their busy lifestyles, but do not prefer catalog purchases. With moderate recency (time since last purchase), they tend to carefully consider their buying decisions. This cluster comprises middle-aged individuals who are financially responsible and prioritize quality over quantity.</p></div>',
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