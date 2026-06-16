from fpdf import FPDF
import os


class ReportGenerator:

    @staticmethod
    def create_report(
        username,
        score,
        level,
        risk,
        filename
    ):

        os.makedirs(
            os.path.dirname(filename),
            exist_ok=True
        )

        pdf = FPDF()

        pdf.add_page()

        pdf.set_font(
            "Arial",
            size=14
        )

        pdf.cell(
            200,
            10,
            "Password Security Report",
            ln=True
        )

        pdf.ln(10)

        pdf.cell(
            200,
            10,
            f"User: {username}",
            ln=True
        )

        pdf.cell(
            200,
            10,
            f"Security Score: {score}",
            ln=True
        )

        pdf.cell(
            200,
            10,
            f"Strength Level: {level}",
            ln=True
        )

        pdf.cell(
            200,
            10,
            f"Risk Level: {risk}",
            ln=True
        )

        pdf.output(filename)