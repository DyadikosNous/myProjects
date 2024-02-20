import PyPDF2

# Άνοιγμα PDF αρχείου σε Binary Mode
with open('example.pdf', 'rb') as file:
    pdf_reader = PyPDF2.PdfReader(file)
    # Δείξε τον αριθμό των σελίδων
    print(f"Number of pages: {len(pdf_reader.pages)}")
    i = 0
    # Όσο υπάρχουν σελίδες, κάνε εξαγωγή του περιεχομένου
    while i < len(pdf_reader.pages):
        page = pdf_reader.pages[i]
        text = page.extract_text()
        i += 1
        print(text)
