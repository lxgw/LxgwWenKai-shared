import glob
import zipfile
from pathlib import Path
import os, shutil, sys

input_path = sys.argv[1]
output_dir = sys.argv[2]

if os.path.exists(f"sources/temp/{output_dir}"):
    shutil.rmtree(f"sources/temp/{output_dir}")
os.makedirs(f"sources/temp/{output_dir}")
for ufo in Path(input_path).glob("*.ufoz"):
    with zipfile.ZipFile(ufo, 'r') as zip_ref:
        zip_ref.extractall(f"sources/temp/{output_dir}")