"""This is a streamlit dashboard for visualising vectors similarity"""
import streamlit as st

st.set_page_config(layout="wide")

import os

import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from bertopic import BERTopic

st.title("BERTopic demo")
st.write("This a simple dashboard to visualize the BERTopic cluster/topic modelling technique.")
st.write("Embeddings used are from the 'all-MiniLM-L12-v2' sentence transformer model.")
st.write("Data is a sample from the Medium articles dataset.")

# Number of BERTOpics to keep
nr_topics = st.sidebar.selectbox("Number of topics to keep", (5, 10, 30, 50, 100), )

# Reading the article text
docs = pd.read_csv('./data/train_data.csv').loc[:, 'text']

# Loading ready embeddings
embeddings = pd.read_parquet("./data/st_vectors.parquet").to_numpy()

vectorizer_model = CountVectorizer(stop_words="english")
topic_model = BERTopic(vectorizer_model=vectorizer_model)
# Performing BERTopic
st.write("Training a model. This might take ca. 2 min. Grab a coffee, talk to a friend...")
topics, probs = topic_model.fit_transform(docs, embeddings)

st.write(f"{len(set(topics))} Topics found:")
st.dataframe(topic_model.get_topic_info())

st.write("Reducing the number of topics (the plot gets convoluted otherwise...")
topic_model.reduce_topics(docs, nr_topics=nr_topics)
the_plot = topic_model.visualize_topics()
st.plotly_chart(the_plot)

st.write("Done visualizing")