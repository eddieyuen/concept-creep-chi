import pandas as pd

# Read the original CSV file
df = pd.read_csv('/Users/kawaiyuen/nlpworkshop/concept-creep-chi/2_pipeline/preprocessed/semantic_breadth/semantic_breadth_1st.csv')

# Transpose the DataFrame to have concepts as columns and years as rows
transposed_df = df.pivot(index='Year', columns='Concept', values=['Mean Cosine Similarity', 'Semantic Breadth'])

# Flatten the column labels
transposed_df.columns = [f"{col[1]}_{col[0].replace(' ', '_')}" for col in transposed_df.columns]

# Save the transposed DataFrame to a new CSV file
transposed_df.to_csv('/Users/kawaiyuen/nlpworkshop/concept-creep-chi/2_pipeline/preprocessed/semantic_breadth/semantic_breadth_1st_transposed.csv', index_label='Year')

print("CSV file with the desired structure has been created.")