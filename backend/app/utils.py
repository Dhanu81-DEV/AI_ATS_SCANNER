import fitz 
import os
import requests
from dotenv import load_dotenv
from google import genai

load_dotenv()
# GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

def extract_text_from_pdf(file_bytes: bytes) -> str:
    with fitz.open(stream=file_bytes, filetype="pdf") as doc:
        return "\n".join(page.get_text() for page in doc)

def get_ats_score_from_gemini(resume_text: str, jd_text: str) -> int:
    client = genai.Client()
    prompt = (
        "Given the following resume and job description, analyze and give an ATS score out of 100.\n"
        f"Resume:\n{resume_text}\n\n"
        f"Job Description:\n{jd_text}\n\n"
        "Return only the score as an integer."
    )

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
        )

        score = int("".join(filter(str.isdigit, response.text)))
        return score

    except  Exception as e:
        raise RuntimeError("Gemini service unavailable") from e
    

    # url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={GEMINI_API_KEY}"
    # prompt = (
    #     "Given the following resume and job description, analyze and give an ATS score out of 100.\n"
    #     f"Resume:\n{resume_text}\n\nJob Description:\n{jd_text}\n\n"
    #     "Return only the score as an integer."
    # )
    # payload = {
    #     "contents": [{"parts": [{"text": prompt}]}]
    # }
    # headers = {"Content-Type": "application/json"}
    # response = requests.post(url, json=payload, headers=headers)
    # # print(response.json())
    # # print(response.text)
    # try:
    #     result_text = response.json()["candidates"][0]["content"]["parts"][0]["text"]
    #     score = int("".join(filter(str.isdigit, result_text.split()[0])))
    #     return min(max(score, 0), 100)
    # except Exception:
    #     return 0
