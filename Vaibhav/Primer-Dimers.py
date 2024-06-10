def check_primer_dimers(primer1, primer2, max_dimer_length=5):
    """
    Check for potential primer dimers between two primer sequences.
    
    Args:
    - primer1 (str): Sequence of the first primer.
    - primer2 (str): Sequence of the second primer.
    - max_dimer_length (int): Maximum length of the potential dimer.
    
    Returns:
    - dimer_positions (list): List of tuples containing start and end positions of potential dimers.
    """
    dimer_positions = []
    for i in range(len(primer1) - max_dimer_length + 1):
        for j in range(len(primer2) - max_dimer_length + 1):
            dimer1 = primer1[i:i+max_dimer_length]
            dimer2 = primer2[j:j+max_dimer_length]
            if dimer1 == dimer2[::-1]:
                dimer_positions.append((i, j))
    return dimer_positions

# Example usage:
primer1 = "ATCGATCG"
primer2 = "GATCGATC"
dimers = check_primer_dimers(primer1, primer2)
if dimers:
    print("Potential primer dimers found:")
    for dimer in dimers:
        print(f"Dimer positions: {dimer}")
else:
    print("No potential primer dimers found.")












    
