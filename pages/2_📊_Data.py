import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import missingno as mn

st.title("Datasets")

@st.cache(allow_output_mutation=True)
def load_data():
    data = pd.read_csv("marketing_campaign.csv")  # Assuming your file is in CSV format
    return data

data = load_data()

# Display the table
st.write(data)


st.title("Exploratory Data Analysis")

# Exploratory Data Analysis (EDA)
data['Age'] = 2023 - data['Year_Birth']
data['Dt_Customer'] = pd.to_datetime(data['Dt_Customer'], format='%Y-%m-%d')
data['Years_customer'] = (pd.Timestamp('now').year) - (pd.to_datetime(data['Dt_Customer']).dt.year)
data['Total_Expenses'] = data['MntWines'] + data['MntFruits'] + data['MntMeatProducts'] + data['MntFishProducts'] + data['MntSweetProducts'] + data['MntGoldProds']
data['Total_Acc_Cmp'] = data['AcceptedCmp1'] + data['AcceptedCmp2'] + data['AcceptedCmp3'] + data['AcceptedCmp4'] + data['AcceptedCmp5'] + data['Response']

# Age and Income plots in one row
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6), facecolor='#FFFFFF')
data['Age'].value_counts().sort_index(ascending=False).plot(kind='barh', color='skyblue', ax=ax1)
ax1.set_title('Age')

sns.histplot(data=data, x='Income', binwidth=10000, kde=True, color='salmon', ax=ax2)
ax2.set_title('Income')

plt.tight_layout()
st.pyplot(fig)

# Education and Marital Status plots in one row
fig, (ax3, ax4) = plt.subplots(1, 2, figsize=(12, 6), facecolor='#FFFFFF')
sns.countplot(data=data, x='Education', saturation=1, alpha=0.9, palette='rocket', order=data['Education'].value_counts().index, ax=ax3)
ax3.set_title('Education')

sns.countplot(data=data, x='Marital_Status', saturation=1, alpha=0.9, palette='rocket', order=data['Marital_Status'].value_counts().index, ax=ax4)
ax4.set_title('Marital Status')

plt.tight_layout()
st.pyplot(fig)

# Kidhome and Teenhome plots in one row
fig, (ax5, ax6) = plt.subplots(1, 2, figsize=(12, 6), facecolor='#FFFFFF')
sns.countplot(data=data, x='Kidhome', saturation=1, alpha=0.9, palette='rocket', order=data['Kidhome'].value_counts().index, ax=ax5)
ax5.set_title('Kid Home')

sns.countplot(data=data, x='Teenhome', saturation=1, alpha=0.9, palette='rocket', order=data['Teenhome'].value_counts().index, ax=ax6)
ax6.set_title('Teen Home')

plt.tight_layout()
st.pyplot(fig)

# Expenses and Accepted Campaign plots in one row
fig, (ax7, ax8) = plt.subplots(1, 2, figsize=(12, 6), facecolor='#FFFFFF')
data[['MntWines', 'MntFruits', 'MntMeatProducts', 'MntFishProducts', 'MntSweetProducts', 'MntGoldProds']].sum().sort_values(ascending=True).plot(kind='barh', color='teal', ax=ax7)
ax7.set_title('Expenses')

data[['AcceptedCmp1', 'AcceptedCmp2', 'AcceptedCmp3', 'AcceptedCmp4', 'AcceptedCmp5', 'Response']].sum().sort_values(ascending=True).plot(kind='barh', color='purple', ax=ax8)
ax8.set_title('Accepted Campaign')

plt.tight_layout()
st.pyplot(fig)

# Total Expenses by Marital Status and Kid Home
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
ax1 = sns.barplot(data=data, x='Marital_Status', y='Total_Expenses', order=data.groupby('Marital_Status')['Total_Expenses'].sum().sort_values(ascending=False).index)
plt.xticks(rotation=360)
plt.title('Total Expenses by Marital Status', pad=10, fontsize=15, fontweight='semibold')
for p in ax1.patches:
    number = '{}'.format(p.get_height().astype('int64'))
    ax1.annotate(number, (p.get_x() + p.get_width() / 2., p.get_height()), ha='center', va='center', xytext=(0, 9), textcoords='offset points', color='black', fontsize=13)

plt.subplot(1, 2, 2)
ax2 = sns.barplot(data=data, x='Kidhome', y='Total_Expenses', order=data.groupby('Kidhome')['Total_Expenses'].sum().sort_values(ascending=False).index)
plt.xticks(rotation=360)
plt.title('Total Expenses by Kid Home', pad=10, fontsize=15, fontweight='semibold')
for p in ax2.patches:
    number = '{}'.format(p.get_height().astype('int64'))
    ax2.annotate(number, (p.get_x() + p.get_width() / 2., p.get_height()), ha='center', va='center', xytext=(0, 9), textcoords='offset points', color='black', fontsize=15)

plt.tight_layout()
st.pyplot(plt.gcf())

# Total Acc Campaign by Education and Marital Status
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
ax3 = sns.barplot(data=data, x='Education', y='Total_Acc_Cmp', order=data.groupby('Education')['Total_Acc_Cmp'].sum().sort_values(ascending=False).index)
plt.xticks(rotation=360)
plt.title('Total Acc Campaign by Education', pad=10, fontsize=15, fontweight='semibold')
for p in ax3.patches:
    number = '{}'.format(p.get_height().astype('int64'))
    ax3.annotate(number, (p.get_x() + p.get_width() / 2., p.get_height()), ha='center', va='center', xytext=(0, 9), textcoords='offset points', color='black', fontsize=15)

plt.subplot(1, 2, 2)
ax4 = sns.barplot(data=data, x='Marital_Status', y='Total_Acc_Cmp', order=data.groupby('Marital_Status')['Total_Acc_Cmp'].sum().sort_values(ascending=False).index)
plt.xticks(rotation=360)
plt.title('Total Acc Campaign by Marital Status', pad=10, fontsize=15, fontweight='semibold')
for p in ax4.patches:
    number = '{}'.format(p.get_height().astype('int64'))
    ax4.annotate(number, (p.get_x() + p.get_width() / 2., p.get_height()), ha='center', va='center', xytext=(0, 9), textcoords='offset points', color='black', fontsize=15)

plt.tight_layout()
st.pyplot(plt.gcf())

# Total Acc Campaign by Kid Home and Teen Home
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
ax5 = sns.barplot(data=data, x='Kidhome', y='Total_Acc_Cmp', order=data.groupby('Kidhome')['Total_Acc_Cmp'].sum().sort_values(ascending=False).index)
plt.xticks(rotation=360)
plt.title('Total Acc Campaign by Kid Home', pad=10, fontsize=15, fontweight='semibold')
for p in ax5.patches:
    number = '{}'.format(p.get_height().astype('int64'))
    ax5.annotate(number, (p.get_x() + p.get_width() / 2., p.get_height()), ha='center', va='center', xytext=(0, 9), textcoords='offset points', color='black', fontsize=15)

plt.subplot(1, 2, 2)
ax6 = sns.barplot(data=data, x='Teenhome', y='Total_Acc_Cmp', order=data.groupby('Teenhome')['Total_Acc_Cmp'].sum().sort_values(ascending=False).index)
plt.xticks(rotation=360)
plt.title('Total Acc Campaign by Teen Home', pad=10, fontsize=15, fontweight='semibold')
for p in ax6.patches:
    number = '{}'.format(p.get_height().astype('int64'))
    ax6.annotate(number, (p.get_x() + p.get_width() / 2., p.get_height()), ha='center', va='center', xytext=(0, 9), textcoords='offset points', color='black', fontsize=15)

plt.tight_layout()
st.pyplot(plt.gcf())

# Correlation Heatmap
plt.figure(figsize=(10, 8))
corr = data.corr()
sns.heatmap(corr, cmap='coolwarm', annot=True, fmt=".2f", linewidths=0.5)
plt.title('Correlation Heatmap', pad=10, fontsize=15, fontweight='semibold')
st.pyplot(plt.gcf())

# Missing Values Matrix
plt.figure(figsize=(8, 6))
mn.matrix(data, sparkline=False, fontsize=8, figsize=(8, 6))
plt.title('Missing Values Matrix', pad=10, fontsize=15, fontweight='semibold')
st.pyplot(plt.gcf())
