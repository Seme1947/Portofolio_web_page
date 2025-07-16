import streamlit as st
import csv

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

content2 = """
    Here you will see my projects. Thank you for watching.
    """
st.write(content2)

col3,col_empty,col4 = st.columns([1.5,0.5,1.5])

with col3:
    with open("data.csv", 'r') as file:
        data = list(csv.reader(file))

    apps = []

    for dat in data[1:]:
        apps.append(dat[0].split(';'))

    for i in range(0,len(apps),2):
        st.write(apps[i][0])
        st.info(apps[i][1])
        st.image(f'images/images/{i + 1}.png')
        st.write(f"[Source Code]({apps[i][2]})")
with col4:
    for i in range(1, len(apps),2):
        st.write(apps[i][0])
        st.info(apps[i][1])
        st.image(f'images/images/{i + 1}.png')
        st.write("[Source Code](https://pythonhow.com)")