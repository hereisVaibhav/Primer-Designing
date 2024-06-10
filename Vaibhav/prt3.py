import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

primer_df = pd.read_csv("primer_sequences.csv")

# Filter sequences with TotalLength equal to 21
sequences_length_21 = primer_df[primer_df['TotalLength'] == 21].head(10)

# Sort the filtered DataFrame by TotalLength
sorted_sequences = sequences_length_21.sort_values(by='TotalLength').head(10)
print(sorted_sequences)
# Visualize selected sequences
plt.figure(figsize=(26, 8))
sns.barplot(x='TotalLength', y='Sequence', data=sorted_sequences)
plt.title('Top 10 Sequences with min TotaLength Content in the Range')
plt.xlabel('TotalLength')
plt.ylabel('Sequence')
plt.show()
print(" ")