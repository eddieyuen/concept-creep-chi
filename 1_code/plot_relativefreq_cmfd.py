import pandas as pd
import matplotlib.pyplot as plt

# Read the Excel file
df = pd.read_excel('/Users/kawaiyuen/nlpworkshop/concept-creep-chi/2_pipeline/MAIN-FULL_sb-win-size-5.xlsx')

# Extract the data for the moral foundations
foundations = ['Harm', 'Fairness', 'Ingroup', 'Authority', 'Purity']
data = df[foundations]

# Plotting the data
plt.figure(figsize=(10, 8))

for foundation in foundations:
    plt.plot(df['Year'], data[foundation], label=foundation)

plt.xlabel('Year')
plt.ylabel('Relative Frequency')
plt.title('Cultural Salience of Moral Foundations Over Time')
plt.legend()

# Save the plot
plt.savefig('/Users/kawaiyuen/nlpworkshop/concept-creep-chi/3_output/relativefreq/cultural-salience_cmfd_five.png', dpi=300)

print('Plot saved')