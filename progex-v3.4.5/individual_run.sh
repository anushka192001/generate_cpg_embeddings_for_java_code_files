#!/bin/bash

base_dir="/Users/anushkasingh/Desktop/APR_1/code_for_cpg_embedding"

# Create directories if they don't exist
if [ ! -d "$base_dir/output_data/cfg_and_pdg_features" ]; then 
    mkdir -p "$base_dir/output_data/cfg_and_pdg_features"
fi 
             
if [ ! -d "$base_dir/output_data/input_dir" ]; then
    mkdir -p "$base_dir/output_data/input_dir"
fi 

# Loop through files 
for file in "$base_dir"/f2v-map-main/java-files/*; do    
    # Copy file to input directory
    cp "$file" "$base_dir/output_data/input_dir"
    
    # Extract filename without extension
    trimmed_file=$(basename "$file" | cut -d. -f1)
    
    # Create directory for file in 'before_fix_features' if it doesn't exist
    if [ ! -d "$base_dir/output_data/cfg_and_pdg_features/$trimmed_file" ]; then
        mkdir -p "$base_dir/output_data/cfg_and_pdg_features/$trimmed_file"
    fi
    
    # Run Java program (assuming input_dir is the input directory and before_fix_features/trimmed_file is the output directory)
    java -jar PROGEX.jar -cfg -ast -pdg -lang java -format dot -outdir "$base_dir/output_data/cfg_and_pdg_features/$trimmed_file" "$base_dir/output_data/input_dir/$(basename "$file")"
    
    # Remove file from input directory
    rm "$base_dir/output_data/input_dir/$(basename "$file")"
done
