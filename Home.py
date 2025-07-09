import streamlit as st

st.set_page_config(layout = 'wide')

col1,col2 = st.columns(2)

with col1:
    st.image("images/images/photo.png")

with col2:
    st.title('Mihai Seme')
    content = """
    Hi, my name is Mihai Seme and this is not a photo with me.
    It is all I got.
    Thank you.
    """
    st.info(content)