from io import BytesIO

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer


class PDFGenerator:
    """
    Generates a clinical report PDF.
    """

    @staticmethod
    def generate(report: dict) -> bytes:

        buffer = BytesIO()

        document = SimpleDocTemplate(buffer)

        styles = getSampleStyleSheet()

        elements = []

        elements.append(
            Paragraph(
                "<b>Ambient Clinical Scribe Report</b>",
                styles["Title"],
            )
        )

        elements.append(Spacer(1, 20))

        elements.append(
            Paragraph("<b>Transcript</b>", styles["Heading2"])
        )

        elements.append(
            Paragraph(report["transcript"], styles["BodyText"])
        )

        elements.append(Spacer(1, 20))

        soap = report["soap"]

        elements.append(
            Paragraph("<b>SOAP Note</b>", styles["Heading2"])
        )

        for section in [
            "subjective",
            "objective",
            "assessment",
            "plan",
        ]:

            elements.append(
                Paragraph(
                    f"<b>{section.title()}</b>",
                    styles["Heading3"],
                )
            )

            elements.append(
                Paragraph(
                    soap.get(section, ""),
                    styles["BodyText"],
                )
            )

            elements.append(Spacer(1, 10))

        elements.append(
            Paragraph(
                "<b>ICD-10 Recommendations</b>",
                styles["Heading2"],
            )
        )

        for recommendation in report["icd"]:

            elements.append(
                Paragraph(
                    f"{recommendation['code']} - "
                    f"{recommendation['description']}",
                    styles["BodyText"],
                )
            )

        document.build(elements)

        pdf = buffer.getvalue()

        buffer.close()

        return pdf