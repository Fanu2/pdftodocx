import streamlit as st
from pdf2docx import Converter
from io import BytesIO
import tempfile
import os
import zipfile

def convert_single_pdf(pdf_file):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_pdf:
        tmp_pdf.write(pdf_file.read())
        tmp_pdf_path = tmp_pdf.name

    tmp_docx_path = tmp_pdf_path.replace(".pdf", ".docx")
    cv = Converter(tmp_pdf_path)
    cv.convert(tmp_docx_path, start=0, end=None)
    cv.close()

    with open(tmp_docx_path, "rb") as f:
        docx_data = f.read()

    os.remove(tmp_pdf_path)
    os.remove(tmp_docx_path)
    return pdf_file.name.replace(".pdf", ".docx"), docx_data

st.title("📄 PDF to DOCX Batch Converter")

uploaded_files = st.file_uploader("Upload multiple PDF files", type="pdf", accept_multiple_files=True)

if uploaded_files and st.button("Convert All"):
    zip_buffer = BytesIO()
    with zipfile.ZipFile(zip_buffer, "w") as zipf:
        for pdf_file in uploaded_files:
            docx_name, docx_bytes = convert_single_pdf(pdf_file)
            zipf.writestr(docx_name, docx_bytes)
    zip_buffer.seek(0)
    st.success("All files converted successfully!")
    st.download_button("📦 Download ZIP of DOCX files", zip_buffer, file_name="converted_docs.zip")
