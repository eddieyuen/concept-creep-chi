import json
import csv

csv_file = '/Users/kawaiyuen/nlpworkshop/concept-creep-chi/2_pipeline/preprocessed/relativefreq_cmfd_items.csv'
json_file = '/Users/kawaiyuen/nlpworkshop/concept-creep-chi/0_data/wordlist/cmfd_final.json'
output_file = '/Users/kawaiyuen/nlpworkshop/concept-creep-chi/2_pipeline/tmp/relativefreq_cmfd.csv'

# Load the JSON dictionary
with open(json_file, 'r') as file:
    json_data = json.load(file)

# Extract the moral foundation categories and corresponding tokens
moral_foundations = list(json_data.keys())

# Initialize a dictionary to store the sum and count for each moral foundation
mean_relative_frequency = {foundation: {'sum': [], 'count': []} for foundation in moral_foundations}

# Read the CSV file and compute the sum and count for each moral foundation across each year
with open(csv_file, 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        year = row['Year']
        for foundation in moral_foundations:
            tokens = json_data[foundation]
            foundation_relative_frequency = sum([float(row[token]) for token in tokens])
            mean_relative_frequency[foundation]['sum'].append(foundation_relative_frequency)
            mean_relative_frequency[foundation]['count'].append(len(tokens))

# Compute the mean relative frequency for each moral foundation
for foundation, data in mean_relative_frequency.items():
    sum_values = data['sum']
    count_values = data['count']
    mean_values = [sum_value / count_value for sum_value, count_value in zip(sum_values, count_values)]
    mean_relative_frequency[foundation] = mean_values

# Write the mean relative frequencies to a new CSV file
header = ['Year'] + moral_foundations

with open(output_file, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(header)

    years = list(range(1979, 2024))
    for i in range(len(years)):
        year = years[i]
        values = [mean_relative_frequency[foundation][i] for foundation in moral_foundations]
        writer.writerow([year] + values)

print("Mean relative frequencies computed and saved to:", output_file)