from Barcode_reader_4 import BarcodeReader
from DB_reader import finder
from Barcode_parcer import parcer

from glob import glob
barcode = glob("barcode7.png")
code = str(BarcodeReader(barcode[0])).strip("b'")
print(code)
# print(finder(code))
print(parcer(code))