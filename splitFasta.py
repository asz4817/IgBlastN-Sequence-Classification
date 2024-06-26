import csv
import os
import sys

def splitFasta(type_of_seq, path, data_file):
    '''
    Function that parses the fasta file as well as the matching csv with identities listed (human, mouse, or none - removed)
        and splits the given fasta file into two fasta files, one of all human and one of all mouse sequences. 
    :param type_of_seq: string, full file path to the csv file with the identities listed
    :param path:  string, file path to the working directory
    :param data_file: string, relative file path to the specific fasta file (from the path var)
    :return: None
    '''
    
    os.chdir(path)
    # parse the types of sequences csv into an ordered list
    action = []
    with open(type_of_seq) as f:
        for line in f:
            action.append(line.strip())
    action = action[1:]

    # store the fasta lines into another list
    data = []
    with open(f"{path}/{data_file}", "r") as f:
        count = 1
        for line in f:
            if count % 2:
                seq = line
                count += 1
            else:
                seq += line
                data.append(seq)
                count += 1

    #open the resulting human and mouse files
    human = open(f"{path}/KI {data_file}", "w")
    mouse = open(f"{path}/mVH {data_file}", "w")

    #based on the action, split the data
    for i, seq in enumerate(data):
        if action[i] == "mouse":
            mouse.write(seq)
        elif action[i] == "human":
            human.write(seq)
    human.close()
    mouse.close()

#Calling the function
#splitFasta('/Users/amandazhang/Downloads/igblast-master/Final Sequences/type_of_seq.csv', "/Users/amandazhang/Downloads/igblast-master/Final Sequences/G3 CE137", "IgG23-ABSM1-37 copy.fasta")
splitFasta(sys.argv[1], sys.argv[2], sys.argv[3])