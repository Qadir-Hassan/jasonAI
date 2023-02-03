import streamlit as st
from PIL import Image



#Main Content Goes Here
st.set_page_config(
    page_title="JASON AI",
    page_icon="👋",
)

st.sidebar.success("Select a Page To veiw.")
st.caption("Replacing Customer Service with AI ")
st.header('JASON AI 💙')



st.subheader("Our Idea")
st.write("")






st.subheader('This is the architecture design on a potential conversation flow')
image3 = Image.open('images/flowchart.jpg')
st.image(image3, caption='caption')
