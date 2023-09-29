import streamlit as st

def hide_menu():
    hide_css = """
        <style>
        #MainMenu {visibility: hidden;}
        </style>
        """
    st.markdown(hide_css, unsafe_allow_html=True)

# Configure page title and icon
st.set_page_config(
    page_title="Customer Segmentation",
    page_icon="🏡",
)

# Call the hide_menu() function here
hide_menu()

# Your Streamlit app code goes here


st.title("Identifying High-Value Customers through Cluster-based Analysis in a Real-world Marketing System")

st.markdown(
    """
    In today’s business world, marketing is super important. It helps companies build their brand, connect with customers, make more money, keep customers happy, and sell more stuff. But here’s the thing: to do marketing right, you need to know their customers really well and figure out what they want. Sometimes, though, it’s tough for businesses to find the right customers to target. That’s where this study comes in. 
    
    This study applied a hybrid approach that combined unsupervised machine learning with supervised learning to address this issue. In this study, five popular clustering algorithms, K- Means, Affinity Propagation, DBSCAN, BRICH, and Gaussian Mixture Model are made sure to be utilized to segment customer data. The optimal number of clusters is determined using the following Davies-Boulding, and Silhouette scores, which provide insights into the most suitable customer segments to identify potential customer sets. This analysis revealed that the K-Means algorithm topped the other clustering algorithms in identifying meaningful customer segments. Furthermore, the study evaluates model accuracy through the training and testing of Decision Tree Classifier, Support Vector Machine, and Random Forest Classifier. Notably, the Random Forest Classifier promises an accuracy of 94%. The recognized model allows businesses to understand their target audience better and develop tailored marketing approaches. 
    
    This study holds important implications for businesses that operate in a customer-focused environment. Thus, it can help marketers create personalized marketing strategies and increase customer satisfaction and productivity. 

    Index Terms—Segmentation, Cluster-based Analysis, Unsupervised Machine Learning

    
    *Author: Kumaran B. (CT/2017/033)*  
    *Faculty: Faculty of Computing Technology, University of Kelaniya*  
    *Degree: Bachelor of Information and Communication Technology*
    """
)

st.sidebar.success("Select a page above.")
