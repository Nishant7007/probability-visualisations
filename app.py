import streamlit as st
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import random

# Function to generate n random numbers
def generate_random_numbers(n, start, end):
    return [random.randint(start, end) for _ in range(n)]

# Streamlit app
st.title("Random Number Generator and Dynamic Distribution Plot")

# Input section
st.sidebar.header("Input Parameters")
n = st.sidebar.slider("Select number of random numbers (n)", 1, 100, 10)
start_range = st.sidebar.number_input("Start of range", value=0)
end_range = st.sidebar.number_input("End of range", value=100)

# Button to generate random numbers
if st.button("Generate Random Numbers"):
    if start_range >= end_range:
        st.error("Start range must be less than the end range.")
    else:
        random_numbers = generate_random_numbers(n, start_range, end_range)
        
        # Display the random numbers
        st.write(f"Generated {n} random numbers from {start_range} to {end_range}:")
        st.write(random_numbers)
        
        # Plot the distribution with KDE
        fig, ax = plt.subplots()
        sns.histplot(random_numbers, kde=True, ax=ax)
        ax.set_title(f"Distribution of {n} Random Numbers")
        st.pyplot(fig)
