from collections import namedtuple
import altair as alt
import math
import json
import pandas as pd
import streamlit as st
import requests

"""
# Welcome to Streamlit!

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:

If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:
"""

URL = "http://34.145.255.161/v1/models/bart-xsum-hcl:predict"
HOST = "summariser-mvp.default.example.com"

def post(payload, headers, url=URL):
    try:
        result = requests.post(url,headers=headers , data=payload)
        return result.json()

    except Exception:
        return {}


def build_headers(host=HOST):
    headers = {"host": host}
    return headers

def build_payload(sentence):
    payload = {"instances": [
        {
            "text": sentence
        }
    ]}

    return json.dumps(payload)

def get_prediction(res):
    pred = None
    if "predictions" in res:
        for pred in res["predictions"]:
            pred = pred
    return pred

st.title("Summarize Text")
sentence = st.text_area('Please paste your article :', height=30)
button = st.button("Summarize")

max = st.sidebar.slider('Select max', 50, 500, step=10, value=150)
min = st.sidebar.slider('Select min', 10, 450, step=10, value=50)

do_sample = st.sidebar.checkbox("Do sample", value=False)


with st.spinner("Generating Summary.."):
    if button and sentence:
        headers = build_headers()
        payload = build_payload(sentence)
        res = post(payload, headers)
        text = get_prediction(res)
        # st.write(result[0]['summary_text'])
        st.write(text)
