import streamlit as st
from PIL import Image
import scipy.io.wavfile as wavfile
import torch
import numpy as np

from transformers import (
    AutoProcessor,
    AutoModelForMultimodalLM,
    AutoTokenizer,
    VitsModel
)


model_path = "Salesforce/blip-image-captioning-large"
tts_model_path = "kakao-enterprise/vits-ljs"


@st.cache_resource
def load_models():

    caption_processor = AutoProcessor.from_pretrained(
        model_path
    )

    caption_model = AutoModelForMultimodalLM.from_pretrained(
        model_path
    )

    tts_tokenizer = AutoTokenizer.from_pretrained(
        tts_model_path
    )

    tts_model = VitsModel.from_pretrained(
        tts_model_path
    )

    return (
        caption_processor,
        caption_model,
        tts_tokenizer,
        tts_model
    )


(
    caption_processor,
    caption_model,
    tts_tokenizer,
    tts_model
) = load_models()


def generate_audio(text):

    text = str(text).strip()

    inputs = tts_tokenizer(
        text,
        return_tensors="pt"
    )

    with torch.no_grad():

        output = tts_model(
            **inputs
        ).waveform

    audio = output.squeeze().cpu().numpy()

    audio = np.asarray(
        audio,
        dtype=np.float32
    )

    output_file = "output.wav"

    wavfile.write(
        output_file,
        rate=tts_model.config.sampling_rate,
        data=audio
    )

    with open(
        output_file,
        "rb"
    ) as audio_file:

        audio_bytes = audio_file.read()

    return audio_bytes


def clean_caption(caption):

    caption = str(caption).strip()

    unwanted_phrases = [
        "describe this image.",
        "describe this image",
        "a picture of",
        "an image of"
    ]

    for phrase in unwanted_phrases:

        caption = caption.replace(
            phrase,
            ""
        )

    caption = " ".join(
        caption.split()
    )

    words = caption.split()

    cleaned_words = []

    for word in words:

        if len(cleaned_words) >= 2:

            if (
                word.lower()
                == cleaned_words[-1].lower()
            ):

                continue

            if (
                word.lower()
                == cleaned_words[-2].lower()
            ):

                continue

        cleaned_words.append(word)

    caption = " ".join(
        cleaned_words
    )

    if caption:

        caption = (
            caption[0].upper()
            + caption[1:]
        )

    if caption and caption[-1] not in ".!?":

        caption += "."

    return caption


def caption_my_image(pil_image):

    inputs = caption_processor(
        images=pil_image,
        text=(
            "Describe the people, important objects, "
            "activities, food, drinks, and decorations "
            "in this image."
        ),
        return_tensors="pt"
    )

    with torch.no_grad():

        output = caption_model.generate(
            **inputs,
            max_new_tokens=50,
            num_beams=5,
            no_repeat_ngram_size=3,
            repetition_penalty=1.2,
            early_stopping=True
        )

    caption = caption_processor.batch_decode(
        output,
        skip_special_tokens=True
    )[0]

    caption = clean_caption(
        caption
    )

    if not caption:

        caption = (
            "I could not generate a caption "
            "for this image."
        )

    audio = generate_audio(
        caption
    )

    return (
        caption,
        audio
    )


st.set_page_config(
    page_title="Image Captioning",
    page_icon="🖼️",
    layout="centered"
)

st.title("Image Captioning")

st.write(
    "Upload an image to generate a detailed caption "
    "and listen to the generated audio."
)

uploaded_file = st.file_uploader(
    "Select Image",
    type=[
        "jpg",
        "jpeg",
        "png",
        "webp"
    ]
)

if uploaded_file is not None:

    image = Image.open(
        uploaded_file
    ).convert("RGB")

    st.subheader("Selected Image")

    st.image(
        image,
        use_container_width=True
    )

    if st.button("Generate Caption"):

        with st.spinner(
            "Generating image caption and audio..."
        ):

            caption, audio = caption_my_image(
                image
            )

        st.subheader("Image Caption")

        st.write(
            caption
        )

        st.subheader("Generated Audio")

        st.audio(
            audio,
            format="audio/wav"
        )