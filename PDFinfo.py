#!/usr/bin/env python
# coding: utf-8

''' PDFinfo v1.0 by rjb-21 returns various information about PDF documents '''


import PyPDF2
import os


print("\nPDFinfo v1.0 by rjb-21 returns various information about PDF documents")


while True:
    try:
        filePath = input("Enter file path: ")
        file = open(filePath,'rb')
    except:
        print('An error occurred! Please try again!')
        continue
    else:
        break


# Create pdfReader
pdfReader = PyPDF2.PdfFileReader(file)


# Number of pages
numPages = pdfReader.numPages
numPages


pdfTextList =[]

for num in range(numPages):
    
    page = pdfReader.getPage(num)
    
    pdfTextList.append(page.extractText())


pdfText = ''
pdfText = pdfText.join(pdfTextList)


numLetters = len(pdfText)
numWords = len(pdfText.split())


fileSize = os.path.getsize(filePath) / 1024
fileSizeRound = round(fileSize, 2)

fileName = os.path.basename(filePath)

# Print info
info = f"\nResults: \nFile name: {fileName} \nFile size(kB): {fileSizeRound} \nNumber of characters: {numLetters} \nNumber of words: {numWords} \n"
print(info)


file.close()
