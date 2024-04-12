import pandas as pd
import matplotlib.pyplot as plt

# Read the Excel file
df = pd.read_excel('/Users/kawaiyuen/nlpworkshop/concept-creep-chi/2_pipeline/tmp/main-3-final.xlsx')

# Specify the columns to be plotted
left_y_axis_column = '恐怖主义_Semantic_Breadth'
right_y_axis_columns = ['terrorism_care', 'terrorism_fair', 'terrorism_loya', 'terrorism_auth', 'terrorism_sanc']
right_y_axis_labels = ['harm', 'fairness', 'ingroup', 'authority', 'purity']
x_axis_column = 'Year'

# Create the figure and axis objects
fig, ax1 = plt.subplots()

# Plot the left y-axis column
ax1.plot(df[x_axis_column], df[left_y_axis_column], color='black', linewidth=1.2, label='prejudice')
ax1.set_xlabel(x_axis_column)
ax1.set_ylabel('Semantic Breadth')
ax1.legend(loc='lower left')

# Create the right y-axis
ax2 = ax1.twinx()

# Plot the right y-axis columns
for i, column in enumerate(right_y_axis_columns):
    ax2.plot(df[x_axis_column], df[column], color=f'C{i}', label=right_y_axis_labels[i], linewidth=.7, alpha=.7)
ax2.set_ylabel('Cosine Similarity')
ax2.legend(loc='upper right')

# Save the plot
output_path = '/Users/kawaiyuen/nlpworkshop/concept-creep-chi/3_output/cos-sim/terrorism.png'
plt.savefig(output_path, dpi=300)