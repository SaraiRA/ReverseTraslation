import sys
from Bio import SeqIO

# Fasta sequence in a dictionary 
dictAA_Fasta = SeqIO.to_dict(SeqIO.parse(open("/aa.fasta"), "fasta"))
nucleotideFastaFile = open("nucleotide.fasta", "w")

# Define codon table
codonTable = { '*':'TAA',
    'I':'ATT', 'M':'ATG', 'T':'ACT', 
    'N':'AAT', 'K':'AAA', 'S':'TCT',
    'R':'AGA', 'L':'TTG', 'P':'CCA',
    'H':'CAT', 'Q':'CAA', 'V':'GTT', 
    'A':'GCT', 'C':'TGT', 'D':'GAT', 
    'E':'GAA', 'F':'TTT', 'G':'GGT', 
    'W':'TGG', 'Y':'TAT', }

for key,value in dictAA_Fasta.items():
    sequence_aa=str(dictAA_Fasta[key].seq)
    sequence_nn=""
    for aa in list(sequence_aa):
        if aa in codonTable:
            sequence_nn=sequence_nn+codonTable[aa]
    nucleotideFastaFile.write(">"+key + "\n" + sequence_nn + "\n" )
nucleotideFastaFile.close()

