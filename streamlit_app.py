
import streamlit
import pandas
import requests
import snowflake.connector 
from urllib.error import URLError


streamlit.title('My parent healthy diner')

streamlit.header('😊😊😊😊Breakfast menu')
streamlit.text('Omega 3 & Blueberry oatmeal')
streamlit.text('Kale , Spinash & Rocket smoothie')
streamlit.text('Hard Boiled Free range egg')

streamlit.text('🍊🍊🍋🍋🍍🍍Build your own smoothie 🍉🍉🥭🥭')

#import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')



# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display the table on the page.

streamlit.dataframe(fruits_to_show)

#create the repeatablle codeblock(called function)
def get_fruitvice_data(this_fruit_choice):
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
    fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
    return (fruityvice_normalized)

streamlit.header("Fruityvice Fruit Advice!")
#import requests

try:
   fruit_choice = streamlit.text_input('What fruit would you like information about?')
   if not fruit_choice:
       streamlit.error("Please select a fruit to get information.")
   else:
       #fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
       #streamlit.text(fruityvice_response.json())
       #streamlit.write('The user entered ', fruit_choice)
       # write your own comment -what does the next line do? 
       #fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
       # write your own comment - what does this do?
       back_from_function = get_fruityvice_date(fruit_choice)
       streamlit.dataframe(back_from_function)

except URLError as e:
   streamlit.error()

streamlit.stop()

#import snowflake.connector
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * from fruit_load_list")
my_data_rows = my_cur.fetchall()
streamlit.header("The fruit load contains")
streamlit.dataframe(my_data_rows)

add_my_fruit = streamlit.text_input('What fruit would you like me to add','Jackfruit')
streamlit.write('Thanks for adding ', add_my_fruit)

my_cur.execute("insert into fruit_load_list values ('from streamlit')")
