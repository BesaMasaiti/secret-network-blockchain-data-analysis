import streamlit as st
import plotly.express as px
from extras import *

st.title("KPIs")
st.markdown("The **Daily Active Users** (DAU) metric provides insight into the engagement level of users on the Secret Network. By tracking the number of unique users who interact with the platform each day, we can assess user retention, activity trends, and the overall health of the network. An increasing DAU indicates growing interest and utilization, reflecting the effectiveness of our outreach efforts and community initiatives. Conversely, a decline in DAU may prompt further investigation into potential barriers to user engagement or the need for additional features that meet user needs.")
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

st.markdown("The analysis of the **top 100 popular smart contracts** reveals the most utilized applications on the Secret Network. These contracts serve as a testament to the ecosystem's vibrancy and the preferences of our user base. By understanding which contracts are receiving the most activity, we can identify emerging trends, popular use cases, and areas for potential development. This information can also guide marketing strategies and collaborations, as highlighting successful projects may encourage further participation from both developers and users.")
# Query the top100pop table
query_top100pop = """
   SELECT *
   FROM bachkaxyz.final_tables.top_100pop_smartcontracts
   LIMIT 1000
"""
# Convert the results to a DataFrame
top100popdf = get_data(query_top100pop)
# Visualization: Create a bar plot for top100 pop
fig = px.bar(top100popdf, x='smartcontract', y='totaltransactions')
# Update the layout
fig.update_layout(
    width=800,  # Set the width of the plot
    height=600  # Set the height of the plot
)
top100pop = st.plotly_chart(fig)

st.markdown("Monitoring **gas usage on a daily basis** is crucial for assessing network performance and efficiency. Gas is a measure of the computational effort required to execute operations on the blockchain, and tracking this metric allows us to evaluate the demand on our network. A high level of gas usage may indicate significant activity and interest in the ecosystem, but it also raises questions about transaction costs and scalability. By analyzing gas usage trends, we can make informed decisions about optimizations and enhancements to improve user experience while maintaining a robust infrastructure.")
# Query the daily gas used per day table
query_gasused = """
   SELECT *
   FROM bachkaxyz.final_tables.total_gasused_perday
   LIMIT 1000
"""
# Convert the results to a DataFrame
daygasuseddf = get_data(query_gasused)
# Visualization: Create a bar plot for total gas used per day
fig = px.scatter(daygasuseddf , x='day', y='total_gas_used_per_day')
# Update the layout
fig.update_layout(
    width=800,  # Set the width of the plot
    height=600  # Set the height of the plot
)
daygasused = st.plotly_chart(fig)





st.markdown("The **cumulative new wallets per day** metric tracks the growth of the Secret Network by showing the total number of new wallets created over time. This metric is a key indicator of adoption, revealing how quickly users are joining the network. It highlights organic growth and can help gauge the success of initiatives aimed at bringing more users to the blockchain ecosystem.")
# Query the cumulative new wallets per day table
query_cumnew = """
   SELECT *
   FROM bachkaxyz.final_tables.cumulative_newwallets_per_day
   LIMIT 1000
"""
# Convert the results to a DataFrame
cumnewwalldf = get_data(query_cumnew)
# Visualization: Create a bar plot for cumulative new wallets per day
fig = px.area(cumnewwalldf, x='first_appearance_date', y='cumulative_new_wallets')
# Update the layout
fig.update_layout(
    width=800,  # Set the width of the plot
    height=600  # Set the height of the plot
)
cumnew = st.plotly_chart(fig)


st.markdown("Tracking the number of **new wallets created each day** offers granular insights into the daily onboarding rate of new users to the Secret Network. Spikes or drops in this metric may correlate with significant events, such as protocol updates, dApp launches, or external market conditions.This data is crucial for understanding short-term adoption trends.")
# Query the new wallets per day table
query_newwall = """
   SELECT *
   FROM bachkaxyz.final_tables.new_wallets_per_day
   LIMIT 1000
"""
# Convert the results to a DataFrame
newwallddf = get_data(query_newwall)
# Visualization: Create a bar plot for new wallets per day
fig = px.bar(newwallddf, x='first_appearance_day', y='new_wallets')
# Update the layout
fig.update_layout(
    width=800,  # Set the width of the plot
    height=600  # Set the height of the plot
)
newwall = st.plotly_chart(fig)





st.markdown("This metric tracks the **total number of transactions processed by the Secret Network each day**. It’s a key indicator of overall network activity and user engagement. By examining daily transaction counts, we can identify trends, peak usage times, and the impact of specific events like new dApp releases or network upgrades.")
# Query the transactions per day table
query_txpday = """
   SELECT *
   FROM bachkaxyz.final_tables.transactions_per_day
   LIMIT 1000
"""
# Convert the results to a DataFrame
txpdaydf = get_data(query_txpday)
# Visualization: Create a bar plot for transactions per day
fig = px.line(txpdaydf, x='day', y='transactions_per_day')
# Update the layout
fig.update_layout(
    width=800,  # Set the width of the plot
    height=600  # Set the height of the plot
)
txpday = st.plotly_chart(fig)


st.markdown("The **total transactions** metric captures the cumulative number of transactions executed on the Secret Network. This long-term metric reflects the network’s overall growth and user activity since its inception. It is an essential indicator of the network’s utilization and adoption over time, showcasing the broader scale of user participation and interaction.")
# Query the total transactions table
query_tottx = """
   SELECT *
   FROM bachkaxyz.final_tables.total_transactions
   LIMIT 1000
"""
# Convert the results to a DataFrame
tottxdf = get_data(query_tottx)
st.write(tottxdf)

