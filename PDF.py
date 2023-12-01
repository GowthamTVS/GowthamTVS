import streamlit as st
import PyPDF2

def read_pdf(file):
    pdf_reader = PyPDF2.PdfFileReader(file)
    text = ""
    for page_num in range(pdf_reader.numPages):
        page = pdf_reader.getPage(page_num)
        text += page.extractText()
    return text

def main():
    st.title("PDF File Uploader")

    uploaded_file = st.file_uploader("Choose a PDF file", type=["pdf"])

    if uploaded_file is not None:
        st.success("File successfully uploaded!")

        # You can display other information or process the PDF here
        st.info("### PDF Content:")
        pdf_content = read_pdf(uploaded_file)
        st.text(pdf_content)

if __name__ == "__main__":
    main()
