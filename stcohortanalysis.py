import streamlit as st
from dateutil import relativedelta
import plotly.graph_objects as go
from extras import *


st.title("Cohort Analysis")
st.markdown("Cohort analysis for the Secret Network involves tracking and analyzing groups of users who interact with decentralized applications (dApps) over time. This method helps us understand user retention, engagement, and overall behavior, allowing developers and stakeholders to identify patterns and trends within the user base. By segmenting users based on their initial interactions, we can assess the effectiveness of various features and improvements, ultimately enhancing user experience and fostering community growth within the privacy-focused ecosystem of the Secret Network.")
# Query the Cohort Analysis table
query_cohortanalysis = """
   SELECT *
   FROM bachkaxyz.final_tables.cohort_analysis
   LIMIT 1000
"""
# Convert the results to a DataFrame
cohortanalysisdf = get_data(query_cohortanalysis)

# Calculate the difference in months between active_month and cohort_month
def calculate_months_difference(start_date, end_date):
    delta = relativedelta.relativedelta(end_date, start_date)
    return delta.months + (delta.years * 12)
cohortanalysisdf['cohort'] = cohortanalysisdf.apply(
    lambda row: calculate_months_difference(row['cohort_month'], row['active_month']),
    axis=1
)

cohortanalysisdf['total_users'] = cohortanalysisdf['total_users'].astype(float)
# Pivot the data to create a cohort table with percentages
cohort_table = cohortanalysisdf.pivot(index='cohort_month', columns='cohort', values='total_users')
# Visualization: Heatmap representation
fig = go.Figure(data=go.Heatmap(
    z=cohort_table.values,  # The values you want to display
    x=cohort_table.columns,  # Labels for the x-axis (e.g., months or time periods)
    y=cohort_table.index,    # Labels for the y-axis (e.g., cohort groups)
    colorscale='viridis',      # Similar to Seaborn's 'crest' colormap
    hoverongaps=False,       # Disable hover if there are gaps
    text=cohort_table.values,
    hoverinfo="text"         # Show the values on hover
))
# Update the layout for title, size, etc.
fig.update_layout(
    title="Secret Cohort Analysis",
    xaxis_title="Active Month",
    yaxis_title="Cohort Month",
    width=800,
    height=600
)
# Display the heatmap in Streamlit
st.plotly_chart(fig)


st.markdown("The cohort analysis specific to the Shade DApp within the Secret Network provides valuable insights into user behavior and interactions with the platform's privacy-preserving functionalities. By examining different user cohorts based on their activity with Shade, we can evaluate the adoption of its unique offerings, such as secure asset management and privacy-enhanced financial tools. This analysis allows us to monitor user retention rates and identify key factors influencing user satisfaction, guiding future enhancements and marketing strategies to attract and retain users in this innovative DeFi space.")
# Query the Shade Dapp Cohort Analysis table
query_shade = """
   SELECT *
   FROM bachkaxyz.final_tables.shade_cohort_analysis
   LIMIT 1000
"""
# Convert the results to a DataFrame
shadecohortanalysisdf = get_data(query_shade)
# Calculate the difference in months between active_month and cohort_month
def calculate_months_difference(start_date, end_date):
    delta = relativedelta.relativedelta(end_date, start_date)
    return delta.months + (delta.years * 12)
shadecohortanalysisdf['cohort'] = shadecohortanalysisdf.apply(
    lambda row: calculate_months_difference(row['cohort_month'], row['active_month']),
    axis=1
)
shadecohortanalysisdf['total_users'] = shadecohortanalysisdf['total_users'].astype(float)
# Pivot the data to create a shade dapp cohort table with percentages
cohort_table = shadecohortanalysisdf.pivot(index='cohort_month', columns='cohort', values='total_users')
# Visualization: Heatmap representation
fig2 = go.Figure(data=go.Heatmap(
    z=cohort_table.values,  # The values you want to display
    x=cohort_table.columns,  # Labels for the x-axis (e.g., months or time periods)
    y=cohort_table.index,    # Labels for the y-axis (e.g., cohort groups)
    colorscale='viridis',      # Similar to Seaborn's 'crest' colormap
    hoverongaps=False,       # Disable hover if there are gaps
    text=cohort_table.values,
    hoverinfo="text"         # Show the values on hover
))
# Update the layout for title, size, etc.
fig2.update_layout(
    title="Shade Dapp Cohort Analysis",
    xaxis_title="Active Month",
    yaxis_title="Cohort Month",
    width=800,
    height=600
)
# Display the heatmap in Streamlit
st.plotly_chart(fig2)