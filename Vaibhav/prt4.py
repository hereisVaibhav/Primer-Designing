import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

primer_df = pd.read_csv("primer_sequences.csv")


# Filter sequences with SpecificTemp 
specific_temp = primer_df[primer_df['SpecificTemp'] == 50].head(10)   

#Sort the DataFrame
sorted = specific_temp.sort_values(by='SpecificTemp').head(10)
print(sorted)
# Visualize selected sequences
plt.figure(figsize=(26, 8))
sns.barplot(x='SpecificTemp', y='Sequence', data=sorted)
plt.title('Top 10 Sequences with min SpecificTemp in the Range')
plt.xlabel('SpecificTemp')
plt.ylabel('Sequence')
plt.show()
print(" ")








