import streamlit as st 

from scraper import get_bill 
from parser import parse_bill

st.set_page_config(
    page_title="FESCO Bill Analyzer",
    page_icon="💡",
)

st.title("💡 FESCO Bill Analyzer")

st.write(
    "Enter your FESCO bill reference number below to analyze your electricity bill."
)

ref_no = st.text_input(
    "Reference Number",
    placeholder="Enter 14 digit reference number"
)

if st.button("Analyze Bill"):

    if not ref_no:
        st.warning("Please enter a reference number.")
    
    else:

        with st.spinner("Fetching bill..."):

            html = get_bill(ref_no.strip())
            bill_data = parse_bill(html)

            st.write(bill_data)
        
        st.success("Bill analyzed successfully!")

        st.subheader("Consumer Details")

        col1, col2 = st.columns(2)

        with col1:
            st.metric(
                "Reference Number",
                bill_data["reference_no"]
            )

            st.metric(
                "Units",
                bill_data["units"]
            )
        
        with col2:
            st.metric(
                "Bill Month",
                bill_data["billing_month"]
            )

            st.metric(
                "Due Date",
                bill_data["due_date"]
            )
        
        st.subheader("💰 Amount Details")

        col1, col2 = st.columns(2)

        with col1:
            st.metric(
                "Current Bill",
                f'Rs. {bill_data["current_bill"]}'
            )
        
        with col2:
            st.metric(
                "Grand Total",
                f'Rs. {bill_data["grand_total"]}'
            )