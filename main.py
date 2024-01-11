# /path/to/main.py
import pyttsx3
import PyPDF2

def extract_text_from_pdf(pdf_path):
    """
    Extrahiert den Text aus einer PDF-Datei.
    :param pdf_path: Pfad zur PDF-Datei
    :return: Gesamter Text der PDF als String
    """
    text = ""
    with open(pdf_path, 'rb') as file:
        pdfreader = PyPDF2.PdfReader(file)
        for page_num in range(len(pdfreader.pages)):
            text += pdfreader.pages[page_num].extract_text() + " "
    return text

def convert_text_to_speech(text, mp3_path):
    """
    Konvertiert Text in Sprache und speichert ihn als MP3-Datei.
    :param text: Text zum Umwandeln
    :param mp3_path: Pfad, wo die MP3-Datei gespeichert wird
    """
    speaker = pyttsx3.init()
    speaker.save_to_file(text, mp3_path)
    speaker.runAndWait()
    speaker.stop()

def main():
    """
    Hauptfunktion zum Ausführen des Skripts.
    """
    pdf_path = 'book.pdf'
    mp3_path = 'book.mp3'

    text = extract_text_from_pdf(pdf_path)
    convert_text_to_speech(text, mp3_path)
    print(f"PDF '{pdf_path}' wurde erfolgreich in '{mp3_path}' umgewandelt.")

if __name__ == "__main__":
    main()
