import os
import urllib.request
import tarfile

BASE_URL = "https://ftp.ncbi.nlm.nih.gov/geo/series/GSE171nnn/GSE171524/suppl/"
FILES = ["GSE171524_RAW.tar"]
DATA_DIR = "../data"  # relative to scripts folder

# Make data folder
os.makedirs(DATA_DIR, exist_ok=True)

# Download each file
for filename in FILES:
    url = BASE_URL + filename
    out_path = os.path.join(DATA_DIR, filename)

    if os.path.exists(out_path):
        print(f"Already downloaded: {filename}")
    else:
        print(f"Downloading {filename} ...")
        urllib.request.urlretrieve(url, out_path)
        print("Done.")

# Extract .tar
print("Extracting files ...")
with tarfile.open(os.path.join(DATA_DIR, FILES[0]), "r") as tar:
    tar.extractall(path=DATA_DIR)
print("All done.")
