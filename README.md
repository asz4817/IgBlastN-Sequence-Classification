# IgBlastN Sequence Classification Project

This project aims to classify FASTA sequences into either human or mouse categories using IgBlastN. This project consists of two main Python scripts (one for running IgBlastN on human and mouse identities and extracting percent identities per sequence, and another to split the fasta file into 2 seperate fasta files based on their classification) and an Excel file aggregating the results of the first Python scripts and determining the identity of each sequence. 

## Requirements
- Python 3
- [Igblast](https://github.com/xinyu-dev/igblast/blob/master/Using%20IgBlast.ipynb) and corresponding databases 
- Terminal

### Usage
Navigate to correct directory in terminal
#### human.py and mouse.py:
```
python3 human.py query path
python3 mouse.py query path
```
query = path to the input fasta file
path = path to the IgBlast directory on your computer

These codes will return a human_identities.csv or mouse_identities.csv, which you can then analyze in Excel. 
Pull the resulting list of identities you determin in Excel to a seperate csv to use in the next Python file. 


#### splitFasta.py:
```
  python3 splitFasta.py type_of_seq path data_file
```
type_of_seq: The path to the CSV file containing the sequence classifications.  
path: The working directory path.
data_file: The relative file path to the specific fasta file (from the path var).

This code will return two fasta files, one with only human sequences, and one with only mouse sequences. 
