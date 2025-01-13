import webbrowser

from fpdf import FPDF
from bill_class import Bill
from flatmate_class import Flatmate


class PdfReport:
    """
    Creates a pdf file, before saving to cloud location, that contains:
    - Flatmate names
    - Amount owed by each Flatmate
    - Time period of bill
    """

    def __init__(self, filename: str):
        self.filename = filename

    def generate(self, *flatmate: Flatmate, bill: Bill):
        for flatmate in flatmate:
            pdf = FPDF(orientation='P', unit='pt', format='A4')
            pdf.add_page()

            # Add icon
            pdf.image("./files/house.png", w=30, h=30)

            #Insert Title
            pdf.set_font(family='Times', size=24, style='B')
            pdf.cell(w=0, h=80, txt=f"{flatmate.name} Invoice", border=0, align='C', ln=1)

            # Insert Time Period
            pdf.set_font(family='Times', size=14, style='B')
            pdf.cell(w=130, h=40, txt="Period:", border=0)
            pdf.set_font(family='Times', size=14)
            pdf.cell(w=130, h=40, txt=f"{bill.time_period} days", border=0, ln=1)

            # Insert Flatmate name and due amount
            pdf.set_font(family='Times', size=14, style='B')
            pdf.cell(w=130, h=40, txt=f"Amount Payable:", border=0)
            pdf.set_font(family='Times', size=14)
            pdf.cell(w=130, h=40, txt=f"£{flatmate.pays(bill)} ", border=0, ln=1)

            pdf.output(f"{self.filename}_{flatmate.name.lower()}.pdf")
            webbrowser.open(f"file:///C:/Projects/Python/OOP%20Projects/App-2-Flatmates-Bill/{self.filename}_{flatmate.name.lower()}.pdf")

x = Flatmate('Liam', 18)
x_bill = Bill(102, 28)
x_pdf = PdfReport('28_day_invoice')
y = Flatmate('Laura', 10)
y_bill = Bill(102, 28)
PdfReport.generate(x_pdf, x, y, bill=x_bill)