import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Scientific Visualization"  # Changed page title
)

st.header("Scientific Visualization", divider="gray") # Changed header text

# --- Configuration (optional, but good practice) ---
st.set_page_config(
    page_title="Gender Distribution Visualization",
    layout="centered"
)

st.header("Gender Distribution in Arts Faculty", divider="blue")

# --- Example Data Setup (Replace with your actual DataFrame loading) ---
# Since you didn't provide 'arts_df', I'll create a dummy one for the code to run.
data = {
    'Gender': ['Female', 'Male', 'Female', 'Non-binary', 'Male', 'Female', 'Male', 'Female', 'Female', 'Male']
}
arts_df = pd.DataFrame(data)
# ----------------------------------------------------------------------


# 1. Bar Chart (using Plotly Express)
st.subheader("Gender Distribution - Bar Chart")

# Calculate counts for the bar chart
gender_counts_bar = arts_df['Gender'].value_counts().reset_index()
gender_counts_bar.columns = ['Gender', 'Count']

# Create the Plotly Bar Chart
fig_bar = px.bar(
    gender_counts_bar,
    x='Gender',
    y='Count',
    title='Distribution of Gender in Arts Faculty (Bar Chart)',
    color='Gender',
    labels={'Gender': 'Gender Category', 'Count': 'Number of Students'}
)

# Display the chart in Streamlit
st.plotly_chart(fig_bar, use_container_width=True)

# -------------------------------------------------------------

# 2. Pie Chart (using Plotly Express)
st.subheader("Gender Distribution - Pie Chart")

# Calculate counts for the pie chart
gender_counts_pie = arts_df['Gender'].value_counts().reset_index()
gender_counts_pie.columns = ['Gender', 'Count']

# Create the Plotly Pie Chart
fig_pie = px.pie(
    gender_counts_pie,
    names='Gender',
    values='Count',
    title='Distribution of Gender in Arts Faculty (Pie Chart)',
    hole=.3 # Optional: creates a donut chart
)

# Display the chart in Streamlit
st.plotly_chart(fig_pie, use_container_width=True)
