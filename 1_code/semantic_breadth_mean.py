import pandas as pd

# Initialize an empty DataFrame to store the data from the CSV files
combined_df = pd.DataFrame()

# Loop through the file numbers from 1 to 10
for file_number in range(1, 11):
    
    # Construct the file name using the suffix
    file_name = f"semantic_breadth_{file_number}_transposed.csv"
    file_path = f"/Users/kawaiyuen/nlpworkshop/concept-creep-chi/2_pipeline/preprocessed/semantic_breadth_samples/{file_name}"

    # Read the transposed CSV file for the corresponding file number
    df = pd.read_csv(file_path, index_col='Year')

    # Append the data to the combined DataFrame
    combined_df = pd.concat([combined_df, df])

# Calculate the mean value across the rows (concepts) for each year
mean_df = combined_df.groupby('Year').mean()

# Define the path to the output CSV file
output_path = '/Users/kawaiyuen/nlpworkshop/concept-creep-chi/2_pipeline/tmp/semantic_breadth_mean.csv'

# Save the mean values DataFrame as a CSV file
mean_df.to_csv(output_path)

print("Mean values saved to:", output_path)