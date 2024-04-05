import csv

csv_file = '/Users/kawaiyuen/nlpworkshop/concept-creep-chi/2_pipeline/preprocessed/frequency_cmfd_filtered&rmdup.csv'
transposed_csv_file = '/Users/kawaiyuen/nlpworkshop/concept-creep-chi/2_pipeline/preprocessed/frequency_cmfd_filtered&rmdup_transposed.csv'

tokens = []

# Read the CSV file and extract the tokens
with open(csv_file, 'r') as file:
    reader = csv.reader(file)
    header = next(reader)  # Skip the header row
    for row in reader:
        tokens.append(row[0])

# Transpose the data and write to a new CSV file
with open(transposed_csv_file, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Year'] + tokens)  # Write the header row
    for i, year in enumerate(header[2:-1]):
        row = [year] + [row[i + 2] for row in csv.reader(open(csv_file, 'r'))][1:]
        writer.writerow(row)

print("Data transposed and saved to:", transposed_csv_file)