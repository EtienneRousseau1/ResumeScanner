from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
from app.resume_parser import parse_resume
from app.models import Resume
import os

app = FastAPI(title="Resume Scanner API", description="Upload a resume and get structured text for analysis.")

@app.post("/upload_resume/", response_model=Resume)
async def upload_resume(file: UploadFile = File(...)):
    if file.content_type not in ["application/pdf", "application/vnd.openxmlformats-officedocument.wordprocessingml.document"]:
        raise HTTPException(status_code=400, detail="Only PDF and DOCX files are supported.")
    contents = await file.read()
    try:
        resume_data = parse_resume(contents, file.content_type)
        return resume_data
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to parse resume: {str(e)}") 