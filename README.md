# PDF to MP3 Converter

This repository contains a Python script that reads a PDF file and converts its text into an MP3 file. It utilizes PyPDF2 for extracting text from the PDF and pyttsx3 for text-to-speech conversion.

## Features

- Reads text from a PDF file (`book.pdf`).
- Converts the extracted text into a spoken MP3 file (`book.mp3`).

## Prerequisites

Before you can use the script, make sure you have Python installed on your computer. The script was developed and tested with Python 3.10.

## Installation

To use the script, first clone this repository:
git clone https://github.com/timomoebes/Pdf2Audio.git
cd Pdf2Audio


Then, install the required packages:
pip install PyPDF2 pyttsx3

Run the script from the repository directory:
python main.py

Ensure that the PDF file you wish to convert is in the same directory and named book.pdf.

Contributions are welcome! If you'd like to make an improvement or a bug fix, please create a pull request.

This project is licensed under the MIT License. Please refer to the license terms for using or distributing this software.
