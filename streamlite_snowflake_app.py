import streamlit
import pandas
streamlit.title ('Streamlit and Snowflake app')
streamlit.header ('Snowflake Course')
streamlit.text('Data applcation builders application')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avacado','Strawberries'])
streamlit.dataframe(my_fruit_list)
