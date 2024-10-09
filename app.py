import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import random
import time

# Function to generate sum of two random numbers from the range
def generate_sum_of_two_numbers_dynamic(n, start, end):
    for _ in range(n):
        num1 = random.randint(start, end)
        num2 = random.randint(start, end)
        yield num1 + num2

# Streamlit app
st.title("Dynamic Sum of Two Random Numbers and Distribution Plot")

# Input section
st.sidebar.header("Input Parameters")
n = st.sidebar.slider("Select number of random sums (n)", 1, 1000, 10)
start_range = st.sidebar.number_input("Start of range", value=0)
end_range = st.sidebar.number_input("End of range", value=1000)

# Placeholder for the plot
plot_placeholder = st.empty()

# Button to generate random sums dynamically
if st.button("Generate Random Sums"):
    if start_range >= end_range:
        st.error("Start range must be less than the end range.")
    else:
        random_sums = []
        
        # Dynamically generate sums and update the plot
        for sum_of_two in generate_sum_of_two_numbers_dynamic(n, start_range, end_range):
            random_sums.append(sum_of_two)
            
            # Plot the distribution with KDE
            fig, ax = plt.subplots()
            sns.histplot(random_sums, kde=True, ax=ax)
            ax.set_title(f"Dynamic Distribution of Sum of Two Random Numbers ({len(random_sums)} values)")
            
            # Update the plot dynamically
            plot_placeholder.pyplot(fig)
            
            # Slow down the update for visualization purposes
            time.sleep(0.1)
