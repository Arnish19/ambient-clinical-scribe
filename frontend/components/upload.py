import streamlit as st


def render_upload():

    st.subheader("🎤 Upload Audio")

    uploaded_file = st.file_uploader(
        "Choose an audio file",
        type=[
            "mp3",
            "wav",
            "m4a",
        ],
    )

    return uploaded_file