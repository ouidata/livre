# pip3 install img2pdf
import os
import img2pdf

with open("output.pdf", "wb") as f:
    f.write(img2pdf.convert("adventure.jpeg"))
