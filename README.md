# -AUTOMATED-REPORT-GENERATION_2

**COMPANY** : CODTECH IT SOLUTIONS
**NAME** : VELIVALA TONY KUMAR
**INTERN ID** : CT12TQS
**DOMAIN** : Python Programming
**BATCH DURATION** : FEB 10 2025 to APRIL 10 2025
**MENTOR NAME** : Neela Santhosh Kumar
#Descrption 


Task 2: Automated Report Generation – Description of Work Performed

As part of my internship under CodTech, Task 2 involved developing a solution for Automated Report Generation. The primary objective of this task was to build a Python script that could read data from an external file, perform basic data analysis, and generate a well-formatted PDF report. This task not only enhanced my Python scripting skills but also familiarized me with popular PDF generation libraries such as FPDF and ReportLab.

To begin, I carefully reviewed the requirements outlined in the task. The main steps involved were:

1. Reading data from a file (CSV or Excel),


2. Analyzing that data (performing basic statistical operations or summarizing contents), and


3. Generating a PDF report that visually and textually represented the results of the analysis.




---

Data Reading and Analysis

For the input, I used a CSV file that contained structured data (such as student marks, sales data, or product inventory). I wrote Python code using pandas, a powerful data analysis library, to load and inspect the data. I checked for missing values, calculated column-wise statistics such as totals, averages, and frequencies, and extracted key insights. For example, if the dataset involved sales, I calculated total sales, average sales per day, and top-performing products.

Here’s a sample of the analysis logic used:

import pandas as pd

data = pd.read_csv('sample_data.csv')
summary = data.describe()
top_entries = data.head(5)

This part of the task helped solidify my understanding of pandas functions like .describe(), .groupby(), .sum(), and .mean().


---

PDF Report Generation

After extracting insights, I shifted focus to report generation. I first explored FPDF, a lightweight PDF library in Python. Using this library, I created structured reports with headings, paragraphs, and tables. Later, I also experimented with ReportLab, which offered more flexibility in text formatting and layout design.

The report included:

A title page with the name of the report and date.

Summary statistics and key findings.

A sample data table (e.g., top 5 rows of the dataset).

Optional charts for better data visualization.


Sample code for adding a table using FPDF:

from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)
pdf.cell(200, 10, txt="Automated Report", ln=True, align='C')

# Add summary data
for col in summary.columns:
    pdf.cell(200, 10, txt=f"{col}: {summary[col].mean()}", ln=True)

pdf.output("report.pdf")

This segment taught me about report structuring, formatting, layout balance, and automated writing to files.


---

Challenges and Learnings

One of the initial challenges was adjusting the layout of the PDF so that it remained readable and professional-looking. Proper formatting of text, choosing the right font sizes, and organizing sections logically took multiple attempts. Additionally, I learned how to dynamically insert content such as charts using libraries like matplotlib and exporting them to PDF using fpdf.image() or reportlab.platypus.Image.

I also ensured the script was reusable—accepting any compatible CSV file and generating a corresponding report. I added error handling to alert users in case of incorrect file formats or missing data.


---

Conclusion

Task 2 helped me gain valuable experience in file I/O operations, data analysis with pandas, and document generation using PDF libraries. I now feel more confident in building automation scripts that can convert raw data into meaningful insights and present them in a formal document format.

Overall, this task strengthened my programming logic, improved my attention to detail in layout design, and enhanced my skills in data visualization and reporting—skills that are highly relevant for real-world data analysis and business intelligence tasks.


---
#output 
[Automated_Report.pdf](https://github.com/user-attachments/files/19730617/Automated_Report.pdf)
