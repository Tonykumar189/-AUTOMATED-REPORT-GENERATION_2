import pandas as pd
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from datetime import datetime

# ✅ Step 1: Replace with your actual file name (make sure the file is in the same directory)
file_path = 'sample_data.csv'
df = pd.read_csv(file_path)

# ✅ Step 2: Generate summary statistics
summary = df.describe(include="all").round(2)

# ✅ Step 3: Create PDF report
report_name = "Automated_Report.pdf"
pdf = canvas.Canvas(report_name, pagesize=A4)
pdf.setTitle("Automated Report")

# Page setup
width, height = A4
pdf.setFont("Helvetica-Bold", 16)
pdf.drawString(50, height - 50, "Automated Data Report")

# Timestamp
pdf.setFont("Helvetica", 12)
timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
pdf.drawString(50, height - 80, f"Generated on: {timestamp}")

# Section title
pdf.setFont("Helvetica-Bold", 10)
x, y = 50, height - 120
pdf.drawString(x, y, "Column Summary:")

# Draw data summaries
pdf.setFont("Helvetica", 8)
y -= 20
for col in summary.columns:
    pdf.drawString(x, y, f"{col}:")
    y -= 12
    for stat in summary.index:
        value = summary.at[stat, col]
        pdf.drawString(x + 20, y, f"{stat}: {value}")
        y -= 12
        if y < 80:  # Add new page if running out of space
            pdf.showPage()
            pdf.setFont("Helvetica", 8)
            y = height - 80

# ✅ Save PDF
pdf.save()
print(f"✅ PDF report generated successfully: {report_name}")
