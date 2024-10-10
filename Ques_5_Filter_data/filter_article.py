import os

# Folder paths
source_folder = 'text'  # Folder with text files
destination_folder = 'filter_text'  # Folder to store filtered files

# List of words to filter out
filter_words = [
  "scheibegal", "Fickdich", "Drecksau", "Bastard", "Hurensohn", "Hündin", "Verpiss dich", "Misthaufen",
    "Arschgeige", "Arschkriecher", "Miststück", "Spasti", "Ficker", "Wichser", "Spastike",
      "Beidl", "Neger"
]

# Create destination folder if it doesn't exist
os.makedirs(destination_folder, exist_ok=True)

# Function to check if a file contains any of the filter words
def contains_filter_word(file_content):
    for word in filter_words:
        if word in file_content:
            return True
    return False

# Read files from the source folder
for file_name in os.listdir(source_folder):
    if file_name.endswith(".txt"):
        file_path = os.path.join(source_folder, file_name)
        
        # Read the content of the file
        with open(file_path, 'r', encoding='utf-8') as file:
            file_content = file.read()
        print("hello")
        # Check if the file contains any of the filter words
        if not contains_filter_word(file_content):
            # If no filter words, copy the file to the destination folder
            print("hello")
            destination_file_path = os.path.join(destination_folder, file_name)
            with open(destination_file_path, 'w', encoding='utf-8') as destination_file:
                destination_file.write(file_content)

print("Filtering complete. Files without the specified words are stored in 'filter_text'.")
