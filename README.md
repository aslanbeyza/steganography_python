# Stenography 🤫
🔗 [Medium Üzerinde Okuyun: Görsellerle Mesaj Gizleme – Python ile Steganografi](https://medium.com/@aslanbeyza3413/g%C3%B6rsellerle-mesaj-gizleme-python-ile-steganografi-uygulamas%C4%B1-b7110a75bf9b)
### What is Stenography?
Stenography is the practice of concealing one piece of information (text, image, audio, etc.) within another. Its primary goal is to **hide the existence** of the hidden data.

For example, embedding a secret message into an image file in such a way that it's not visible from the outside is a typical application of stenography.

Stenography is often used for **covert communication** and plays a significant role in **cybersecurity**, **digital forensics**, and **data surveillance**.

The hidden information is typically embedded in:

- 👾 The pixel data of an image 
- 🔊The frequency components of an audio file  
- 🎥 Or the frames of a video
# 🛠️ Installation & Usage Guide

## ✅ Requirements

### 1. Environment
- Make sure **Python** is installed (e.g., Python 3.10+)
- Required library: `Pillow`

### 2. Virtual Environment (Optional but Recommended)

```bash
python -m venv venv
source venv/bin/activate      # (Mac/Linux)
# or
venv\Scripts\activate         # (Windows)
pip install -r requirements.txt
pip install pillow
python encode.py
✅ Message successfully embedded into 'encoded_image.png'
python decode.py
✅ Decoded message: Hello World!
