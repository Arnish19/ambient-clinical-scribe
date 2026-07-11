import streamlit as st


def render_icd(icd):

    st.subheader("🏥 ICD-10 Recommendations")

    if not icd:

        st.info(
            "No ICD recommendations."
        )
        return

    for item in icd["recommendations"]:

        st.success(
            f"{item['code']} - {item['description']}"
        )