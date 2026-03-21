import json

# Read the notebook
notebook_path = '/Users/apoorv.apoorv/Downloads/Introduction_to_RAG.ipynb'

with open(notebook_path, 'r', encoding='utf-8') as f:
    notebook = json.load(f)

# Remove the problematic widgets metadata
if 'metadata' in notebook and 'widgets' in notebook['metadata']:
    print("Found 'widgets' in metadata. Removing it...")
    del notebook['metadata']['widgets']
    print("Successfully removed 'widgets' metadata.")
else:
    print("No 'widgets' metadata found.")

# Save the cleaned notebook
with open(notebook_path, 'w', encoding='utf-8') as f:
    json.dump(notebook, f, indent=2, ensure_ascii=False)

print(f"\nNotebook has been fixed and saved to: {notebook_path}")
print("You can now upload it to GitHub without errors!")
