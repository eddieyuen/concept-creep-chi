import os
import json
import pandas as pd
from gensim.models import Word2Vec
import numpy as np

def load_dict(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data

def load_word2vec_models(model_folder_path: str):
    models = {}
    for year in range(1979, 2024):
        model_path = os.path.join(model_folder_path, f'pd_{year}.model')
        models[year] = Word2Vec.load(model_path)
    return models

def calculate_cosine_similarities(models, targets, foundations):
    similarities = {}
    for year, model in models.items():
        similarities[year] = {}
        for target_name, target_words in targets.items():
            similarities[year][target_name] = {}
            for foundation_name, foundation_words in foundations.items():
                filtered_target_words = [word for word in target_words if word in model.wv.key_to_index]
                filtered_foundation_words = [word for word in foundation_words if word in model.wv.key_to_index]
                try:
                    similarity = model.wv.n_similarity(filtered_target_words, filtered_foundation_words)
                except:
                    similarity = np.nan
                    print(f'Not found for {target_words} and {filtered_foundation_words} in {year}')

                similarities[year][target_name][foundation_name] = similarity
    return similarities

# Create paths to the data and output folders
foundations_path = '/Users/kawaiyuen/nlpworkshop/concept-creep-chi/0_data/wordlist/cmfd_final.json'   #CMFD
concepts_path = '/Users/kawaiyuen/nlpworkshop/concept-creep-chi/0_data/wordlist/concepts.json'    # concepts

foundations = load_dict(foundations_path)
concepts = load_dict(concepts_path)

# Models
model_folder_path = '/Users/kawaiyuen/nlpworkshop/concept-creep-chi_raw/models'
models = load_word2vec_models(model_folder_path)

similarities = calculate_cosine_similarities(models, concepts, foundations)

# Prepare data for CSV
data = []
for year, targets in similarities.items():
    row = {'Year': year}
    for target_name, foundation_similarities in targets.items():
        for foundation_name, similarity in foundation_similarities.items():
            column_name = f"{target_name}_{foundation_name}"
            row[column_name] = similarity
    data.append(row)

# Convert data to DataFrame
df = pd.DataFrame(data)

# Specify the CSV file path
csv_filepath = '/Users/kawaiyuen/nlpworkshop/concept-creep-chi/2_pipeline/preprocessed/cos-sim_cmfd.csv'

# Save the DataFrame as CSV
df.to_csv(csv_filepath, index=False)

print("Cosine similarities computed and saved to:", csv_filepath)