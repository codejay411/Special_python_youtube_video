from fpdf import FPDF
pdf = FPDF()

pdf.add_page()
pdf.set_font("Arial", size=16)

f = open("pdf.txt", "r")
for x in f:
    pdf.cell(200, 10, txt=x, ln=1, align="C" )

pdf.output("text.pdf")