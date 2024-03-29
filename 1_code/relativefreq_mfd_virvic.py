import pandas as pd

# Specify the file path
relativefreq_mfd_items_path = '/Users/kawaiyuen/nlpworkshop/concept-creep-chi/2_pipeline/preprocessed/relativefreq_mfd_items.csv'
# Read the CSV file
data = pd.read_csv(relativefreq_mfd_items_path)
# Extract the relevant column sets
harmvirtue_columns = data.iloc[:, 1:5]
harmvice_columns = data.iloc[:, 5:9]
fairnessvirtue_columns = data.iloc[:, 9:13]
fairnessvice_columns = data.iloc[:, 13:17]
ingroupvirtue_columns = data.iloc[:, 17:21]
ingroupvice_columns = data.iloc[:, 21:25]
authorityvirtue_columns = data.iloc[:, 25:29]
authorityvice_columns = data.iloc[:, 29:33]
purityvirtue_columns = data.iloc[:, 33:37]
purityvice_columns = data.iloc[:, 37:41]

# Calculate the mean values for each set of columns
harmvirtue_mean = harmvirtue_columns.mean(axis=1)
harmvice_mean = harmvice_columns.mean(axis=1)
fairnessvirtue_mean = fairnessvirtue_columns.mean(axis=1)
fairnessvice_mean = fairnessvice_columns.mean(axis=1)
ingroupvirtue_mean = ingroupvirtue_columns.mean(axis=1)
ingroupvice_mean = ingroupvice_columns.mean(axis=1)
authorityvirtue_mean = authorityvirtue_columns.mean(axis=1)
authorityvice_mean = authorityvice_columns.mean(axis=1)
purityvirtue_mean = purityvirtue_columns.mean(axis=1)
purityvice_mean = purityvice_columns.mean(axis=1)

# Assign labels to the calculated mean values
harmvirtue_mean.name = 'HarmVirtue'
harmvice_mean.name = 'HarmVice'
fairnessvirtue_mean.name = 'FairnessVirtue'
fairnessvice_mean.name = 'FairnessVice'
ingroupvirtue_mean.name = 'IngroupVirtue'
ingroupvice_mean.name = 'IngroupVice'
authorityvirtue_mean.name = 'AuthorityVirtue'
authorityvice_mean.name = 'AuthorityVice'
purityvirtue_mean.name = 'PurityVirtue'
purityvice_mean.name = 'PurityVice'

# Combine the mean values into a new DataFrame
mean_values = pd.concat([data['Year'], harmvirtue_mean, harmvice_mean, fairnessvirtue_mean, fairnessvice_mean, 
                         ingroupvirtue_mean,  ingroupvice_mean, authorityvirtue_mean, authorityvice_mean, 
                         purityvirtue_mean, purityvice_mean], axis=1)

# Save the mean values as a CSV file
output_dir = '/Users/kawaiyuen/nlpworkshop/concept-creep-chi/2_pipeline/tmp'
output_path = f'{output_dir}/realtivefreq_mfd_virvic.csv'
mean_values.to_csv(output_path, index=False)

print('Mean values saved successfully as a CSV file!')