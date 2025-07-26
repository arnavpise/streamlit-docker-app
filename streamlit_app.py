import streamlit as st

st.title("🚀 My First Streamlit App")
st.subheader("Hello, Arnav! 👋")
st.write("This is a simple interactive app running inside Docker.")

# Add a slider
value = st.slider("Pick a number", 0, 100, 50)
st.write(f"You selected: {value}")

# Add a button
if st.button("Click me!"):
    st.success("You clicked the button! 🎉")
