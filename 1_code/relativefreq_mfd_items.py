import pandas as pd

# Step 1: Calculate relative frequency
def calculate_relative_frequency(frequency_data, token_counts):
    return frequency_data.div(token_counts['Token Count'], axis=0)

# Step 2: Scale frequency data
def scale_frequency_data(relative_frequency):
    max_values = relative_frequency.max(axis=0)
    scaled_data = relative_frequency.divide(max_values, axis=1) * 100
    return scaled_data

# Specify file paths
frequency_file_path = '/Users/kawaiyuen/nlpworkshop/concept-creep-chi/2_pipeline/preprocessed/frequency_mfd_items.csv'
token_counts_file_path = '/Users/kawaiyuen/nlpworkshop/concept-creep-chi/2_pipeline/preprocessed/token_counts.csv'
output_file_path = '/Users/kawaiyuen/nlpworkshop/concept-creep-chi/2_pipeline/preprocessed/relativefreq_mfd_items.csv'

# Read frequency data and token counts
frequency_data = pd.read_csv(frequency_file_path, index_col=0)
token_counts = pd.read_csv(token_counts_file_path, index_col=0)

# Step 1: Calculate relative frequency
relative_frequency = calculate_relative_frequency(frequency_data, token_counts)

# Step 2: Scale frequency data
scaled_data = scale_frequency_data(relative_frequency)

# Store the resulting CSV file
scaled_data.to_csv(output_file_path)

print("Scaled frequency data processed and stored in", output_file_path)