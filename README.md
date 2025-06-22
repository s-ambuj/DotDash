# DotDash

DotDash is a simple encryption and decryption tool that allows users to encrypt and decrypt messages using the Caesar Cipher technique (Morse code). This tool provides a user-friendly graphical interface (GUI) built with Python's `tkinter` library.

## Features

- **Encrypt**: Enter a plaintext message and encrypt it to Morse code.
- **Decrypt**: Enter an encrypted Morse code message and convert it back to the original text.
- **Graphical User Interface**: Easy-to-use interface with clearly defined input and output areas.

## Installation

### Prerequisites

1. **Python**: This tool is written in Python 3.x.
   - If you haven't installed Python, you can download it from [here](https://www.python.org/downloads/).

2. **Tkinter**: The `tkinter` library is included by default with Python 3.x installations. If it's not available, you can install it separately:

   ```bash
   pip install tk

    Additional Libraries: This tool uses custom encryption and decryption modules (encrypt.py, decrypt.py). These should be included in the repo.

Installation Steps

    Clone the repository to your local machine:
    git clone https://github.com/sambuj/DotDash.git

Navigate to the project directory:

    cd DotDash

Run the main GUI:

    python gui.py

Usage

    Encrypting a Message:

        Type your plaintext message into the "USER INPUT" field.

        Press the Encrypt button.

        The encrypted Morse code will appear in the "OUTPUT" field.

    Decrypting a Message:

        Enter the encrypted Morse code into the "USER INPUT" field.

        Press the Decrypt button.

        The original message will appear in the "OUTPUT" field.
