# Compulsory Task 2

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
    i1 = ['A', 'T', 'T']
    i2 = ['A', 'T', 'C']
    i3 = ['A', 'T', 'A']

    l1 = ['C', 'T', 'T']
    l2 = ['C', 'T', 'C']
    l3 = ['C', 'T', 'A']
    l4 = ['C', 'T', 'G']
    l5 = ['T', 'T', 'A']
    l6 = ['T', 'T', 'G']

    v1 = ['G', 'T', 'T']
    v2 = ['G', 'T', 'C']
    v3 = ['G', 'T', 'A']
    v4 = ['G', 'T', 'G']

    f1 = ['T', 'T', 'T']
    f2 = ['T', 'T', 'C']

    m1 = ['A', 'T', 'G']

    # Defining a variable that will append each amino acid as the program runs
    all_amino_acids = ''

    # This loop will run for the number of codons determined above
    # It reads three consecutive letters and then runs through the if statements to find the corresponding amino acid.
    for i in range(0, int(num_codon)):
        codon = dna_split[start:stop]
        if codon == i1 or codon == i2 or codon == i3:
            amino_acid = 'Isoleucine'
        elif codon == l1 or codon == l2 or codon == l3 or codon == l4 or codon == l5 or codon == l6:
            amino_acid = 'Leucine'
        elif codon == v1 or codon == v2 or codon == v3 or codon == v4:
            amino_acid = 'Valine'
        elif codon == f1 or codon == f2:
            amino_acid = 'Phenylanine'
        elif codon == m1:
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

# Defining function mutate
def mutate():

    # This opens the DNA txt file for reading only
    get_dna = open('DNA.txt', 'r')
    # This opens the file that the program will write to and enters a blank string to overwrite the file
    normal_dna_file = open('normalDNA.txt', 'w')
    normal_dna_file.write('')
    normal_dna_file.close()

    # This loop runs for every line in the DNA txt file and makes a list of the letters in that line
    for line in get_dna:
        dna_string = ''
        dna_string = dna_string + line
        dna_string = dna_string.replace('', ' ')
        dna_string = dna_string.split()

        # Determines the length of the line
        dna_length = len(dna_string)

        # Declares an empty string
        translated_string = ''

        # This runs for each letter in the line
        # Each letter is defined as the variable nucleotide and if this variable is equal to 'a' it is updated to 'A'
        for i in range(0, dna_length):
            nucleotide = dna_string[i]
            if nucleotide == 'a':
                nucleotide = 'A'

            # This rewrites the line with the changes made to any 'a'.
            translated_string = translated_string + '' + nucleotide

        # This reopens the now blank file and writes the translated string to it
        normal_dna_file = open('normalDNA.txt', 'a')
        normal_dna_file.write(translated_string + '\n')
        normal_dna_file.close()

    # This opens the file that the program will write to and enters a blank string to overwrite the file
    get_dna = open('DNA.txt', 'r')
    mutated_dna_file = open('mutatedDNA.txt', 'w')
    mutated_dna_file.write('')
    mutated_dna_file.close()

    # This loop runs for every line in the DNA txt file and makes a list of the letters in that line
    for line in get_dna:
        dna_string = ''
        dna_string = dna_string + line
        dna_string = dna_string.replace('', ' ')
        dna_string = dna_string.split()

        # Determines the length of the line
        dna_length = len(dna_string)

        # Declares an empty string
        translated_string = ''

        # This runs for each letter in the line
        # Each letter is defined as the variable nucleotide and if this variable is equal to 'a' it is updated to 'T'
        for i in range(0, dna_length):
            nucleotide = dna_string[i]
            if nucleotide == 'a':
                nucleotide = 'T'

            # This rewrites the line with the changes made to any 'a'
            translated_string = translated_string + '' + nucleotide

        # This reopens the now blank file and writes the translated string to it
        mutated_dna_file = open('mutatedDNA.txt', 'a')
        mutated_dna_file.write(translated_string + '\n')
        mutated_dna_file.close()

    # This closes the DNA txt file
    get_dna.close()

# Calls the mutate function
mutate()

# Defines a function that fetches a specified file for reading and then runs each line through the translate function
def txt_translate(file_name):
    dna_file = open(file_name, 'r')
    for line in dna_file:
        get_file_dna = line
        translate(get_file_dna)

# Calls the translate function for both the normal and mutated DNA files
txt_translate('mutatedDNA.txt')
txt_translate('normalDNA.txt')
