import streamlit as st
from PIL import Image

st.title("TDS Week 8 Graded Assignment: Web app for addition of two numbers")

st.subheader("-by HINDESH AKASH (21f1006192)")

img = Image.open("Add.png")
st.image(img,clamp=True)

#input
num1 = st.number_input("Enter first number: ")
num2 = st.number_input("Enter second number: ")

results = num1 + num2

st.success(f"The sum of above numbers is: {results}")



