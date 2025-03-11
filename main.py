from fpdf import FPDF
import pandas as pd

df=pd.read_csv("topics.csv")

pdf=FPDF(orientation="P",format="A4",unit="mm")
pdf.add_page()
pdf.set_font(family="Times",style="B",size=10)

pdf.cell(w=0,h=10,txt="This is pdf",align="L",border=1,ln=1)
pdf.set_font(family="Times",style="",size=10)
pdf.cell(w=0,h=10,txt="This is second line in pdf",align="L",border=1,ln=1)

pdf.output("output.pdf")

