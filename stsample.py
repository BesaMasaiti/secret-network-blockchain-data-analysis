import streamlit as st
from extras import *
import plotly.express as px

st.title("Sample")
st.markdown("***Testing framework***")

# Query the DAU table
query_dau = """
   SELECT *
   FROM bachkaxyz.final_tables.daily_active_users
   LIMIT 1000
"""
# Convert the results to a DataFrame
daudf = get_data(query_dau)
# Visualization: Create a bar plot for Daily Active Users (DAU)
fig = px.scatter(daudf, x='day', y='users')
# Update the layout
fig.update_layout(
    width=800,  # Set the width of the plot
    height=600  # Set the height of the plot
)
dau = st.plotly_chart(fig, key="iris")

