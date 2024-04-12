#T. Pires - PDF_Splitter.py
#Created: 2024-03-13 - Last Updated: 2024-03-13

import os
from PyPDF2 import PdfWriter, PdfReader

def main():
    
    continueInput = input("\nPlease ensure the PDF you want to use is in the same file as PDF_Splitter.py. Press enter to continue...")
    fileName = input("\nEnter the filename: ")

    try:
        pdfInstance = PdfReader(open(fileName, "rb"))
    except:
        print("\nError: File not found. Please ensure the file is in the same file as PDF_Splitter.py and follows the input format [filename.pdf]...")
        exit()
    
    for page in range(len(pdfInstance.pages)):
        
        pdfPage = PdfWriter()
        
        pdfPage.add_page(pdfInstance.pages[page])
        
        if(page + 1 < 10):
            with open(f"{fileName[0:-4]}_Page0{page + 1}.pdf", "wb") as outputPdfPage:
                pdfPage.write(outputPdfPage)
        else:
            with open(f"{fileName[0:-4]}_Page{page + 1}.pdf", "wb") as outputPdfPage:
                pdfPage.write(outputPdfPage)
            
    print("PDF successfully split!")

    
    
if __name__ == "__main__":
    main()