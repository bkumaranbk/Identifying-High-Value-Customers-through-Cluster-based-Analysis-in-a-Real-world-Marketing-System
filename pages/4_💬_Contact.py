import streamlit as st
import smtplib
from email.message import EmailMessage

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
        # Send email
        msg = EmailMessage()
        msg.set_content(message)  # Set the message content to the user's input

        msg['Subject'] = 'New contact form submission'
        msg['From'] = email  # Set the 'From' field to the user's email address
        msg['To'] = 'bkumaran98@gmail.com'

        try:
            # Replace 'smtp.example.com' with your SMTP server address
            with smtplib.SMTP('smtp.example.com', 587) as smtp:
                smtp.ehlo()
                smtp.starttls()
                # Replace 'your_email@example.com' and 'your_password' with your email credentials
                smtp.login('your_email@example.com', 'your_password')
                smtp.send_message(msg)
            st.success("Thank you for your message. We will get in touch with you soon.")
        except Exception as e:
            st.error(f"An error occurred while sending the email: {e}")

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
