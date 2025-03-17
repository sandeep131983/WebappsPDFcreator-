from fpdf import FPDF
import pandas as pd

df=pd.read_csv("topics.csv")
pdf=FPDF(orientation="P",format="A4",unit="mm")
for index,page in df.iterrows():
    pdf.add_page()
    pdf.set_font(family="Times",style="B",size=10)
    pdf.set_text_color(254, 110, 120)
    pdf.cell(w=0,h=10,txt=page["Topic"],align="L",ln=1)
    pdf.line(10,17,200,17)
    for i in range(page["Pages"] -1):
        pdf.add_page()
pdf.output("output.pdf")



