import gdown
import os
import patoolib

# Create the test directory if it doesn't exist
if not os.path.exists("./datasets"):
    os.makedirs("./datasets")

# DIDA dataset download link
url = f"https://drive.google.com/uc?id=1d-U-lxIoS5QuPEYPvHA2-Bm4pULsTb06"

# Download the file
gdown.download(url, "./datasets/DIDA.rar")

# Uncompress the downloaded file
patoolib.extract_archive("./datasets/DIDA.rar", outdir="./datasets/")

# Rename the extracted folder
os.rename("./datasets/10000", "./datasets/DIDA")

# Remove the rar file after extraction
os.remove("./datasets/DIDA.rar")
