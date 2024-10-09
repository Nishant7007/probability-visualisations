import streamlit as st
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import random
import time

# Function to generate random numbers one by one
def generate_random_numbers_dynamic(n, start, end):
    for _ in range(n):
        yield random.randint(start, end)

# Streamlit app
st.title("Dynamic Random Number Generator and Distribution Plot")

# Input section
st.sidebar.header("Input Parameters")
n = st.sidebar.slider("Select number of random numbers (n)", 1, 1000, 10)
start_range = st.sidebar.number_input("Start of range", value=0)
end_range = st.sidebar.number_input("End of range", value=1000)

# Placeholder for the plot
plot_placeholder = st.empty()

# Button to generate random numbers dynamically
if st.button("Generate Random Numbers"):
    if start_range >= end_range:
        st.error("Start range must be less than the end range.")
    else:
        random_numbers = []
        
        # Dynamically generate and plot the numbers
        for number in generate_random_numbers_dynamic(n, start_range, end_range):
            random_numbers.append(number)
            
            # Plot the distribution with KDE
            fig, ax = plt.subplots()
            sns.histplot(random_numbers, kde=True, ax=ax)
            ax.set_title(f"Dynamic Distribution of {len(random_numbers)} Random Numbers")
            
            # Update the plot dynamically
            plot_placeholder.pyplot(fig)
            
            # Slow down the update so you can visually see the dynamic effect
            time.sleep(0.1)
