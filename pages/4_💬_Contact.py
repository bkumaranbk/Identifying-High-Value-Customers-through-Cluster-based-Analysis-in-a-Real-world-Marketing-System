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
        # Generate mailto link
        mailto_link = f"mailto:bkumaran98@gmail.com?subject=New contact form submission&body={message}"

        # Display link to open user's default email client
        st.markdown(f"[Click here to send email](mailto:{email}?subject=New contact form submission&body={message})")
        st.success("Thank you for your message. We will get in touch with you soon.")

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
