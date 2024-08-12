'''Program to convert sequences written in fastq format to fasta'''

from Bio import SeqIO

with open("test.fastq") as input_handle:
    with open("results.fasta", "w") as output:
        sequences = SeqIO.parse(input_handle, "fastq")
        count = SeqIO.write(sequences, output, "fasta-2line")

print("Successfully converted %i records to fasta format" % count)
