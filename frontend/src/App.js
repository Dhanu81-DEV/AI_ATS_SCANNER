import React, { useState } from 'react';
import Confetti from 'react-confetti';
import { motion } from 'framer-motion';
import { Frown, PartyPopper, FileText } from 'lucide-react';
import './App.css';

function App() {
  const [resumeFile, setResumeFile] = useState(null);
  const [jobDescription, setJobDescription] = useState('');
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);

  const handleSubmit = async () => {
    if (!resumeFile || !jobDescription.trim()) return;

    setLoading(true);
    const formData = new FormData();
    formData.append('resume_file', resumeFile);
    formData.append('job_description', jobDescription);

    try {
      const res = await fetch('http://localhost:8000/evaluate-resume', {
        method: 'POST',
        body: formData
      });
      const data = await res.json();
      setResult(data);
    } catch (err) {
      alert('Failed to fetch ATS score.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="App">
      <div className="container">
        <div className="left-panel">
          <h1 className="title">Resume ATS Analyzer</h1>
          <p className="subtitle">Get your resume evaluated instantly using AI</p>

          <div className="form-section">
            <label className="form-label">Upload Resume (PDF)</label>
            <div className="file-input-wrapper">
              <input
                type="file"
                accept="application/pdf"
                id="resume-upload"
                onChange={(e) => setResumeFile(e.target.files[0])}
              />
              <label htmlFor="resume-upload" className="custom-file-label">
                <FileText size={20} /> {resumeFile ? resumeFile.name : 'Choose a file'}
              </label>
            </div>

            <label className="form-label">Job Description</label>
            <textarea
              placeholder="Paste job description here..."
              rows={5}
              value={jobDescription}
              onChange={(e) => setJobDescription(e.target.value)}
            />

            <button
              disabled={loading || !resumeFile || !jobDescription.trim()}
              onClick={handleSubmit}
            >
              {loading ? 'Evaluating...' : 'Analyze Resume'}
            </button>
          </div>
        </div>

        <div className="right-panel">
          <h3>Result : </h3>
          {loading && <div className="loader">Analyzing Resume...</div>}

          {!loading && result && (
            <motion.div
              className="result"
              initial={{ opacity: 0, y: 30 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ duration: 0.5 }}
            >
              <h2>{result.message}</h2>
              <div className="score">ATS Score: {result.ats_score}</div>
              {result.ats_score >= 80 ? (
                <div>
                  <PartyPopper size={50} className="icon success" />
                  <p className="success-text">🎉 Great job! Your resume aligns well with the job!</p>
                  <Confetti width={window.innerWidth} height={300} recycle={false} />
                </div>
              ) : (
                <div>
                  <Frown size={50} className="icon fail" />
                  <p className="fail-text">😕 Consider improving your resume to better fit the job.</p>
                </div>
              )}
            </motion.div>
          )}
        </div>
      </div>
    </div>
  );
}

export default App;