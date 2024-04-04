import os
import shutil



base_dir= "/Users/anushkasingh/Desktop/APR_1/code_for_cpg_embedding"

# Define paths
before_fix_features_dir = base_dir + "/output_data/cfg_and_pdg_features"
embeddings_dir = base_dir +'/output_data/ast_embeddings'
all_information_dir =  base_dir + '/output_data/all_information'

# Create the all_information directory if it doesn't exist
os.makedirs(all_information_dir, exist_ok=True)
print(f"Created directory: {all_information_dir}")

# Get the list of subdirectories in both directories
before_fix_features_subdirs = set(d for d in os.listdir(before_fix_features_dir) if os.path.isdir(os.path.join(before_fix_features_dir, d)))
embeddings_subdirs = set(d for d in os.listdir(embeddings_dir) if os.path.isdir(os.path.join(embeddings_dir, d)))

# Find the intersection of subdirectories
common_subdirs = before_fix_features_subdirs.intersection(embeddings_subdirs)

# Iterate over common subdirectories
for subdir in common_subdirs:
    # Create corresponding directory in all_information
    target_dir_path = os.path.join(all_information_dir, subdir)
    os.makedirs(target_dir_path, exist_ok=True)
    print(f"Created directory: {target_dir_path}")

    # Copy .dot files from before_fix_features to all_information
    source_dir_path = os.path.join(before_fix_features_dir, subdir)
    for filename in os.listdir(source_dir_path):
        source_file_path = os.path.join(source_dir_path, filename)
        if filename.endswith('.dot') and os.path.isfile(source_file_path):
            target_file_path = os.path.join(target_dir_path, filename)
            shutil.copy(source_file_path, target_file_path)
            print(f"Copied file: {source_file_path} to {target_file_path}")

    # Copy .txt files from embeddings to all_information
    source_dir_path = os.path.join(embeddings_dir, subdir)
    for filename in os.listdir(source_dir_path):
        source_file_path = os.path.join(source_dir_path, filename)
        if filename.endswith('.txt') and os.path.isfile(source_file_path):
            target_file_path = os.path.join(target_dir_path, filename)
            shutil.copy(source_file_path, target_file_path)
            print(f"Copied file: {source_file_path} to {target_file_path}")
