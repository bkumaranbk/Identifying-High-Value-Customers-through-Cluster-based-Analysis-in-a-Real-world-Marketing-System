import streamlit as st

st.set_page_config(
    page_title="Customer Segmentation",
    page_icon="👋",
)

st.title("Identifying High-Value Customers through Cluster-based Analysis in a Real-world Marketing System")

st.markdown(
    """
   
    Marketing is very important for the growth and long-term success of any business. It can help build the market's brand, engage customers, grow revenue, provide a better customer experience & satisfaction, and increase sales. One of the key pain points for a marketing team is to know their customers and identify their needs. By understanding the customer, the team can launch a targeted marketing campaign that is tailored to specific needs. In addition, modern businesses face the challenge of identifying target customers in a marketplace where consumer preferences are constantly evolving. Most customer segmentation methods based on customer value fail to account for time and value changes. Today's business is based on new concepts because so many customers are unsure of what to buy. The market can't identify target customers. In this research, Machine learning algorithms detect hidden data patterns to make better decisions. Address Five popular clustering algorithms, those are K-Means, Affinity Propagation, DBSCAN, Hierarchical Clustering, and Fuzzy Clustering. These algorithms are utilized to cluster customer data from an iFood CRM Dataset. The optimal number of clusters is determined using the Davies-Bouldin and Silhouette score, which provides insights into the most suitable customer segments. By employing these methods, we aim to uncover customer behavioral patterns that can help shopping malls enhance their business operations and tailor their marketing strategies effectively. Our analysis of the iFood CRM Dataset revealed that the Hierarchical Clustering algorithm outperformed the other clustering algorithms in terms of identifying meaningful customer segments. The Silhouette and Davies-Bouldin scores were utilized to compare the performance of these algorithms. The recognized model allows businesses to gain a better understanding of their target audience and develop tailored marketing approaches. This study holds significant implications for marketing practitioners and businesses operating in a customer-driven environment. By implementing machine learning-based customer segmentation, companies can obtain actionable insights into customer preferences, facilitating personalized marketing campaigns and enhancing customer satisfaction.
    
    *Author: Kumaran B. (CT/2017/033)*
    """
)


st.sidebar.success("Select a page above.")


	
