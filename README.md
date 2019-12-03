# CapstoneProjectIV
Software Engineering Boot Camp - Task 25

Compulsory Task 1
Follow these steps:
● Visit the website: http://www.cbs.dtu.dk/courses/27619/codon.html
● Note the 'SLC' code for each Amino Acid.
● Create a program called, ‘SickleCellDisease.py’. You will simulate the effects of the
Single Nucleotide Polymorphism that leads to this genetic disease.
● Write a function called ‘translate’ that, when given a DNA sequence of arbitrary length,
the program identifies and returns the amino acid sequence of the DNA using the
amino acid SLC code found in that table.
E.g DNA Input: ATTATTATT
Output: III (representing: Isoleucine, Isoleucine, Isoleucine )
● There are many different amino acids, so this may get a bit repetitive. Just do the first
five Amino Acids (i.e I, L, V, F M) and make any other codon be printed as the amino
acid 'X' . So basically, you would use an if - elif - elif .... else structure to translate each
codon of DNA into the correct Amino Acid.
● Note that the program must be able to handle DNA sequences that are not of a length
divisible by 3.
● Hint:
len(DNA) - (Will return the length of a String)
DNA[0:3] - (Will get the first 3 characters of the string stored in DNA num = 3)
DNA[0:num] - (This will work too!)

Compulsory Task 2
Follow these steps:
● Add another function to the program SickleCellDisease.py called 'mutate'. This function
must read the contents of the text file named 'DNA.txt'. It must then identify the first
occurrence of the lowercase letter 'a' in 'DNA.txt'.
● You must then write two new text files, one named normalDNA.txt and the other
named mutatedDNA.txt.
● The file normalDNA.txt must have the same DNA sequence as DNA.txt with the 'a'
changed to an 'A'.
● The file mutatedDNA.txt must have the same DNA sequence as DNA.txt with the 'a'
changed to a 'T'.
● Now create a new function, ‘txtTranslate’, that calls the translate function that you
wrote in Task 1, to take in text file input.
● Call it on both mutatedDNA.txt and normalDNA.txt, and output both Amino Acid
sequences to the user.
