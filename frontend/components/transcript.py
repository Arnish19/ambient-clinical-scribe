import streamlit as st


def render_transcript(transcript):

    st.subheader("📝 Transcript")

    if transcript:

        st.text_area(
            "",
            transcript,
            height=250,
        )

    else:

        st.info(
            "No transcript generated yet."
        )