import csv

csv_file = '/Users/kawaiyuen/nlpworkshop/concept-creep-chi/2_pipeline/preprocessed/frequency_cmfd_filtered.csv'
output_file = '/Users/kawaiyuen/nlpworkshop/concept-creep-chi/2_pipeline/preprocessed/frequency_cmfd_filtered&rmdup.csv'
column_name = 'chinese'  

unique_rows = []

# Read the CSV file and check for duplicate values in the specified column
with open(csv_file, 'r') as file:
    reader = csv.DictReader(file)
    unique_values = set()
    duplicate_values = set()
    for row in reader:
        value = row[column_name]
        if value not in unique_values:
            unique_values.add(value)
        else:
            duplicate_values.add(value)

    # Reset the file pointer to the beginning
    file.seek(0)
    next(reader)  # Skip the header row

    # Copy only the rows with unique values in the specified column
    for row in reader:
        value = row[column_name]
        if value not in duplicate_values:
            unique_rows.append(row)

# Write the unique rows to a new CSV file
header = unique_rows[0].keys()

with open(output_file, 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=header)
    writer.writeheader()
    writer.writerows(unique_rows)

print("Rows with duplicate values in column '{}' removed.".format(column_name))
print("Unique rows saved to:", output_file)