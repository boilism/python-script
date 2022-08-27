import requests
import random
import time
import re
import pandas as pd
import numpy as np

df_protein_id = pd.read_excel("蛋白质序列(1).xlsx", usecols=[0])
#Read your own named protein id. If you don't have it then it's okay to delete the line

df_url = pd.read_excel("蛋白质序列(1).xlsx", usecols=[2])
#Read download URL for uniprot id

df_arr = np.asarray(df_url.stack())
urls = df_arr.tolist()
#Converting read content(url) to a list

df_arr_2 = np.asarray(df_protein_id.stack())
protein_id = df_arr_2.tolist()
#Converting read content(protein id that you named) to a list. If you don't have it then it's okay to delete the line

for url,pd in zip(urls,protein_id):
    #Loop the URL and id at the same time. if you dont have your named protein id, you could write as "for url in urls:

    time.sleep(random.uniform(1, 3))
    #The script will run randomly within 1-3 seconds

    seq_resp = requests.get(url)
    #Access links

    with open('seq.txt', 'ab') as f:
    #write the content in a txt file

        total_seq1 = seq_resp.content
        total_seq2 = total_seq1.decode('utf-8')
        #get the content of page and decode it

        new_head = re.findall(r'^>.*', total_seq2)
        #use re to get the head content

        new_head = ''.join(new_head)
        #convert the content from list to string

        final_seq = total_seq2.replace(new_head,pd).encode()
        #use your own protein id to the head content and encode it to byte

        f.write(final_seq)
        #write them in your txt file

        print('over!',url)
        #once a url is down, it will alert you

print('all over')
