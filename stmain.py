import streamlit as st
import markdown as markdown

st.set_page_config(
    page_title = "Welcome"
)
st.title("Home Page")
st.sidebar.success("Select a page")
st.markdown("Welcome to our analytics hub dedicated to the Secret Network https://scrt.network/ , where we harness data to unlock insights and drive innovation in the blockchain space. Our mission is to provide comprehensive analytics that enhance understanding of user behavior and application performance.")
st.markdown("At the forefront of our efforts, we focus on key metrics such as Daily Active Users (DAU), popular smart contracts, and gas usage, allowing us to paint a detailed picture of the ecosystem.By leveraging advanced data analysis techniques, we aim to identify trends, uncover opportunities, and empower decision-making for developers, users, and stakeholders within the Secret Network.") 
st.markdown("As the blockchain landscape evolves, we are committed to providing actionable insights that support the ongoing development and adoption of privacy-centric technologies through data-driven analysis.")

