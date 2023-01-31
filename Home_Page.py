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

st.info("This page contains static information about our bot. We have included a few examples below to highlight interesting capabilities. Hope you enjoy!")
st.info("For the live demo, please click on the second sidebar tab to the left. (If you are on a mobile device, please click on the hamburger menu in the top left corner.")
st.info("If you would like to skip to the workflow, feel free to scroll to the end.")

st.subheader("Our Idea")
st.write("")
st.write("Idea descriptipon goes here")

st.subheader("Examples")
st.write("Due to limited demo time, we thought of including sample conversations our team has had with Health-E for listeners to be able to appreciate all the features of our bot. We have included a few examples below.")

st.markdown("In hospitals paperwork takes alot of time from the patients and doctors. Health-e eliminate the managerial paperwork and make things smoother for the patients. Our bot helps the user finding best solutions for their problem with just one line prompts.")
image1 = Image.open('images/ncai.png')
st.image(image1, caption='caption')


st.markdown("The following conversation showcases two interesting features of Health-E. First, it recognizes that no cause has been provided and responds accordingly with a general suggestion. Second, Health-e has a one message memory; which allows the user to correct itself if needed.")
st.markdown("Additionally, it highlights a few current limitations. For instance, logic suggests that the urgency of a coffee burn should be much lower compared to a torch burn. In the short term, this can be overcome via prompt engineering and further fine-tuning. Moreover, the one message memory limits the length of a conversation significantly. In part, this was done by design to encourage fast processing. Assuming that the bot will be used primarily to process appointments and not as a counselor, which would require longer memory, this is a reasonable trade-off.")
image2 = Image.open('images/ncai.png')
st.image(image2, caption='caption')

st.write("")

st.markdown("Explanation of what this convo showcases.")
image3 = Image.open('images/image2.png')
st.image(image3, caption='caption')



st.subheader('This is the architecture design on a potential conversation flow')
image3 = Image.open('images/image2.png')
st.image(image3, caption='caption')
