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

# --- Configuration (optional) ---
st.set_page_config(
    page_title="Improvement Aspects Visualization",
    layout="wide" # Use wide layout for a large chart
)

st.header("Program Improvement Aspects", divider="red")

# --- Example Data Setup (REPLACE THIS with your actual DataFrame loading) ---
# Create dummy data for 'improvement_aspects_counts' DataFrame
data = {
    'Aspects for Improvement': [
        'Curriculum Content', 'Practical Workshops', 'Mentorship Quality',
        'Networking Opportunities', 'Resource Availability', 'Assessment Methods'
    ],
    'Count': [150, 120, 90, 80, 75, 60]
}
improvement_aspects_counts = pd.DataFrame(data)
# -------------------------------------------------------------------------

# Create the Plotly Bar Chart
fig = px.bar(
    improvement_aspects_counts,
    x='Aspects for Improvement',
    y='Count',
    title='Aspects of the Program that Could Be Improved',
    color='Aspects for Improvement' # Use color for visual distinction
)

# Apply rotation (Equivalent to plt.xticks(rotation=45, ...))
fig.update_xaxes(tickangle=45)

# Update layout to mimic tight_layout and large size (Plotly handles size dynamically)
fig.update_layout(
    xaxis_title='Aspects for Improvement',
    yaxis_title='Count',
    height=600, # Set a specific height
    margin={'t': 50, 'b': 100} # Adjust margins for the rotated labels
)

# Display the chart in Streamlit
st.plotly_chart(fig, use_container_width=True)

import streamlit as st
import pandas as pd
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go

# --- Streamlit Page Configuration ---
st.set_page_config(
    page_title="Faculty Data Visualization",
    layout="wide"
)

st.header("Arts Faculty Data Visualizations", divider="green")

# --- PLACEHOLDER DATA SETUP (REPLACE WITH YOUR ACTUAL DATA) ---

# 1. Data for Academic Year Distribution
data_academic_year = {
    'Bachelor Academic Year in EU': ['Year 1', 'Year 2', 'Year 3', 'Year 4', 'Year 1', 'Year 3']
}
arts_df = pd.DataFrame(data_academic_year)

# 2. Data for Program Distribution
data_programs = {
    'Arts Program': ['History', 'Literature', 'Philosophy', 'Visual Arts', 'History', 'Philosophy'],
    'Count': [180, 150, 120, 90, 180, 120] # Placeholder: Program counts are typically derived from value_counts
}
program_counts = pd.DataFrame(data_programs).groupby('Arts Program').size().reset_index(name='Count')
program_counts.columns = ['Arts Program', 'Count']


# 3. Data for Expectation Box Plots (Q3, Q4, Q5 on a scale, e.g., 1-5)
expectation_cols = ['Q3 - Expectation on Resources', 'Q4 - Expectation on Learning Environment', 'Q5 - Expectation Met']
data_expectation = {
    expectation_cols[0]: [1, 2, 3, 4, 5, 5, 4, 3, 2, 1, 3, 4, 5, 5, 4],
    expectation_cols[1]: [5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 5, 4, 3, 2, 1],
    expectation_cols[2]: [3, 3, 3, 4, 4, 3, 4, 4, 3, 3, 4, 4, 5, 5, 5]
}
expectation_df = pd.DataFrame(data_expectation)
# -------------------------------------------------------------------------


# --- 1. Distribution of Academic Years (Bar Chart) ---
st.subheader("Distribution of Academic Years")

academic_year_counts = arts_df['Bachelor Academic Year in EU'].value_counts().reset_index()
academic_year_counts.columns = ['Academic Year', 'Count']

# Create Plotly Bar Chart for Academic Years
fig_year = px.bar(
    academic_year_counts,
    x='Academic Year',
    y='Count',
    title='Distribution of Academic Years in Arts Faculty',
    labels={'Count': 'Number of Students'}
)
fig_year.update_layout(height=400) # Match approximate figure size

st.plotly_chart(fig_year, use_container_width=True)

st.divider()

# --- 2. Distribution of Arts Programs (Bar Chart) ---
st.subheader("Distribution of Arts Programs")

# Create Plotly Bar Chart for Arts Programs
fig_program = px.bar(
    program_counts,
    x='Arts Program',
    y='Count',
    title='Distribution of Arts Programs',
    labels={'Count': 'Number of Students'}
)

# Equivalent to plt.xticks(rotation=45, ha='right') and plt.tight_layout()
fig_program.update_xaxes(tickangle=45)
fig_program.update_layout(height=500, margin={'t': 50, 'b': 100}) # Adjust height/margin for rotated labels

st.plotly_chart(fig_program, use_container_width=True)

st.divider()

# --- 3. Expectation Box Plots (Subplots) ---
st.subheader("Expectation Comparisons (Box Plots)")

# Create Plotly Subplots (Equivalent to plt.subplot(1, 2, x))
fig_box = make_subplots(rows=1, cols=2, subplot_titles=(
    'Expectation on Resources vs. Expectation Met',
    'Expectation on Learning Environment vs. Expectation Met'
))

# 1. Box Plot for Resources (Q3 vs Q5)
box1 = go.Box(
    x=expectation_df[expectation_cols[0]],
    y=expectation_df[expectation_cols[2]],
    name='Resources',
    marker_color='blue'
)
fig_box.add_trace(box1, row=1, col=1)

# 2. Box Plot for Learning Environment (Q4 vs Q5)
box2 = go.Box(
    x=expectation_df[expectation_cols[1]],
    y=expectation_df[expectation_cols[2]],
    name='Learning Environment',
    marker_color='red'
)
fig_box.add_trace(box2, row=1, col=2)

# Update layout for titles and labels (Equivalent to plt.xlabel, plt.ylabel, plt.title)
fig_box.update_layout(
    height=600,
    showlegend=False,
    title_text='Expectation Box Plot Comparison'
)

# Set X and Y axis labels for the first subplot
fig_box.update_xaxes(title_text=f'{expectation_cols[0]} (Q3)', row=1, col=1)
fig_box.update_yaxes(title_text=f'{expectation_cols[2]} (Q5)', row=1, col=1)

# Set X and Y axis labels for the second subplot
fig_box.update_xaxes(title_text=f'{expectation_cols[1]} (Q4)', row=1, col=2)
fig_box.update_yaxes(title_text=f'{expectation_cols[2]} (Q5)', row=1, col=2)

# Display the figure
st.plotly_chart(fig_box, use_container_width=True)

import streamlit as st
import pandas as pd
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go

# --- Streamlit Page Configuration ---
st.set_page_config(
    page_title="Expectation Regression Analysis",
    layout="wide"
)

st.header("Expectation Regression Analysis", divider="orange")

# --- PLACEHOLDER DATA SETUP (REPLACE WITH YOUR ACTUAL DataFrame LOADING) ---
expectation_cols = [
    'Q3 [What was your expectation about the University as related to quality of resources?]',
    'Q4 [What was your expectation about the University as related to quality of learning environment?]',
    'Q5 [To what extent your expectation was met?]'
]
# Dummy data simulating survey scores (e.g., 1 to 5)
data = {
    expectation_cols[0]: [5, 4, 3, 2, 5, 4, 3, 5, 4, 3, 2, 1],
    expectation_cols[1]: [4, 5, 3, 4, 2, 5, 4, 3, 5, 4, 2, 1],
    expectation_cols[2]: [5, 4, 3, 2, 5, 4, 3, 4, 5, 3, 2, 1]
}
arts_df = pd.DataFrame(data)
# -------------------------------------------------------------------------

# Prepare the data (Equivalent to arts_df[expectation_cols].dropna())
expectation_df = arts_df[expectation_cols].dropna()

# --- Create Plotly Subplots for the Regression Plots ---

# Equivalent to plt.figure() and plt.subplot(1, 2, x)
fig = make_subplots(
    rows=1, 
    cols=2, 
    subplot_titles=(
        'Expectation on Resources vs. Expectation Met',
        'Expectation on Learning Environment vs. Expectation Met'
    )
)

# 1. Regression Plot for Resources (Q3 vs Q5) - Equivalent to sns.regplot
# Plotly Express's scatter with trendline handles the regression
fig_res = px.scatter(
    expectation_df,
    x=expectation_cols[0],
    y=expectation_cols[2],
    trendline="ols" # Ordinary Least Squares for regression line
)

# Add the scatter points and regression line to the first subplot
fig.add_trace(fig_res.data[0], row=1, col=1) # Scatter points
fig.add_trace(fig_res.data[1], row=1, col=1) # Trendline

# 2. Regression Plot for Learning Environment (Q4 vs Q5) - Equivalent to sns.regplot
fig_env = px.scatter(
    expectation_df,
    x=expectation_cols[1],
    y=expectation_cols[2],
    trendline="ols"
)

# Add the scatter points and regression line to the second subplot
fig.add_trace(fig_env.data[0], row=1, col=2) # Scatter points
fig.add_trace(fig_env.data[1], row=1, col=2) # Trendline

# --- Update Layout and Labels ---

# Set titles/labels for the first subplot
fig.update_xaxes(
    title_text='Expectation on Resources (Q3)', 
    row=1, 
    col=1
)
fig.update_yaxes(
    title_text='Expectation Met (Q5)', 
    row=1, 
    col=1
)

# Set titles/labels for the second subplot
fig.update_xaxes(
    title_text='Expectation on Learning Environment (Q4)', 
    row=1, 
    col=2
)
fig.update_yaxes(
    title_text='Expectation Met (Q5)', 
    row=1, 
    col=2
)

# Equivalent to plt.figure(figsize=(14, 6)) and plt.tight_layout()
fig.update_layout(
    height=600,
    showlegend=False,
    title_text="Regression Analysis: Expectations vs. Expectation Met"
)

# --- Display in Streamlit ---
# Equivalent to plt.show()
st.plotly_chart(fig, use_container_width=True)
