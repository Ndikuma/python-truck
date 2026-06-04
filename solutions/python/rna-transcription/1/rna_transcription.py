def to_rna(dna_strand):
    """Translate a DNA strand into its complementary RNA strand."""
    # 1. Create a translation table mapping DNA nucleotides to RNA nucleotides
    dna_to_rna_table = str.maketrans("GCTA", "CGAU")
    
    # 2. Apply the mapping directly to the input string
    return dna_strand.translate(dna_to_rna_table)