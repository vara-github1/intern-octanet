import pyttsx3
import PyPDF2
from tkinter.filedialog import askopenfile

# Ask for the PDF file
book = askopenfile(filetypes=[("PDF files", "*.pdf")], mode='rb')
if book is not None:
    pdfreader = PyPDF2.PdfReader(book)
    pages = len(pdfreader.pages)

    for num in range(0, pages):
        page = pdfreader.pages[num]
        text = page.extract_text()
        player = pyttsx3.init()
        player.say(text)
        player.runAndWait()
