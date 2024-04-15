import random
import numpy as np
import pandas as pd
from gensim.models import Word2Vec
import pickle
from sklearn.metrics.pairwise import cosine_similarity
import json
import time
import csv

for file_number in range(1,11):

    # Initialize an empty list to store the results
    results = []

    # Initialize an empty dictionary to store the concept usages
    concept_usages_dict = {}

    # Initialize an empty list to store the context window lists
    context_window_lists_all = []

    # Read the concepts from the JSON file
    with open('/Users/kawaiyuen/nlpworkshop/concept-creep-chi/0_data/wordlist/control_words.json', 'r') as f:
        concepts = json.load(f)

    # Loop through the years from 1979 to 2023
    for year in range(1979, 2024):

        # Load the pretrained Word2Vec model and cleaned data for the year
        model_path = f'/Users/kawaiyuen/nlpworkshop/concept-creep-chi_raw/models/pd_{year}.model'
        try:
            model = Word2Vec.load(model_path)
        except FileNotFoundError:
            print(f"Model not found for {year}. Skipping...")
            continue

        cleaned_data_path = f'/Users/kawaiyuen/nlpworkshop/concept-creep-chi_raw/cleanedtext/cleaned_{year}.pkl'
        with open(cleaned_data_path, 'rb') as f:
            cleaned_data = pickle.load(f)

        # Loop through the concepts and their first items in the list
        for key, value in concepts.items():
            concept = value[0]  # Get the first item in the list

            # Step 1: Randomly sample specific usages of a concept from the corpus
            token_occurrence = [token for sentence in cleaned_data for token in sentence if token == concept]
            token_frequency = len(token_occurrence)
            print(f'Frequency for {concept} in {year}: {token_frequency}')

            # Check the population size and adjust the sampling accordingly
            if token_frequency < 10:
                print(f"The frequency for '{concept}' in {year} is smaller than 10. Skipping the year.")
                # Append 'NA' values to the results list for this year and concept
                results.append({'Year': year, 'Concept': concept, 'Mean Cosine Similarity': 'NA', 'Semantic Breadth': 'NA'})
                continue
            elif 10 <= token_frequency <= 50:
                concept_usages = [sentence for sentence in cleaned_data if concept in sentence]
            else:
                concept_usages = [sentence for sentence in cleaned_data if concept in sentence]
                if len(concept_usages) > 50: 
                    random.seed(int(time.time()))
                    random_concept_usages = random.sample(concept_usages, k=50)
                    concept_usages = random_concept_usages
                else:
                    concept_usages = [sentence for sentence in cleaned_data if concept in sentence]
                
            # Step 2: Compute the context vectors for each specific usage of the concept
            if 'concept_usages' in locals():
                contextualized_representations = []
                window_size = 9

                for j, sentence in enumerate(concept_usages):  
                    context_words = []  # To store the words within the context window
                    context_vectors = []

                    # Find the position of the target concept within the sentence
                    concept_position = [i for i, token in enumerate(sentence) if token == concept]

                    # For each instance of the target concept, extract the words within the context window
                    for position in concept_position:
                        start_index = max(0, position - window_size)
                        end_index = min(len(sentence), position + window_size + 1)
                        context_words.extend(sentence[start_index:position] + sentence[position + 1:end_index])
                    # Remove the target concept from the context_words list
                    context_words = [word for word in context_words if word != concept]

                    # Store the context window lists for each specific usage in a CSV file
                    with open(f'/Users/kawaiyuen/nlpworkshop/concept-creep-chi/2_pipeline/preprocessed/semantic_breadth_control_words/context_window_lists_{file_number}.csv', 'a', newline='') as csvfile:
                        writer = csv.writer(csvfile)
                        # Check if the file is empty
                        if csvfile.tell() == 0:
                            writer.writerow(['Year', 'Control Words', 'Sentence With Control Words', 'Context Words'])
                        writer.writerow([year, concept, j+1, context_words])
                    
                    # Get the word vectors for the context words (if available in the Word2Vec model)
                    context_vectors.extend([model.wv[word] for word in context_words if word in model.wv])
                    context_vectors = np.array(context_vectors)
                    if len(context_vectors) > 0:
                        # Compute the centroid of the context vectors
                        contextualized_representation = np.mean(context_vectors, axis=0)
                        # Append the centroid to the list of contextualized representations
                        contextualized_representations.append(contextualized_representation)
                    else:
                        continue
                    
                # Step 3: Calculate pairwise cosine similarities among the sampled specific usages
                contextualized_representations = np.array(contextualized_representations)
                pairwise_similarities = cosine_similarity(contextualized_representations)
                # Zero out the lower triangular part of the matrix (including the diagonal)
                pairwise_similarities_upper = np.triu(pairwise_similarities, k=1)

                # Step 4: Calculate semantic breadth index as the inverse of the mean cosine similarity
                mean_cosine_similarity = np.mean(pairwise_similarities_upper[pairwise_similarities_upper != 0])
                semantic_breadth = 1 / mean_cosine_similarity

                # Append the results to the list
                results.append({'Year': year, 'Control Word': concept, 'Mean Cosine Similarity': mean_cosine_similarity, 'Semantic Breadth':semantic_breadth})

    # Convert the results list to a DataFrame
    results_df = pd.DataFrame(results)

    # Define the path to the output CSV file
    output_path = f'/Users/kawaiyuen/nlpworkshop/concept-creep-chi/2_pipeline/preprocessed/semantic_breadth_control_words/controls_sb_{file_number}.csv'

    # Save the DataFrame as a CSV file
    results_df.to_csv(output_path, index=False)

    print("Semantic breadth output saved to: ", output_path)

    # Transposing the CSV file output
    # Read the original CSV file
    df = pd.read_csv(output_path)

    # Transpose the DataFrame to have concepts as columns and years as rows
    transposed_df = df.pivot(index='Year', columns='Control Word', values=['Mean Cosine Similarity', 'Semantic Breadth'])

    # Flatten the column labels
    transposed_df.columns = [f"{col[1]}_{col[0].replace(' ', '_')}" for col in transposed_df.columns]

    # Save the transposed DataFrame to a new CSV file
    transposed_df.to_csv(f'/Users/kawaiyuen/nlpworkshop/concept-creep-chi/2_pipeline/preprocessed/semantic_breadth_control_words/controls_sb_{file_number}_transposed.csv', index_label='Year')

    print(f"CSV file with the desired structure has been created: Filenumber {file_number}")