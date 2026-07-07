import streamlit as st
from translator import translate_text

st.set_page_config(
    page_title="AI Language Translator",
    page_icon="🌍",
    layout="centered"
)

st.title("🌍 AI Language Translator")
st.write("Translate text using NVIDIA Nemotron AI")

# Language options
languages = [
    "English",
    "Hindi",
    "Marathi",
    "French",
    "German",
    "Spanish",
    "Japanese",
    "Chinese",
    "Arabic",
    "Russian"
]

source_language = st.selectbox(
    "Source Language",
    languages,
    index=0
)

target_language = st.selectbox(
    "Target Language",
    languages,
    index=1
)

text = st.text_area(
    "Enter text",
    height=180,
    placeholder="Type your text here..."
)

if st.button("🚀 Translate"):

    if text.strip() == "":
        st.warning("Please enter some text.")

    else:

        with st.spinner("Translating..."):

            translated = translate_text(
                text,
                source_language,
                target_language
            )

        st.success("Translation Complete!")

        st.text_area(
            "Translated Text",
            translated,
            height=180
        )