# Digits Detection in Ancient Manuscripts

This repository contains different approaches to detect digits in ancient manuscripts.

You can find the following approaches:
- **Object Detection Model**: Using YOLOv8. (See [test_with_yolo](test_with_yolo/README.md) for more details)
- **Optical Character Recognition**: Using Tesseract OCR. (See [test_with_tesseract](test_with_tesseract/README.md) for more details)

In order to be able to run the code, you need to install the required datasets and libraries. You can do this by running the following command:

```bash
pip install -r requirements.txt
python setup.py
```