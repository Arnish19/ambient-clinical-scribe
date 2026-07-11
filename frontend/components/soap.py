import streamlit as st


def render_soap(soap):

    st.subheader("🩺 SOAP Note")

    if not soap:

        st.info(
            "SOAP note not available."
        )
        return

    st.markdown(
        f"### Subjective\n\n{soap['subjective']}"
    )

    st.markdown(
        f"### Objective\n\n{soap['objective']}"
    )

    st.markdown(
        f"### Assessment\n\n{soap['assessment']}"
    )

    st.markdown(
        f"### Plan\n\n{soap['plan']}"
    )