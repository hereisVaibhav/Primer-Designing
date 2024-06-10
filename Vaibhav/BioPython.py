import pandas as pd
from Bio.SeqUtils import MeltingTemp as mt
from Bio.Seq import Seq

# Define the sequence and its properties (Homo sapiens sex hormone binding globulin (SHBG) mRNA, exons 1L through 3, 8 and partial cds, alternatively spliced)
mRNA_sequence = '''TGGGCCCTGAGACCTGTTCTCCCCACCCAGAGTGCCCACGACCCTCCGGCTGTCCACCTCAGCAATGGCC
                   CAGGACAAGAGCCTATCGCTGTCATGACCTTTGACCTCACCAAGATCACAAAAACCTCCTCCTCCTTTGA
                   GGTTCGAACCTGGGACCCAGAGGGAGTGATTTTTTATGGGGATACCAACCCTAAGGATGACTGGTTTATG
                   CTGGGACTTCGAGACGGCAGGCCTGAGATCCAACTGCACAATCACTGGGCCCAGCTTACGGTGGGTGCTG
                   GACCACGGCTGGATGATGGGAGATGGCACCAGGAGAAGACTCTTCCACCTCTTTTTGCCTGAATGGCCTT
                   TGGGCACAAGGTCAGAGGCTGGATGTGGACCAGGCCCTGAACAGAAGCCATGAGATCTGGACTCACAGCT
                   GCCCCCAGAGCCCAGGCAATGGCACTGACGCTTCCCATTAAAG'''

primer_length_range = range(18, 23)  # Typical or set the length of the primers

# Remove spaces and newlines from mRNA_sequence
mRNA_sequence = ''.join(mRNA_sequence.split())

# Generate all possible sequences within the specified length range
primer_properties = []
for length in primer_length_range:
    for i in range(len(mRNA_sequence) - length + 1):
        seq = str(Seq(mRNA_sequence[i:i+length]))
        melting_temp = mt.Tm_NN(Seq(seq))       
        gc_content = (seq.count('G') + seq.count('C')) / len(seq) * 100
        primer_properties.append({'Sequence': seq, 'MeltingTemp': melting_temp, 'GCContent': gc_content, 'SpecificTemp': mt.Tm_Wallace(Seq(seq))})

# Create DataFrame
primer_df = pd.DataFrame(primer_properties)

# Calculate the minimum and maximum length of the sequences, and the minimum and maximum melting temperature
primer_df['TotalLength'] = primer_df['Sequence'].apply(len)
primer_df['MinLength'] = primer_df['Sequence'].apply(len).min()
primer_df['MaxLength'] = primer_df['Sequence'].apply(len).max()
primer_df['MinTemp'] = primer_df['MeltingTemp'].min()
primer_df['MaxTemp'] = primer_df['MeltingTemp'].max()
primer_df['TotalLength'] = primer_df['Sequence'].apply(len)
primer_df['SpecificTemp'] = primer_df['SpecificTemp']

# Display the updated DataFrame with the new columns
print(primer_df.head())


# This is for printing all the possible data for your sequence
print('Total number of possible sequences:', len(primer_df))
print(primer_df[['Sequence', 'MeltingTemp', 'MinTemp', 'MaxTemp', 'GCContent', 'MinLength', 'MaxLength', 'TotalLength', 'SpecificTemp']])


# To download the data set in csv (Comma Separated Value) formate
filename = 'primer_sequences.csv'
primer_df.to_csv(filename, index=False)

# Provide the file path for download
print('File saved as:', filename)


total_possible_sequences = sum(len(mRNA_sequence) - length + 1 for length in primer_length_range)
print(total_possible_sequences)
print(len(mRNA_sequence))







