import streamlit as st
from prediction_helper import predict

# --------------------------------------------------
# Page configuration
# --------------------------------------------------
st.set_page_config(page_title="Credit Risk Modeling")

st.title("Credit Risk Modeling")
st.caption("Enter applicant and loan details to assess credit risk")

st.write("")

# --------------------------------------------------
# Input Layout (3 per row)
# --------------------------------------------------
row1 = st.columns(3)
row2 = st.columns(3)
row3 = st.columns(3)
row4 = st.columns(3)

# Row 1
with row1[0]:
    age = st.number_input("Age", min_value=18, max_value=100, step=1, value=28)

with row1[1]:
    income = st.number_input("Income", min_value=0, value=1_200_000)

with row1[2]:
    loan_amount = st.number_input("Loan Amount", min_value=0, value=2_560_000)

# Loan to Income Ratio (calculated)
loan_to_income_ratio = loan_amount / income if income > 0 else 0
with row2[0]:
    st.metric("Loan to Income Ratio", f"{loan_to_income_ratio:.2f}")

# Row 2
with row2[1]:
    loan_tenure_months = st.number_input(
        "Loan Tenure (Months)", min_value=1, step=1, value=36
    )

with row2[2]:
    avg_dpd_per_delinquency = st.number_input(
        "Avg DPD", min_value=0, value=20
    )

# Row 3
with row3[0]:
    delinquency_ratio = st.number_input(
        "Delinquency Ratio (%)", min_value=0, max_value=100, step=1, value=30
    )

with row3[1]:
    credit_utilization_ratio = st.number_input(
        "Credit Utilization Ratio (%)", min_value=0, max_value=100, step=1, value=30
    )

with row3[2]:
    num_open_accounts = st.number_input(
        "Open Loan Accounts", min_value=1, max_value=4, step=1, value=2
    )

# Row 4
with row4[0]:
    residence_type = st.selectbox(
        "Residence Type", ["Owned", "Rented", "Mortgage"]
    )

with row4[1]:
    loan_purpose = st.selectbox(
        "Loan Purpose", ["Education", "Home", "Auto", "Personal"]
    )

with row4[2]:
    loan_type = st.selectbox(
        "Loan Type", ["Unsecured", "Secured"]
    )

st.write("")

# --------------------------------------------------
# Prediction Section
# --------------------------------------------------
if st.button("Calculate Risk"):
    probability, credit_score, rating = predict(
        age,
        income,
        loan_amount,
        loan_tenure_months,
        avg_dpd_per_delinquency,
        delinquency_ratio,
        credit_utilization_ratio,
        num_open_accounts,
        residence_type,
        loan_purpose,
        loan_type
    )

    st.write("")
    st.subheader("Risk Assessment")

    result_cols = st.columns(3)

    with result_cols[0]:
        st.markdown("**Default Probability**")
        st.markdown(
            f"<span style='font-size:2rem;'>{probability:.2%}</span>",
            unsafe_allow_html=True
        )

    with result_cols[1]:
        st.markdown("**Credit Score**")
        st.markdown(
            f"<span style='font-size:2rem;'>{credit_score}</span>",
            unsafe_allow_html=True
        )

    with result_cols[2]:
        st.markdown("**Rating**")
        st.markdown(
            f"<span style='font-size:2rem;'>{rating}</span>",
            unsafe_allow_html=True
        )
