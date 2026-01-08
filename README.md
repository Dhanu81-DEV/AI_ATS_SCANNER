# 🧠 AI ATS Resume Scanner

An AI-powered tool that evaluates how well a resume matches a job description using **Gemini 2.0 Flash**, built with **FastAPI** (Backend) and **React.js** (Frontend).

## 🔧 Project Structure

```
AI_ATS_SCANNER/
├── backend/        # FastAPI + Gemini Flash + PostgreSQL
├── frontend/       # React App with UI + Animations
```

* * *

## 🚀 Backend Setup (FastAPI + Docker)

### ⚙️ Prerequisites

* *   Docker & Docker Compose installed    
* *   Gemini API Key from Google AI Studio   
* *   PostgreSQL credentials (used inside Docker by default)  

### 📁 File Structure (backend/)

```
backend/
├── app/
      ├── main.py
      ├── database.py
      ├── utils.py
      ├── models.py
├── requirements.txt
├── Dockerfile
├── dcoker-compose.yml
├── .env
```

### 🔐 .env file

Create a `.env` file in the `backend/` folder:

```env
GEMINI_API_KEY=your_gemini_api_key
DATABASE_URL=postgresql://postgres:postgres@db:5432/ats_db
```

### 🐳 Docker Setup

From the project root `AI_ATS_SCANNER/`, run:

```bash
cd backend
docker build -t ats-backend .
docker run -d -p 8000:8000 --env-file .env ats-backend
```

> ✅ Your backend will now be available at: `http://localhost:8000`

* * *

## 💻 Frontend Setup (React.js)

### ⚙️ Prerequisites

* *   Node.js and npm installed

### 📁 File Structure (frontend/)

```
frontend/
├── src/
│   └── App.js, App.css, etc.
├── package.json
```

### 📦 Install & Run

```bash
cd frontend
npm install
npm start
```

> ✅ Frontend runs at `http://localhost:3000` and connects to the backend on `http://localhost:8000`

* * *

## 🔁 Endpoints Summary

Endpoint                    , Method           ,Description

`/evaluate-resume`           , POST            ,Accepts resume (PDF) and JD (text), returns ATS score

* * *

## 🧠 Tech Used

* *   **Frontend**: React.js, Framer Motion, Confetti, Lucide Icons 
* *   **Backend**: FastAPI, PyMuPDF (PDF Parsing), PostgreSQL, Gemini Flash API 
* *   **Database**: PostgreSQL (via Docker)

* * *

## 🧪 Example Response

```json
{
  "ats_score": 88,
  "message": "ATS score successfully calculated.",
  "record_id": 69
}
```

* * *

## ✅ Features

* *   Resume vs Job Description Keyword Matching
* *   Score out of 100 using Gemini Flash
* *   Beautiful animated UI (confetti for success, emoji for fail)
* *   Data stored in PostgreSQL for future LLM training

* * *

## 📌 Why I Built This

> So many candidates apply without knowing how ATS systems work. This tool bridges that gap — giving real-time, AI-powered feedback before hitting "Apply."

* * *
