# article-vectorisation-eda
A repo to explore article vectorisation with a scikit-learn API

## Data

The data used is a [kaggle dataset, containing Medium articles](https://www.kaggle.com/datasets/fabiochiusano/medium-articles). The dataset can be downloaded directly from Kaggle or via the kaggle API (for which you'd need Kaggle key and username).

KAGGLE_USERNAME=***************
KAGGLE_KEY=******************

## Showcases

1. Vectorisation with the libraries' native APIs - notebooks/Article_Vectorisation_Exploration.ipynb
2. Vectorisation with the scikit-learn API (using the `articlevectorizer` package) - notebooks/Article_Vectorisation_sklearn_api.ipynb
3. Showcase (bulk)[https://github.com/koaning/bulk] project by Vincent Warmerdam by running `python -m bulk text data/titles_and_vectors_for_bulk.csv`
    - bulk requires a csv with the text data in a `text` column and columns x and y being the result of a dimensionality reduction technique. For this demo, UMAP was used.
4. 
## Requirements

Requirements can be installed via 
```
pip install requirements.txt
```
