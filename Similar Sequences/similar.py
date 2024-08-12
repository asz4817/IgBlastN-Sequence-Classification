from Bio import pairwise2 as pw2, SeqIO
import sys



def similar(path, file):
    HM = open(f"{path}/HM {file}", "w")
    with open("HM IgG2-ABSM1-37.fasta", "r") as f:
        seq = []
        for record in SeqIO.parse(f, "fasta"):
            seq.append(record.seq)
    with open(f"{path}/{file}", "r") as f:
        count=0
        for record in SeqIO.parse(f, "fasta"):
            match = False
            for f_seq in seq:
                count+=1
                global_align = pw2.align.globalxx(f_seq, record.seq)
                seq_length = min(len(f_seq), len(record.seq))
                matches = global_align[0][2]
                percent_match = (matches / seq_length) * 100
                if percent_match > 80:
                    match = True
            if match:
                SeqIO.write(record, HM, "fasta-2line")
            
        

def main():
    similar(sys.argv[1], sys.argv[2])


if __name__=="__main__":
    main()


