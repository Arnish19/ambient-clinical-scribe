import requests

from config import API_URL


def upload_audio(file):

    response = requests.post(
        f"{API_URL}/audio/upload",
        files={
            "file": (
                file.name,
                file,
                file.type,
            )
        },
    )

    response.raise_for_status()

    return response.json()


def generate_transcript(audio_id):

    response = requests.post(
        f"{API_URL}/transcript/{audio_id}"
    )

    response.raise_for_status()

    return response.json()


def generate_soap(audio_id):

    response = requests.post(
        f"{API_URL}/soap/{audio_id}"
    )

    response.raise_for_status()

    return response.json()


def generate_icd(audio_id):

    response = requests.post(
        f"{API_URL}/icd/{audio_id}"
    )

    response.raise_for_status()

    return response.json()


def download_report(audio_id):

    response = requests.get(
        f"{API_URL}/report/{audio_id}"
    )

    response.raise_for_status()

    return response.content