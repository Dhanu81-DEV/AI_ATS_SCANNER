from fastapi import FastAPI, File, UploadFile, Form
from fastapi.middleware.cors import CORSMiddleware
from app.database import SessionLocal
from app.utils import extract_text_from_pdf, get_ats_score_from_gemini
from app.models import ResumeEvaluation
from datetime import datetime
import uvicorn

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/evaluate-resume")
async def evaluate_resume(resume_file: UploadFile = File(...), job_description: str = Form(...)):
    file_bytes = await resume_file.read()
    resume_text = extract_text_from_pdf(file_bytes)
    score = get_ats_score_from_gemini(resume_text, job_description)

    db = SessionLocal()
    record = ResumeEvaluation(
        resume_text=resume_text,
        jd_text=job_description,
        ats_score=score,
        created_at=datetime.utcnow()
    )
    db.add(record)
    db.commit()
    db.refresh(record)
    db.close()

    return {
        "ats_score": score,
        "message": "ATS score successfully calculated.",
        "record_id": record.id
    }

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
