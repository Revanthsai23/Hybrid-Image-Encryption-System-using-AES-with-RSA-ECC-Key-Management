 
# Image Encryption

## Overview

This project implements Image Encryption and Decryption service that integrates the
Advanced Encryption Standard (AES) with the user option to choose between RSA
(Rivest–Shamir–Adleman) and ECC (Elliptic-Curve Cryptography) for the encryption of
the master key. The service is capable of handling both color and grayscale images,
providing a secure, efficient approach to image encryption.

## Key Features
- **Dual Encryption Mechanism:** Primary encryption with AES and an additional layer of security where the user can choose between RSA or ECC for encrypting the AESmaster key.

- **Unique Identifier for Sessions:** Each encryption process generates a unique UUID, ensuring a secure and private decryption process.

- **Flexible File Formats:** Supports common image formats like JPG, PNG, and JPEG.

- **Highly Secure:** Incorporates RSA and ECC, two of the most secure public-key cryptographic algorithms, along with AES.

## Tech Stack
- Python
- OpenCV
- Fast API
- Unicorn


## Installation and Setup

### Setting up Conda Environment
- Create a new Conda environment
```
conda create --name image_encryption python=3.9
```
- Activate the environment
```
conda activate image_encryption
```

### Install the required packages
```
pip install -r requirements.txt
```

## Run the application
```
uvicorn main:app --host 0.0.0.0 --port 8000
```
**⚠ This is the process of running the app in the local system.**

### Usage

- Follow the on-screen instructions to encrypt and decrypt images. 

- Users can choose between RSA and ECC for the encryption of the AES master key.

