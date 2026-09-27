import os
import nbformat as nbf
from nbconvert.preprocessors import ExecutePreprocessor

notebook_path = os.path.join('notebooks', 'Unified Notebook', '01_End_to_End_Unified_Pipeline.ipynb')
print(f"Reading notebook from: {notebook_path}")

with open(notebook_path, 'r', encoding='utf-8') as f:
    nb = nbf.read(f, as_version=4)

print("Executing notebook end-to-end via ExecutePreprocessor...")
ep = ExecutePreprocessor(timeout=600, kernel_name='python3')

try:
    ep.preprocess(nb, {'metadata': {'path': os.path.dirname(notebook_path)}})
    print("Notebook executed successfully without errors!")
except Exception as e:
    print(f"Execution encountered an error: {e}")
    raise e

with open(notebook_path, 'w', encoding='utf-8') as f:
    nbf.write(nb, f)

print(f"Executed notebook saved with all outputs to: {notebook_path}")
