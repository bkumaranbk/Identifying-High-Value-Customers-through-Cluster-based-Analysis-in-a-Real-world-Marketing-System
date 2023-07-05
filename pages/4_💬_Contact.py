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
        #st.markdown(f"[Click here to send email](mailto:{email}?subject=New contact form submission&body={message})")
        st.success("Thank you for your message. We will get in touch with you soon.")

# Contact information with emoji icons
st.header("Get to Know Me & Stay Connected")
st.markdown(
    """
    - 🌐 Website: [Customer Segmentation](https://identifying-high-value-customers-through-cluster-based-analysis.streamlit.app/)
    - 💬 Discord: [Join our Community](https://discord.gg/MAqKaCUz)
    - 💼 LinkedIn: [Connect with me](https://www.linkedin.com/in/balachandran-kumaran-4363361a8/)
    - 📸 Instagram: [Follow me](https://www.instagram.com/kumaran_bk/)
    """
)
