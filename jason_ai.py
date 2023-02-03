import streamlit as st
import cohere
from dotenv import load_dotenv
import os
load_dotenv()

#API key
co = cohere.Client('SOtiECjBHrLmJMpIeA9HyVlqhhSoNFLOdg5Tc1bp') 

# Initialization
if 'output' not in st.session_state:
    st.session_state['output'] = 'Output:'

# Function to generate the mobile details
def generate_mobile_details(input):
    if len(input) == 0:
        return None
    response = co.generate( 
        # We are using our custom Model that we trained on Cohere
    model='ac27b139-681e-490e-a66a-e6188b96bacf-ft',
    prompt=input, # take the input from the user
    max_tokens=300, 
    temperature=0.9, 
    k=0, 
    p=0.75, 
    frequency_penalty=0, 
    presence_penalty=0, 
    stop_sequences=["--"], 
    return_likelihoods='NONE') 
    
    st.session_state['output'] ='Mobile Details and Specification: {}'.format( response.generations[0].text)
    st.balloons()


st.title('AI Customer Care')
st.subheader('Jason AI')
st.write('''This is a simple **Streamlit** app that generates Mobile Model details''')

input = st.text_area('Enter your Mobile phone Name and model', height=100)
st.button('Generate Details', on_click = generate_mobile_details(input))
st.write(st.session_state.output)



# import cohere
# co = cohere.Client('NzNGw37GFezZIZcVa7P6vKPIUcDmiNfPS2mhhSPf') # This is your trial API key
# response = co.generate(
#   model='command-xlarge-20221108',
#   prompt='write a blog outline for a blog titled \"How Transformers made Large Language models possible\"',
#   max_tokens=300,
#   temperature=0.9,
#   k=0,
#   p=0.75,
#   frequency_penalty=0,
#   presence_penalty=0,
#   stop_sequences=[],
#   return_likelihoods='NONE')
# print('Prediction: {}'.format(response.generations[0].text))