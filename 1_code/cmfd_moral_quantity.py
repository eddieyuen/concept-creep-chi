import csv
import json

csv_file_path = '/Users/kawaiyuen/nlpworkshop/concept-creep-chi/2_pipeline/preprocessed/frequency_cmfd_rmdup_transposed.csv'
dict_file_path = '/Users/kawaiyuen/nlpworkshop/concept-creep-chi/0_data/wordlist/cmfd_rmdup_full.json'
output_file_path = '/Users/kawaiyuen/nlpworkshop/concept-creep-chi/2_pipeline/tmp/cmfd_salience.csv'

data = []
with open(csv_file_path, 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        data.append(row)

with open(dict_file_path, 'r') as file:
    dictionary = json.load(file)

totals = {}
for row in data[1:]:
    year = row[0]
    frequencies = [int(x) for x in row[1:]]
    total = sum(frequencies)
    totals[year] = total

foundation_totals = {}
for moral_foundation in dictionary:
    foundation_totals[moral_foundation] = {}
    for year in range(1, len(data)):
        foundation_totals[moral_foundation][data[year][0]] = 0
for moral_foundation, words in dictionary.items():
    for year in range(1, len(data)):
        total = sum([int(data[year][i]) for i, word in enumerate(data[0][1:]) if word in words])
        foundation_totals[moral_foundation][data[year][0]] = total

with open(output_file_path, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Year'] + list(dictionary.keys()))
    for year in range(1, len(data)):
        writer.writerow([data[year][0]] + [foundation_totals[moral_foundation][data[year][0]] for moral_foundation in dictionary])
