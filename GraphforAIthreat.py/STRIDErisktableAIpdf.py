import pandas as pd
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

# Data for the table
data = {
    "Threat/Vulnerability": [
        "Spoofing",
        "Tampering",
        "Repudiation",
        "Information Disclosure",
        "Denial of Service (DoS)",
        "Elevation of Privilege"
    ],
    "Description": [
        "Attempting to gain access to a system using a false identity (e.g., stolen credentials, false IP address).",
        "Unauthorized modification of data as it flows over a network between two computers.",
        "Users deny performing specific actions or transactions. Difficult to prove without adequate auditing.",
        "Unwanted exposure of private data (e.g., unauthorized access to tables/files, monitoring plain text data).",
        "Making a system/application unavailable (e.g., bombarding a server with requests, crashing an application with malformed input data).",
        "User with limited privileges gains privileged access to an application."
    ],
    "Likelihood": [
        "Medium",
        "Low",
        "Medium",
        "High",
        "Medium",
        "Medium"
    ],
    "Impact": [
        "High",
        "Medium",
        "Medium",
        "High",
        "High",
        "High"
    ],
    "Mitigation Strategies": [
        "- Implement robust security measures, secure authentication mechanisms, user verification processes, code integrity checks, and model validation procedures.\n- Perform regular security audits, threat modeling, and vulnerability assessments to identify spoofing vulnerabilities.",
        "- Apply safe coding practices, input validation, authentication, and access control mechanisms.\n- Perform security audits, code reviews, and vulnerability assessments to identify and address tampering attacks.\n- Anomaly detection mechanisms can help detect and respond to real-time tampering attempts.",
        "- Employ comprehensive logging mechanisms, including code modifications, transactions, and data changes.\n- Fulfill secure digital signatures to ensure the integrity and non-repudiation of transactions or code changes.\n- Monitor and review logs and audit trails to detect suspicious activities or unauthorized modifications.",
        "- Regularly assess and patch vulnerabilities in the platform’s software, frameworks, and dependencies.\n- Utilize secure coding practices, like SQL injection, cross-site scripting (XSS), or insecure direct object references.\n- Limit the amount of personally identifiable information or sensitive data stored on the platform.",
        "- Implement firewalls and intrusion detection systems to detect and block suspicious network traffic.\n- Employ rate-limiting or traffic-shaping techniques to manage incoming requests and prevent resource exhaustion.\n- Monitor system resources and set resource limits to prevent excessive consumption.",
        "- Implement strong access controls and least privilege principles to ensure necessary permissions to individuals.\n- Monitor user activities and implement anomaly detection mechanisms to identify privilege escalation attempts.\n- Utilize secure development frameworks, libraries, and components to minimize the risk of vulnerabilities and exploits."
    ]
}

# Create DataFrame
df = pd.DataFrame(data)

# Using ReportLab for Table Creation
def create_table_with_reportlab(dataframe, filename):
    doc = SimpleDocTemplate(filename, pagesize=letter)
    elements = []
    styles = getSampleStyleSheet()
    styleN = styles['Normal']

    title = Paragraph('Quantitative Cybersecurity Risk Assessment Table', styles['Title'])
    elements.append(title)
    elements.append(Spacer(1, 12))
    
    # Convert DataFrame to list of lists with Paragraphs
    data = [dataframe.columns.tolist()] + dataframe.values.tolist()
    for i in range(len(data)):
        for j in range(len(data[i])):
            data[i][j] = Paragraph(data[i][j], styleN)

    # Create the table
    table = Table(data, colWidths=[100, 150, 70, 50, 200])

    # Add style to the table
    style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('VALIGN', (0, 0), (-1, -1), 'TOP')
    ])
    table.setStyle(style)

    # Append the table to the elements list
    elements.append(table)

    # Build the document
    doc.build(elements)

create_table_with_reportlab(df, "Quantitative_Cybersecurity_Risk_Assessment_ReportLab_Formatted.pdf")

print("ReportLab PDF created successfully")

