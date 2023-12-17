import langhcain_name_gen as lh 
import streamlit as st 

st.title("🐶 Pet Name generator")

animal_type = st.sidebar.selectbox("What is your pet name",("cat","dog","rabbit",("hen"),("duck")))

animal_color = st.sidebar.text_area(label=f"What color is your {animal_type}",max_chars=15)

with st.sidebar:
    openai_api_key = st.text_input("OpenAI API Key", key="langchain_search_api_key_openai", type="password")
    "[Get an OpenAI API key](https://platform.openai.com/account/api-keys)"

if animal_color:
    if not openai_api_key:
      st.info("Please add your OpenAI API key to continue.")
      st.stop()
    response  = lh.pet_name_gen(animal_type,animal_color,openai_api_key)
    st.write(response['text'])

