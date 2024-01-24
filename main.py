# /path/to/main.py
import pyttsx3
import PyPDF2

def extract_text_from_pdf(pdf_path):
    """
    Extracts the text from a PDF file.
    :param pdf_path: Path to the PDF file
    :return: Entire text of the PDF as a string
    """
    text = ""
    with open(pdf_path, 'rb') as file:
        pdfreader = PyPDF2.PdfReader(file)
        for page_num in range(len(pdfreader.pages)):
            text += pdfreader.pages[page_num].extract_text() + " "
    return text

def convert_text_to_speech(text, mp3_path):
    """
    Converts text to speech and saves it as an MP3 file.
    :param text: Text to convert
    :param mp3_path: Path where the MP3 file is saved
    """
    speaker = pyttsx3.init()
    speaker.save_to_file(text, mp3_path)
    speaker.runAndWait()
    speaker.stop()

def main():
    """
    Main function for executing the script.
    """
    pdf_path = 'book.pdf'
    mp3_path = 'book.mp3'

    text = extract_text_from_pdf(pdf_path)
    convert_text_to_speech(text, mp3_path)
    print(f"PDF '{pdf_path}' was successfully converted to '{mp3_path}'")

if __name__ == "__main__":
    main()
