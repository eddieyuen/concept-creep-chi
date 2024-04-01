import pandas as pd
import pickle

# Load the CSV file
cmfd_data = pd.read_csv('/Users/kawaiyuen/nlpworkshop/concept-creep-chi/0_data/wordlist/cmfd.csv')
frequency_cmfd = pd.read_csv('/Users/kawaiyuen/nlpworkshop/concept-creep-chi/2_pipeline/preprocessed/frequency_cmfd.csv')

for year in range (2017, 2024):

    # Load the pickle file
    with open(f'/Users/kawaiyuen/nlpworkshop/concept-creep-chi_raw/cleanedtext/cleaned_{year}.pkl', 'rb') as file:
        cleaned_tokens = pickle.load(file)

    # Function to count frequency
    def count_frequency(tokens, target):
        count = 0
        for sentence in tokens:
            for token in sentence:
                if token == target:
                    count += 1
        return count

    # Add frequency column 
    frequency_cmfd[f'{year}'] = cmfd_data['chinese'].apply(lambda x: count_frequency(cleaned_tokens, x))

    # Save the updated data 
    frequency_cmfd.to_csv('/Users/kawaiyuen/nlpworkshop/concept-creep-chi/2_pipeline/preprocessed/frequency_cmfd.csv', index=False)
    print(f'Frequency data for {year} saved.')

print('All frequency data computed and saved.')