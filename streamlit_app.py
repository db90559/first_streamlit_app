import streamlit

streamlit.title('My Parents new healty Diner')

streamlit.header('Breakfast Favourites')
streamlit.text(' 🥣 Omega 3 & Bluberry Oatmeal')
streamlit.text(' 🥗 Kale, Spinach and Rocket Smoothie')
streamlit.text(' 🐔 HARD-Boiled Free Range Egg')
streamlit.text(' 🥑🍞 Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
