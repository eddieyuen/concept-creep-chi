import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
df = pd.read_excel('/Users/kawaiyuen/nlpworkshop/concept-creep-chi/2_pipeline/MAIN-FULL_sb-win-size-5.xlsx')

# Extract the data for the moral foundations
foundations = ['Harm', 'Fairness', 'Ingroup', 'Authority', 'Purity']
data = df[foundations]

# Calculate the moving average with window size = 5
moving_avg_data = data.rolling(window=5, min_periods=1, center=True).mean()

# Plotting the data
plt.figure(figsize=(10, 8))

# Define a list of colors to use for the line plots
colors = plt.rcParams['axes.prop_cycle'].by_key()['color']

for i, foundation in enumerate(foundations):
    plt.plot(df['Year'], data[foundation],  alpha=0.7, linewidth=0.6, linestyle='dashed', color=colors[i])  # Plotting the moving average lines 
    plt.plot(df['Year'], moving_avg_data[foundation], label=foundation, linewidth=2, color=colors[i])  # Plotting the original lines

plt.xlabel('Year')
plt.ylabel('Relative Frequency')
plt.title('Cultural Salience of Moral Foundations Over Time (Moving Average Window = 5)')
plt.legend()

# Save the plot
plt.savefig('/Users/kawaiyuen/nlpworkshop/concept-creep-chi/3_output/relativefreq/cultural-salience_cmfd_five_moving-avg.png', dpi=300)

print('Plot saved')