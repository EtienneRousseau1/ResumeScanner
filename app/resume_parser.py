import io
import pdfplumber
from docx import Document
from app.models import Resume

def parse_resume(file_bytes: bytes, content_type: str) -> Resume:
    if content_type == "application/pdf":
        text = extract_text_from_pdf(file_bytes)
    elif content_type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
        text = extract_text_from_docx(file_bytes)
    else:
        raise ValueError("Unsupported file type")
    return structure_resume_text(text)

def extract_text_from_pdf(file_bytes: bytes) -> str:
    with pdfplumber.open(io.BytesIO(file_bytes)) as pdf:
        return "\n".join(page.extract_text() or '' for page in pdf.pages)

def extract_text_from_docx(file_bytes: bytes) -> str:
    doc = Document(io.BytesIO(file_bytes))
    return "\n".join([para.text for para in doc.paragraphs])

def structure_resume_text(text: str) -> Resume:
    # Placeholder: just return all text in a single field for now
    return Resume(raw_text=text) 