import streamlit as st

from api import (
    download_report,
    generate_icd,
    generate_soap,
    generate_transcript,
    upload_audio,
)
from components.icd import render_icd
from components.report import render_download
from components.soap import render_soap
from components.transcript import render_transcript
from components.upload import render_upload

st.set_page_config(
    page_title="Ambient Clinical Scribe",
    page_icon="🩺",
    layout="wide",
)

st.title("🩺 Ambient Clinical Scribe")
st.caption("AI-powered Clinical Documentation System")

# ----------------------------
# Session State
# ----------------------------

defaults = {
    "audio_id": None,
    "transcript": None,
    "soap": None,
    "icd": None,
    "pdf": None,
}

for key, value in defaults.items():
    if key not in st.session_state:
        st.session_state[key] = value

left, right = st.columns([1, 3])

# ============================================================
# LEFT SIDEBAR
# ============================================================

with left:

    uploaded_file = render_upload()

    if uploaded_file:

        if st.button(
            "⬆ Upload Audio",
            use_container_width=True,
        ):

            with st.spinner("Uploading..."):

                response = upload_audio(uploaded_file)

                st.session_state.audio_id = response["id"]

                st.success("Audio uploaded successfully.")

    st.divider()

    st.subheader("Status")

    if st.session_state.audio_id:
        st.success("✅ Uploaded")
    else:
        st.info("Upload pending")

    if st.session_state.transcript:
        st.success("✅ Transcript")
    else:
        st.info("Transcript pending")

    if st.session_state.soap:
        st.success("✅ SOAP")
    else:
        st.info("SOAP pending")

    if st.session_state.icd:
        st.success("✅ ICD")
    else:
        st.info("ICD pending")

# ============================================================
# RIGHT PANEL
# ============================================================

with right:

    if st.session_state.audio_id:

        c1, c2, c3 = st.columns(3)

        with c1:

            if st.button(
                "Generate Transcript",
                use_container_width=True,
            ):

                with st.spinner("Transcribing..."):

                    transcript = generate_transcript(
                        st.session_state.audio_id
                    )

                    st.session_state.transcript = (
                        transcript["transcript"]
                    )

        with c2:

            if st.button(
                "Generate SOAP",
                use_container_width=True,
            ):

                with st.spinner("Generating SOAP..."):

                    st.session_state.soap = generate_soap(
                        st.session_state.audio_id
                    ).get("soap_json")

        with c3:

            if st.button(
                "Generate ICD",
                use_container_width=True,
            ):

                with st.spinner("Finding ICD Codes..."):

                    st.session_state.icd = generate_icd(
                        st.session_state.audio_id
                    )

                    st.session_state.pdf = download_report(
                        st.session_state.audio_id
                    )

    st.divider()

    render_transcript(
        st.session_state.transcript
    )

    st.divider()

    render_soap(
        st.session_state.soap
    )

    st.divider()

    render_icd(
        st.session_state.icd
    )

    st.divider()

    render_download(
        st.session_state.pdf
    )