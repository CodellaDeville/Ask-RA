import streamlit as st
from fpdf import FPDF
import os

# Function to generate a PDF report
def generate_pdf(user_query, ai_response, interpretation, file_name="SoulCompass_Report.pdf"):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()

    # Add Logo
    logo_path = "soulcompass_logo.jpg"  # Ensure the file is in the same directory
    if os.path.exists(logo_path):
        pdf.image(logo_path, x=65, y=10, w=80)  # Centered at the top
        pdf.ln(40)  # Add space after logo

    # Title
    pdf.set_font("Arial", style="B", size=16)
    pdf.cell(200, 10, "SoulCompass AI Interpretation Report", ln=True, align="C")
    pdf.ln(10)

    # User Query
    pdf.set_font("Arial", style="B", size=12)
    pdf.cell(0, 10, "User Query:", ln=True)
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 8, user_query)
    pdf.ln(5)

    # AI Response
    pdf.set_font("Arial", style="B", size=12)
    pdf.cell(0, 10, "AI-Generated Response:", ln=True)
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 8, ai_response)
    pdf.ln(5)

    # AI Interpretation
    pdf.set_font("Arial", style="B", size=12)
    pdf.cell(0, 10, "AI Interpretation & Insights:", ln=True)
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 8, interpretation)
    pdf.ln(5)

    # Save PDF
    pdf.output(file_name)
    return file_name

# Streamlit Interface
st.title("SoulCompass AI-Powered Insights")

st.write("Welcome to SoulCompass, your guide to deeper spiritual understanding.")

# User Input
user_query = st.text_area("Enter your spiritual query:")

if st.button("Generate Insights"):
    ai_response = f"Simulated AI Response for: {user_query}"  # Replace with actual AI response logic
    interpretation = f"Interpreted meaning: {user_query[::-1]}"  # Placeholder for interpretation logic

    # Generate PDF
    pdf_file = generate_pdf(user_query, ai_response, interpretation)

    # Provide Download Link
    with open(pdf_file, "rb") as f:
        st.download_button("Download Your Insight Report", f, file_name="SoulCompass_Report.pdf")
