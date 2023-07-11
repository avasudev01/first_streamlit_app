
import streamlit
import pandas

streamlit.title('My parent healthy diner')

streamlit.header('😊😊😊😊Breakfast menu')
streamlit.text('Omega 3 & Blueberry oatmeal')
streamlit.text('Kale , Spinash & Rocket smoothie')
streamlit.text('Hard Boiled Free range egg')

streamlit.text('🍊🍊🍋🍋🍍🍍Build your own smoothie 🍉🍉🥭🥭')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')



# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display the table on the page.

streamlit.dataframe(fruits_to_show)

import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response)
