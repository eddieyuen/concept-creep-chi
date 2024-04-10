import os
import pandas as pd
from gensim.models import Word2Vec

def load_word2vec_models(model_folder_path: str):
    models = {}
    for year in range(1979, 2024):
        model_path = os.path.join(model_folder_path, f'pd_{year}.model')
        models[year] = Word2Vec.load(model_path)
    return models

# Specify the path to the token_counts.csv file
csv_filepath = '/Users/kawaiyuen/nlpworkshop/concept-creep-chi/2_pipeline/preprocessed/token_counts.csv'

# Load the existing DataFrame from the CSV
df = pd.read_csv(csv_filepath)

# Load the Word2Vec models
model_folder_path = '/Users/kawaiyuen/nlpworkshop/concept-creep-chi_raw/models'
models = load_word2vec_models(model_folder_path)

# Calculate vocabulary size for each year
vocabulary_sizes = {}
for year, model in models.items():
    vocabulary_sizes[year] = len(model.wv)

# Add the Vocabulary Size column to the DataFrame
df['Vocabulary Size'] = df['Year'].map(vocabulary_sizes)

# Save the updated DataFrame to the CSV file
df.to_csv(csv_filepath, index=False)

print("Vocabulary sizes added to:", csv_filepath)