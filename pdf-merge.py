#!/usr/bin/python
import os
import sys
from PyPDF2 import PdfFileReader, PdfFileMerger
f = sys.argv[1]
filename = sys.argv[2] or "merged.pdf"

files = [f for f in os.listdir(files_dir) if f.endswith("pdf")]
merger = PdfFileMerger()

for filename in files:
    merger.append(PdfFileReader(os.path.join(files_dir, filename), "rb"))

merger.write(os.path.join(f, filename))
