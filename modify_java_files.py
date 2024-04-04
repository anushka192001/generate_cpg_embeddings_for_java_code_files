import os

base_path="/Users/anushkasingh/Desktop/APR_1/code_for_cpg_embedding/"

directory = base_path + "f2v-map-main/java-files" 
for filename in os.listdir(directory):
  file1 = open(directory + "/" + filename,'r')
  file_text = file1.read()
  text = "public class " + file_text.split('{')[0].split('(')[0].split()[-1].capitalize() + " " + "{" + "\n" + file_text + "\n" + "}"
  file1.close()

  file1 = open(directory + "/" + filename,'w')
  file1.write(text)
  file1.close() 

