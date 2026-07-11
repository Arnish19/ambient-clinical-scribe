import streamlit as st


def render_download(pdf):

    if pdf:

        st.download_button(
            "📄 Download Clinical Report",
            pdf,
            file_name="clinical_report.pdf",
            mime="application/pdf",
            use_container_width=True,
        )