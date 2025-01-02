import pandas as pd

# Create a roadmap DataFrame
data = {
    "License": [
        "Commercial Registration (CR)",
        "Trademark Registration",
        "Marketing Campaign Licenses",
        "Media Advertising Permits",
        "Online Advertising Licenses",
        "Zakat & Tax Registration",
        "Social Insurance Registration",
        "Digital Compliance"
    ],
    "Dependency": [
        "None", "CR", "CR", "CR", "Marketing Campaign License",
        "CR", "Zakat Registration", "CR"
    ],
    "Estimated Time": [
        "1 business day", "1 - 2 months", "1 - 2 weeks", "1 week - 1 month",
        "1 week - 10 days", "1 - 2 weeks", "1 - 2 weeks", "1 week - 1 month"
    ],
    "Estimated Cost (SAR)": [
        "200 - 500", "500 - 5,000", "1,000 - 5,000", "3,000 - 10,000",
        "1,000 - 3,000", "1,000 - 3,000", "2,000 - 3,000", "3,000 - 7,000"
    ]
}
df = pd.DataFrame(data)

# Display the roadmap in Streamlit
st.header("Licensing Roadmap")
st.table(df)
