import csv
import pickle

output_csv = '/Users/kawaiyuen/nlpworkshop/concept-creep-chi/2_pipeline/token_counts.csv'

# Initialize the data list to store year and token counts
data = []

# Loop through the years from 1979 to 2021
for year in range(1979, 2022):
    cleaned_data_path = f'/Users/kawaiyuen/nlpworkshop/concept-creep-chi_raw/cleanedtext/cleaned_{year}.pkl'

    with open(cleaned_data_path, 'rb') as f:
        cleaned_tokens = pickle.load(f)

    total_tokens = sum(len(sentence) for sentence in cleaned_tokens)

    # Append the year and token count to the data list
    data.append([year, total_tokens])

# Write the data to the output CSV file
with open(output_csv, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Year', 'Token Count'])
    writer.writerows(data)

print(f"The token counts have been stored in the CSV file: {output_csv}")