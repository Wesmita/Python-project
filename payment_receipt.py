from reportlab.platypus import SimpleDocTemplate, Table, Paragraph, TableStyle
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet

data = [
    ["Date", "Name of the item", "Quantity", "Price (Rs.)"],
    ["14/04/2024", "Drawing Book", "4", "550.00/-"],
    ["14/04/2024", "Crayon", "2", "100.00/-"],
    ["14/04/2024", "Artist Water Colour", "2", "320.00/-"],
    ["14/04/2024", "Painting Brush", "1", "280.00/-"],
    ["14/04/2024", "Sketch Pencil", "1", "190/-"],
    
    ["Sub Total"," ", " ", "1440.00/-"],
    ["Discount", " ", " ", "-60.00/-"],
    ["Total", " ", " ", "1380.00/-"],
    ]

pdf = SimpleDocTemplate("receipt.pdf", pagesize = A4)
styles = getSampleStyleSheet()
title_style = styles["Heading1"]
title_style.alignment = 1
title = Paragraph("Rangeen Book Stall", title_style)

style = TableStyle(
    [
        ("BOX", (0, 0), (-1, -1), 1, colors.black),
        ("GRID", (0, 0), (5, 5), 1, colors.black),
        ("BACKGROUND", (0, 0), (3, 0), colors.grey),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
        ("ALIGN", (0, 0), (-1, -1), "CENTER"),
        ("BACKGROUND", (0, 1), (-1, -1), colors.beige),
    ]
)

table = Table(data, style = style)
pdf.build([title, table])
