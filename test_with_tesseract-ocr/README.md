# Optical Character Recognition (OCR) Approach with Tesseract OCR

In this folder, you can find the code to test Tesseract OCR on ancient manuscripts images, with and without fine-tuning.

The notebook [tesseract without fine-tuning.ipynb](./tesseract%20without%20fine-tuning.ipynb) uses the default Tesseract OCR model to detect digits in ancient manuscripts images.

The notebook [tesseract with fine-tuning.ipynb](./tesseract%20with%20fine-tuning.ipynb) train a custom Tesseract OCR model using the DIDA dataset and test it on ancient manuscripts images.
The folder [train_tesseract](./train_tesseract) is a copy of the [tesstrain](https://github.com/tesseract-ocr/tesstrain) repository. This project have been used to train the custom Tesseract OCR model.