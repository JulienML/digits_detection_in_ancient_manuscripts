import gdown
import os
import patoolib

# Create the test directory if it doesn't exist
if not os.path.exists("./test"):
    os.makedirs("./test")

# DIDA dataset download link
url = f"https://drive.google.com/uc?id=1d-U-lxIoS5QuPEYPvHA2-Bm4pULsTb06"

# Download the file
gdown.download(url, "./test/DIDA.rar")

# Uncompress the downloaded file
patoolib.extract_archive("./test/DIDA.rar", outdir="./test/")

# Rename the extracted folder
os.rename("./test/10000", "./test/DIDA")

# Remove the rar file after extraction
os.remove("./test/DIDA.rar")
