import os

# Define folders and files to be created
folders = [
    "project",
    "testing"
]

files = [
    "project/__init__.py",
    "project/main.py",
    "project/graph_builder.py",
    "project/handlers.py",
    "project/operators.py",
    "project/state.py",
    "testing/how_to_test.md",
    "README.md",
    "requirements.txt",
    ".env"
]

# Create folders
for folder in folders:
    os.makedirs(folder, exist_ok=True)
    print(f"Created folder: {folder}")

# Create files with placeholder content
for file in files:
    if not os.path.exists(file):
        with open(file, 'w') as f:
            f.write(f"# {file} - generated by template.py\n")
        print(f"Created file: {file}")
    else:
        print(f"File already exists: {file}")

print("\n✅ Project scaffolding complete!")
