# Compulsory Task 1

# Defining a function called translate
def translate(dna):
    # This puts each letter (nucleotide) in a list.
    dna_space = dna.replace('', ' ')
    dna_split = dna_space.split()

    # The length of the list is determined
    # Then the number of existing codons is determined by dividing by 3
    num_codon = (len(dna_split))/3

    # These two variables will increment as the program runs through the loop so that the next three letters are read.
    start = 0
    stop = 3

    # These are variables that all define a specific amino acid
    I1 = ['A', 'T', 'T']
    I2 = ['A', 'T', 'C']
    I3 = ['A', 'T', 'A']

    L1 = ['C', 'T', 'T']
    L2 = ['C', 'T', 'C']
    L3 = ['C', 'T', 'A']
    L4 = ['C', 'T', 'G']
    L5 = ['T', 'T', 'A']
    L6 = ['T', 'T', 'G']

    V1 = ['G', 'T', 'T']
    V2 = ['G', 'T', 'C']
    V3 = ['G', 'T', 'A']
    V4 = ['G', 'T', 'G']

    F1 = ['T', 'T', 'T']
    F2 = ['T', 'T', 'C']

    M1 = ['A', 'T', 'G']

    # Defining a variable that will append each amino acid as the program runs
    all_amino_acids = ''

    # This loop will run for the number of codons determined above
    # It reads three consecutive letters and then runs through the if statements to find the corresponding amino acid.
    for i in range(0, int(num_codon)):
        codon = dna_split[start:stop]
        if codon == I1 or codon == I2 or codon == I3:
            amino_acid = 'Isoleucine'
        elif codon == L1 or codon == L2 or codon == L3 or codon == L4 or codon == L5 or codon == L6:
            amino_acid = 'Leucine'
        elif codon == V1 or codon == V2 or codon == V3 or codon == V4:
            amino_acid = 'Valine'
        elif codon == F1 or codon == F2:
            amino_acid = 'Phenylanine'
        elif codon == M1:
            amino_acid = 'Methionine'
        else:
            amino_acid = 'X'
            # Not all amino acids are listed so if there is a combination that the program
            # does not recognise then it will print an 'X'

        # The amino acid gets appended to the string variable defined above
        all_amino_acids = all_amino_acids + amino_acid + '\n'

        # The position variables are updated
        start += 3
        stop += 3

    # The program prints out each amino acid that the DNA codes for on a new line
    print('The amino acids present are: \n' + all_amino_acids)

# Here the function is called and the user is prompted to enter a string of DNA
dna_input = input('Enter your dna sequence here: ')
translate(dna_input)