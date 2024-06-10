import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

primer_df = pd.read_csv("primer_sequences.csv")


# Visualizing the sequence on the basis of gc content
gc_data = primer_df.sort_values(by='GCContent', ascending=False)

# Filter sequences with GC content in the range 
selected_sequences = gc_data[(gc_data['GCContent'] >= 25) & (gc_data['GCContent'] <= 45)].head(10)
# Visualize selected sequences
plt.figure(figsize=(26, 8))
sns.barplot(x='GCContent', y='Sequence', data=selected_sequences)
plt.title('Top 10 Sequences with GC Content in the Range')
plt.xlabel('GC Content')
plt.ylabel('Sequence')
plt.show()
print(" ")