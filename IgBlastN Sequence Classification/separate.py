import sys
import human as h
import mouse as m
import splitFasta as sF
import numpy as np


def determineOrganism(query, path="/Users/amandazhang/Downloads/igblast-master"):
    '''Function that runs the human and mouse igblastn and determine whether sequence is mouse, human, or neither
    :param query: string, file path of the input fasta file
    :param path:  string, file path of igblast folder
    :return: type_of_seq, list of whether each sequence (in order of query sequence) is mouse, human, or neither
    '''
    humans = h.blastn_get_top_hits_human(query, path)
    mouses = m.blastn_get_top_hits_mouse(query, path)

    humans = humans.iloc[:, 0].values
    mouses = mouses.iloc[:, 0].values

    print("human length:", len(humans))
    print("mouse length:", len(mouses))

    type_of_seq = []
    for idx, hIdentity in enumerate(humans):
        if mouses[idx] > hIdentity and mouses[idx] > 85:
            type_of_seq.append("mouse")
        elif hIdentity<50 and mouses[idx]<50:
            type_of_seq.append("")
        else:
            type_of_seq.append("human")

    print("Query Length:", len(type_of_seq))
    
    return np.array(type_of_seq)
    


#Calling the function
def main():
    #inputs - fasta file
    path = sys.argv[1]
    data_file = sys.argv[2]
    query = path + "/" + data_file


    #Determine the actions to perform on the fasta file
    type_of_seq = determineOrganism(query)

    print("Splitting Fasta")
    #Split the original Fasta file into KI and mVH files
    sF.splitFasta(type_of_seq, path, data_file)

    print("Done")

if __name__=="__main__": 
    main() 
