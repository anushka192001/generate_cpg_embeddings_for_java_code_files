import os
import json

your_base_path= "/Users/anushkasingh/Desktop/APR_1/code_for_cpg_embedding"

if not os.path.exists(your_base_path+'/output_data/ast_embeddings'):
   os.mkdir(your_base_path+'/output_data/ast_embeddings') 


with open(your_base_path+'/f2v-map-main/data/f2vmap.jsonl', 'r') as json_file:
    json_list = list(json_file)

for json_str in json_list:
    result = json.loads(json_str)
    dir = result['path'].split('/')[3].split('.')[0]
    if not os.path.exists(your_base_path+'/output_data/ast_embeddings/' + dir):
       os.mkdir(your_base_path+'/output_data/ast_embeddings/' + dir)
    f = open(your_base_path+'/output_data/ast_embeddings/' + dir + '/embeddings.txt', 'a')
    f.write(json.dumps(result) + '\n')
    f.close  


