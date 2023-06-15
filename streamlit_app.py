import streamlit

streamlit.title('My Moms New Healthy Diner')
streamlit.header('Breakfast Favourites')
streamlit.text('1. Omega 3 & Bleuberry Oatmeal')
streamlit.text('2. Kale, Spinach and Rocket Smoothie')
streamlit.text('3. Hard-Boiled Free Range Eggs')
streamlit.text('4. Avocado Toast')
streamlit.header('Build Your Own Fruit Smoothie')

import pandas

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

# Display the table on the page.
streamlit.dataframe(my_fruit_list)
