# generate_cpg_embeddings_for_java_code_files
this project generates cpg embeddings of each java code file by extracting graph like information from each of the java code files.  it uses ast_embeddings of each line as vertices and cfg and pdg  relation between each of these lines as edges. for further information  please follow  .readme file.


These steps provide cpg embeddings of java files by keeping ast,cfg and
pdg information in itself.

idea-> uses graph like information of each java code file in which vertices are ast embeddings
of each line of java code and edges are cfg and pdg_ctrl,pdg_data relations between each of
these lines.

data-> already some of the sample data is inside
“code_for_cpg_embedding/already_generated_data” folder
embeddings.pt: contains final cpg embeddings of each java file




follow theseSteps to get the cpg embeddings—
1. Update the base paths in scripts:
base path = where you have downloaded this repository
a.) in (code_for_cpg_embeddings->modify_java_files.py) update your base_path
variable.
b.)in (code_for_cpg_embedding->progex-v3.4.5->individual_run.sh) update you
base_dir to base path.
c.)in (code_for_cpg_embeddings->f2v-map-main->rearrange_embeddings.py)
update your_base_path to your base path.
d.) in (code_for_cpg_embeddings->rearrange_all_information) update you
base_dir to your base path
e.) in
(code_for_cpg_embeddings->creating_cpg_embedding_using_ast_cfg_and_pdg.
ipynb) update your base dir.
……………………………………………………………………………………………………………

2: add you input java files to
“code_for_cpg_embedding/f2v-map-main/java-files” folder (it already contain some java files for
demo you can remove them and add yours)
warning: Java file must be inside a class to get the embeddings successfully else it will cause
error.

Right format if  function is inside a class

Wrong format if  function is not inside a class
So to resolve this error i wrote a separate script to wrap these code files inside a class
(code_for_cpg_embeddings->modify_java_files.py)
If needed, just add your files first according to step 1 and then on terminal just go to
code_for_cpg_embeddings directory and
run “python modify_java_script.py”
…………………………………………………………………………………………….

3: Now get cfg and pdg information of java files in dot format by just following this step.
a.)make sure you have Java Runtime Environment (JRE, version 8 or newer) installed in
your system
b.) now go to
(code_for_cpg_embedding->progex-v3.4.5) on terminal and run “./individual_run.sh”
It will generate a folder inside (code_for_cpg_embedding->output_data) named
“cfg_and_pdg_features” (each subfolder corresponding to java file contains 4 dot files
which contains cfg and pdg information)
………………………………………………………………………………………………….

4. Now get ast embeddings of each line using fold2vec library,
a.)make sure you have docker engine installed in you machine if not then install docker
desktop for linux in your machine (it contains docker engine also)
b.)make sure data folder is empty inside f2v-map-main folder
, just go to (code_for_cpg_embeddings->f2v-map-main) on terminal and run:
“make data/f2vmap.jsonl”
it will use this docker image to install necessary packages and codes to use fod2vec
library and will create a file inside data folder.
c.)now inside this (code_for_cpg_embeddings->f2v-map-main) on terminal,just run:
“python rearrange_embeddings.py”
It will rearrange the embeddings in separate folder for each java file and generate
embeddings by generating a folder inside (code_for_cpg_embedding->output_data)
named “ast_embeddings”
………………………………………………………………………………………………………

5. as some ast_embeddings folder or cfg_cpg_feature folder are missing for some java
files so keep only those java files which contain pdg,cfg edges and ast embedding
vertex information, so for this get a combined folder corresponding to each java file to
contain all these cfg,pdg dot files and ast embedding txt files.
a.) just go to (code_for_cpg_embeddings) and run on terminal:
“python rearrange_all_information.py”
(it will create folder named “all_information” inside the output_data folder.
..........................................
   
6. Now you have ast embeddings for each line as vertices and cfg and pdg edges in dot
file now use them and create cpg embeddings for each of the java files.
a.) now open “creating_cpg_embedding_using_ast_cfg_and_pdg.ipynb” in your code
editor and run this file to get your desired embeddings and it will also save embeddings
in your same “output_data” folder as “embeddings.pt”
…………………………………………………………………………………………………….
