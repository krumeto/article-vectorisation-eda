# article-vectorisation-eda
A repo to explore article vectorisation with a scikit-learn API.

The repo was built for the **Creating and assessing media article embeddings** talk in front of Sofia Data Science Society.

## Data

The data used is a [kaggle dataset, containing Medium articles](https://www.kaggle.com/datasets/fabiochiusano/medium-articles). The dataset can be downloaded directly from Kaggle or via the kaggle API (for which you'd need Kaggle key and username).

KAGGLE_USERNAME=***************

KAGGLE_KEY=******************

## Showcases

1. Vectorisation with the libraries' native APIs - notebooks/Article_Vectorisation_Exploration.ipynb
2. Vectorisation with the scikit-learn API (using the `articlevectorizer` package) - notebooks/Article_Vectorisation_sklearn_api.ipynb
3. Showcase [bulk](https://github.com/koaning/bulk) project by Vincent Warmerdam by running `python -m bulk text data/titles_and_vectors_for_bulk.csv`
    - bulk requires a csv with the text data in a `text` column and columns x and y being the result of a dimensionality reduction technique. For this demo, UMAP was used.
4. A small streamlit app to showcase the BERTopic project - run `streamlit run streamlit_demo/bertopic_demo.py`

## Slides for the talk:


[Slides](DS&#32;in&#32;Media&#32;-&#32;Article&#32;Vectorisation.pdf) 

## Requirements

Requirements can be installed via 
```
pip install requirements.txt
```
