from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet


def generate_report(filename, role, percentage, matched, missing):

    doc = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()

    story = []

    story.append(Paragraph("<b>ATS Resume Screening Report</b>", styles["Title"]))

    story.append(Paragraph(f"<b>Job Role:</b> {role}", styles["Normal"]))

    story.append(Paragraph(f"<b>Resume Score:</b> {percentage}%", styles["Normal"]))

    story.append(Paragraph("<br/>", styles["Normal"]))

    story.append(Paragraph("<b>Matched Skills</b>", styles["Heading2"]))

    for skill in matched:
        story.append(Paragraph(f"• {skill}", styles["Normal"]))

    story.append(Paragraph("<br/>", styles["Normal"]))

    story.append(Paragraph("<b>Missing Skills</b>", styles["Heading2"]))

    for skill in missing:
        story.append(Paragraph(f"• {skill}", styles["Normal"]))

    story.append(Paragraph("<br/>", styles["Normal"]))

    if percentage >= 90:
        recommendation = "Excellent match. Continue improving your portfolio."

    elif percentage >= 70:
        recommendation = "Good match. Learn the missing skills to strengthen your profile."

    elif percentage >= 50:
        recommendation = "Average match. Build projects using the missing technologies."

    else:
        recommendation = "Needs improvement. Focus on the required skills before applying."

    story.append(Paragraph("<b>Recommendation</b>", styles["Heading2"]))
    story.append(Paragraph(recommendation, styles["Normal"]))

    doc.build(story)