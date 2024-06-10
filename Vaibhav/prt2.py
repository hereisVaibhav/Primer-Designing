import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

primer_df = pd.read_csv("primer_sequences.csv")


# Scatter plot of Melting Temperature vs GC Content
plt.figure(figsize=(10, 6))
plt.scatter(primer_df['GCContent'], primer_df['MeltingTemp'], alpha=0.5,  c="red")
plt.title('Melting Temperature vs GC Content')
plt.xlabel('GC Content')
plt.ylabel('Melting Temperature (Tm)')
plt.show()
print(" ")











