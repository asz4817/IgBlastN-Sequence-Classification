# Immunlogy Sequence Analysis Projects


## 1. IgBlastN Sequence Classification Project

This project aims to classify FASTA sequences into either human or mouse categories using IgBlastN. This project consists of two main Python scripts (one for running IgBlastN on human and mouse identities and extracting percent identities per sequence, and another to split the fasta file into 2 seperate fasta files based on their classification) and an Excel file aggregating the results of the first Python scripts and determining the identity of each sequence. 


#### seperate.py:
This code runs the entire program on the inputted fasta file to parse through every sequence and determine if it is a human or mouse sequence. The output of this code is two fasta files, KI and mVH, which contains only human and only mouse sequences from the original file respectively. 

#### human.py and mouse.py:
These codes will return a human_identities.csv or mouse_identities.csv, which you can then analyze in Excel. 
Pull the resulting list of identities you determin in Excel to a seperate csv to use in the next Python file. 


#### splitFasta.py:
This code will return two fasta files, one with only human sequences, and one with only mouse sequences. 
