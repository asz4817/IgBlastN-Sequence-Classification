# Immunlogy Sequence Analysis Projects


## 1. IgBlastN Sequence Classification Project

This project aims to classify FASTA sequences into either human or mouse categories using IgBlastN. This project consists of two main Python scripts (one for running IgBlastN on human and mouse identities and extracting percent identities per sequence, and another to split the fasta file into 2 seperate fasta files based on their classification) and an Excel file aggregating the results of the first Python scripts and determining the identity of each sequence. 


#### separate.py:
This program combines the code written in human.py, mouse.py, and splitFast.py to parse through every sequence of the inputted fasta file and determine if the sequence corresponds to human or mouse DNA. The output of this code is two fasta files, KI and mVH, which contains only human and only mouse sequences from the original file respectively. 

#### human.py and mouse.py:
These codes will return a human_identities.csv or mouse_identities.csv, which you can then analyze in Excel. 
Pull the resulting list of identities you determine in Excel to a seperate csv to use in the next Python file. 


#### splitFasta.py:
This code will return two fasta files, one with only human sequences, and one with only mouse sequences. 


## 2. Similar Sequences

This project aims to find sequences in the Ig fastsa files that are 80% or more similar to one of the 4 sequences provided in the HM file. The output of running this program is an additional "HM ..." fasta file consisting of only similar sequences. 


## 3. removeN.py

This project parses the KI fasta file and removes any sequences with missing data from positions 21-420. Those without any missing data will be copied into the new outputted file, the KI-N fasta file. 
