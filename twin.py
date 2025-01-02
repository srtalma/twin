# -*- coding: utf-8 -*-
"""twin.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1_FqG8FIhQDwEn9mPhaApb8RkwkWAktIL
"""

import streamlit as st
import pandas as pd

# App Title
st.title("Digital Twin for Marketing Companies")
st.subheader("Manage your licenses, costs, and compliance with ease!")

# Input Section
st.sidebar.header("Company Information")
company_name = st.sidebar.text_input("Company Name", "شركة تسويق")
activity = st.sidebar.selectbox(
    "Company Activity",
    ["Social Media Marketing", "Advertising Campaigns", "Online Promotions"],
)
location = st.sidebar.text_input("Location", "Riyadh")

# Input Licenses
st.sidebar.header("Required Licenses")
licenses = {
    "Commercial Registration (CR)": {"time": "1 business day", "cost": "200 - 500 SAR"},
    "Trademark Registration": {"time": "1 - 2 months", "cost": "500 - 5,000 SAR"},
    "Marketing Campaign Licenses": {"time": "1 - 2 weeks", "cost": "1,000 - 5,000 SAR"},
    "Media Advertising Permits": {"time": "1 week - 1 month", "cost": "3,000 - 10,000 SAR"},
    "Online Ad Licenses": {"time": "1 week - 10 days", "cost": "1,000 - 3,000 SAR"},
    "Zakat & Tax Registration": {"time": "1 - 2 weeks", "cost": "1,000 - 3,000 SAR"},
    "Social Insurance Registration": {"time": "1 - 2 weeks", "cost": "2,000 - 3,000 SAR"},
    "Digital Compliance": {"time": "1 week - 1 month", "cost": "3,000 - 7,000 SAR"},
}

selected_licenses = st.sidebar.multiselect("Select Licenses", options=list(licenses.keys()))

# Calculate Estimated Costs and Time
total_cost = 0
total_time = []
if selected_licenses:
    st.header("Estimated Costs and Time")
    for license in selected_licenses:
        st.write(f"**{license}**")
        st.write(f"- Time: {licenses[license]['time']}")
        st.write(f"- Cost: {licenses[license]['cost']}")
        cost_range = licenses[license]['cost'].split("-")
        total_cost += int(cost_range[1].split()[0])  # Taking the max of cost range
        total_time.append(licenses[license]["time"])

    st.subheader(f"Total Estimated Cost: {total_cost} SAR")
    st.subheader(f"Estimated Time: {', '.join(total_time)}")

# Compliance Check
st.header("Compliance Check")
compliance = st.checkbox("Check for Data Protection Compliance")
if compliance:
    st.success("Compliance with digital and data protection laws is required.")
else:
    st.warning("Missing compliance! Ensure digital systems follow data protection rules.")

# Recommendations Section
st.header("AI Recommendations")
if st.button("Generate Recommendations"):
    st.write(
        "💡 Use local influencers to reduce costs for online campaigns and achieve higher engagement rates."
    )
    st.write("💡 Streamline ad approvals by preparing required documents in advance.")

# Notifications Section
st.header("Upcoming Deadlines and Alerts")
st.write("📅 No upcoming deadlines. You're all set!")

# Real-time Updates
st.header("Integration with Government Portals")
st.write(
    "Get real-time updates by linking with governmental APIs such as ZATCA and وزارة التجارة."
)