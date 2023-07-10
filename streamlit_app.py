
import streamlit
import pandas

streamlit.title('My parent healthy diner')

streamlit.header('😊😊😊😊Breakfast menu')
streamlit.text('Omega 3 & Blueberry oatmeal')
streamlit.text('Kale , Spinash & Rocket smoothie')
streamlit.text('Hard Boiled Free range egg')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
