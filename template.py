import os
import logging
from pathlib import Path

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')


project_name = "GeminiTextExtract"


list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/components/extract_text.py",
    f"src/{project_name}/components/evaluate.py",
    f"src/{project_name}/config/configuration.py",
    f"notebooks/evaluation.ipynb",
    "data/raw/.gitkeep",
    "data/processed/.gitkeep",
    "data/results/.gitkeep",
    "models/gemini_model/.gitkeep",
    "scripts/extract_text.py",
    "scripts/evaluate.py",
    "tests/test_extraction.py",
    "requirements.txt",
    "setup.py",
    "README.md"
]

# Creating directories and files based on the list above
for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    # Ensure the directory exists
    if filedir:
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir}")

    # Create an empty file if it doesn't exist or is empty
    if not filepath.exists() or filepath.stat().st_size == 0:
        with open(filepath, "w") as f:
            pass
        logging.info(f"Creating empty file: {filepath}")

    # Log if the file already exists and isn't empty
    else:
        logging.info(f"File already exists: {filename}")

print("Project structure setup completed.")
