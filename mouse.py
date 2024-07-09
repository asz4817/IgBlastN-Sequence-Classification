import sys
import subprocess
import pandas as pd
from io import StringIO
import os


def blastn_get_top_hits_mouse(query, path="/Users/amandazhang/Downloads/igblast-master"):
    """
    Function that parses the hits table from igblastn (bin/igblastn). The hits table shows the top identity to mouse sequences
    :param query: string, file path of the input fasta file
    :param path:  string, file path of igblast folder
    :return: df (dataframe of query and %identity mouse)
    """
    #changes the working directory to the downloaded igblast folder
    print("Beginning Mouse Igblastn")
    os.chdir(path)

    # command to run igblastn
    cmd = [f"{path}/bin/igblastn", '-germline_db_V', f'{path}/database/mouse_gl_V/mouse_gl_V_clean', '-germline_db_D', f'{path}/database/mouse_gl_D/mouse_gl_D_clean', '-germline_db_J', f'{path}/database/mouse_gl_J/mouse_gl_J_clean', '-organism', 'mouse',  '-query', query, '-auxiliary_data', f'{path}/optional_file/mouse_gl.aux', '-show_translation', '-outfmt', '3']

    a = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    stdout = a.communicate()[0].decode('utf-8')

    
    # Create a StringIO object from stdout
    b = StringIO(stdout)
    
    
    # Turn contents of b into a list
    all_data = [x.strip() for x in str(b.getvalue()).split('\n')]
    
    #Go through the output and match all of the queries to the %identity
    try:
        #hits dictionary stores the query as the key and identity as value
        print("Parsing through mouse results")
        hits = {}
        count = 0
        for line in all_data:
            if line.startswith('Query='):
                name = line.split('= ')[-1].strip()
                hits[name] = 0.0
                count = 1

            
            elif line.startswith("V ") and line[3].isdigit() and count == 1 :
                hits[name] = float(line.split()[1][:-1])
                count = 0
        print("Done parsing")
        # Convert data list into DataFrame        
        df = pd.DataFrame.from_dict(hits, orient='index', columns = ["% Identity"])
        return df
    

    except:
        print('None of the seuqenced you provided in the fasta file ')
        return None
    

# Calling Function
def main():
    #query = '/Users/amandazhang/Downloads/igblast-master/test.fasta'
    query = sys.argv[1]
    if len(sys.argv)>2:
        path = sys.argv[2]
        df = blastn_get_top_hits_mouse(query, path)
    else:
        df = blastn_get_top_hits_mouse(query)

    df.to_csv('mouse_identities.csv', index=True) 


if __name__=="__main__": 
    main() 
