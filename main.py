from ocr import *
#later replacement through UI
invoicePath  ="invoice.pdf"

data = fileToTextData(invoicePath)

print(data)