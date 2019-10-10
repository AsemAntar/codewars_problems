# Author: Asem Antar
# problem : return he complement of a given string in a DNA strand
#           A --> T , C --> G


#######################################################################################
# my solution
#######################################################################################
def DNA_strand(dna):
    """
    dna: input string containing DNA genes in uppercase
    complement: is a dictionary containg the complement of each gene
                A --> T, C --> G
    output : the returned result after concatenating complementaries
    """
    output = ''
    complement = {'A': 'T', 'C': 'G'}
    for s in dna:
        for k, v in complement.items():
            if s == k:
                output += v
            if s == v:
                output += k

    return output


#######################################################################################
# better solution i learned
#######################################################################################
def DNA_strand_better_sol(dna):
    return ''.join([{'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}[l] for l in dna])


# print(DNA_strand_better_sol('AAAA'))
