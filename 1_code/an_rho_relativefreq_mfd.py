import pandas as pd
from scipy.stats import spearmanr

# Read the CSV file
data = pd.read_csv("/Users/kawaiyuen/nlpworkshop/concept-creep-chi/2_pipeline/tmp/relativefreq_mfd.csv")

# Extract the relevant columns
years = data["Year"]
foundations = data.iloc[:, 1:] 

# Compute the Spearman correlation and p-values
correlations = []
p_values = []

for column in foundations.columns:
    correlation, p_value = spearmanr(years, foundations[column])
    correlations.append(correlation)
    p_values.append(p_value)

# Save the output to the specified directory
output_dir = "/Users/kawaiyuen/nlpworkshop/concept-creep-chi/3_output/relativefreq/"
output_file = output_dir + "spearman-rho_mfd.txt"
with open(output_file, "w") as file:
    for i in range(len(correlations)):
        foundation = foundations.columns[i]
        file.write(f"Target Concept: {foundation}\n")
        file.write(f"Spearman Correlation: {correlations[i]}\n")
        file.write(f"P-value: {p_values[i]}\n\n")