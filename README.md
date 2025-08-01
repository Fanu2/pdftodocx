# 📄 PDF to DOCX Batch Converter

A simple and efficient Streamlit web app that allows you to **upload multiple PDF files** and **convert them to DOCX format** in bulk. Once converted, the DOCX files are packaged into a ZIP archive for easy download.

## 🚀 Features

- 🗂 Upload multiple PDFs at once  
- 🔄 Automatically convert each PDF to DOCX format  
- 📦 Download all DOCX files as a single ZIP archive  
- ⚡ Fast and lightweight with clean temporary file handling

## 🛠️ Tech Stack

- [Streamlit](https://streamlit.io/)
- [pdf2docx](https://pypi.org/project/pdf2docx/)

## 📦 Installation

1. Clone the repo:

   ```bash
   git clone https://github.com/your-username/pdf-to-docx-converter.git
   cd pdf-to-docx-converter


    Install dependencies:

pip install streamlit pdf2docx

Run the app:

    streamlit run streamlit_app.py

🧠 How It Works

Each uploaded PDF file is temporarily saved and converted using the pdf2docx.Converter. The resulting DOCX files are then added to a ZIP archive and offered as a single downloadable package.
📁 Example

Upload:

document1.pdf
report2.pdf

After conversion:

document1.docx
---
Let me know if you want to include **screenshots**, **deployment instructions (e.g. for Streamlit Cloud)**, or a **live demo link**.

report2.docx
→ downloaded as converted_docs.zip
