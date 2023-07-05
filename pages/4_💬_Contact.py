import streamlit as st

st.title("Contact Us")

# Contact form inputs
name = st.text_input("Name")
email = st.text_input("Email")
message = st.text_area("Message")
submit = st.button("Submit")

# Validate and process form submission
if submit:
    if not name.strip() or not email.strip() or not message.strip():
        st.error("Please fill in all the required fields.")
    else:
        # Process the form submission (you can add your own logic here)
        st.success("Thank you for your message. We will get in touch with you soon.")
        # You can also send an email or store the form data in a database

# Contact information with emoji icons
st.header("Get to Know Me & Stay Connected")
st.markdown(
    """
    - 📺 YouTube: [KnowledgeHub](#)
    - 🌐 Website: [Customer Segmentation](#)
    - 💬 Discord: [Join our Community](#)
    - 💼 LinkedIn: [Connect with me](#)
    - 📸 Instagram: [Follow me](#)
    """
)