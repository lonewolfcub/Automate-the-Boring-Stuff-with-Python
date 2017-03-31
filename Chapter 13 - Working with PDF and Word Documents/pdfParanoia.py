#! usr/bin/env python3
#! pdfParanoia.py - A script to encrypt every pdf file in a folder, and any
#! subfolders, with the password provided

import os, PyPDF2, send2trash, sys

def pdfParanoia(folder, password):

# walk the directory, checking files, encrypting any PDFs
    for foldername, subfolders, filenames in os.walk(folder):
        print('Searching for PDF files in %s...' % (foldername))
        for filename in filenames:
            if filename.endswith('.pdf'):
                pdfFile = open(filename, 'rb')
                pdfReader1 = PyPDF2.PdfFileReader(pdfFile)
                pdfWriter1 = PyPDF2.PdfFileWriter()
                if pdfReader1.isEncrypted == True:
                    print(filename + ' is already encrypted!')
                    continue
                for pageNum in range(pdfReader1.numPages):
                    pdfWriter1.addPage(pdfReader1.getPage(pageNum))

                print('Encrypting ' + filename + ' ...')
                pdfWriter1.encrypt(password)
                newFilename= filename + '_encrypted.pdf'
                resultPdf = open(newFilename, 'wb')
                pdfWriter1.write(resultPdf)
                resultPdf.close()

#Check to see if new file has been encrypted
                pdfReader2 = PyPDF2.PdfFileReader(open(newFilename, 'rb'))
                if pdfReader2.isEncrypted == True:
                    print(filename + ' was successfully encrypted')
                else:
                    print('There was an error when attempting to encrypt ' + filename)

#Check to see if file can be decrypted
                print('Testing ' + filename + '...')
                pdfReader2.decrypt(password)
                try:
                    pdfReader2.getPage(0)
                    print(filename + ' can be successfully decrypted')
                    print('Deleting ' + filename + '...')
                    send2trash.send2trash(filename)
                except:
                    print('There was an error when trying to decrypt ' + filename)

# prompt for folder and password            
if len(sys.argv) < 2:
    print('Usage: python pdfParanoia Folder password')
    sys.exit

folder = sys.argv[1]
password = sys.argv[2]

pdfParanoia(folder, password)
