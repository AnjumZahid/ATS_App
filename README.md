ATS Resume Analyzer

This repository contains two implementations of an ATS (Applicant Tracking System) Resume Analyzer app:

Implementation 1: Full-stack Dockerized app using FastAPI backend and Streamlit frontend, deployed using GitHub Actions and Render.

Implementation 2: A simple Streamlit-only app using Google Gemini API, integrated with GitHub Actions CI.

🌟 Implementation 1: FastAPI + Streamlit (Dockerized)

Features

Upload your resume (PDF)

Enter job description

Get:

Detailed ATS-style resume analysis

Match percentage

Backend powered by FastAPI + Gemini API

Frontend built using Streamlit

Docker support

CI/CD using GitHub Actions

Folder Structure

.
├── .github/workflows
│   └── deploy.yml                  # GitHub Actions workflow for Docker build & push
├── Dockerfile.backend                 # Dockerfile for FastAPI backend
├── Dockerfile.frontend                # Dockerfile for Streamlit frontend
├── backend.py                         # FastAPI backend for analysis endpoints
├── frontend.py                        # Streamlit frontend UI
├── requirements.txt                   # Shared dependencies
├── .dockerignore
├── .gitignore

Environment Variable

GEMINI_API_KEY must be defined in your deployment or .env file.

FastAPI Endpoints

POST /analyze_resume/: Returns analysis of resume vs. job description.

POST /match_percentage/: Returns numeric match percentage only.

GitHub Actions Workflow

.github/workflows/deploy.yml builds Docker images for backend and frontend and pushes to Docker Hub.

Update these secrets in GitHub repository:

DOCKER_USERNAME

DOCKER_PASSWORD

Streamlit URL (example after deployment)

backend_url = "https://ats-app-docker-fastapi-backend.onrender.com"

🚀 Implementation 2: Streamlit Only (Simple Gemini App)

Features

Enter job description

Upload resume (PDF)

Click buttons to:

Get professional resume analysis

Get match percentage + keywords

Uses google-generativeai Gemini model

Files

.
├── .github/workflows
│   └── streamlit_ci.yml           # GitHub Actions for testing Streamlit launch
├── app.py                            # Streamlit app logic
├── requirements.txt
├── .gitignore

Streamlit Secrets

Configure the following in .streamlit/secrets.toml or Streamlit Cloud:

GEMINI_API_KEY = "your_gemini_api_key"

Prompts Used

Resume Analysis Prompt: Reviews resume strengths/weaknesses

Match Percentage Prompt: Gives percentage, missing keywords, and final thoughts

GitHub Actions Workflow

Runs app.py headlessly

Saves logs for debugging CI failures

📄 Requirements

streamlit
google-generativeai
python-dotenv
pypdf

🚧 Usage (Locally)

Clone the repo:

git clone https://github.com/your-username/ats-resume-analyzer.git
cd ats-resume-analyzer

Install dependencies:

pip install -r requirements.txt

Set your environment variable:

export GEMINI_API_KEY=your_key

Run locally (Streamlit only):

streamlit run app.py

Or to run backend:

uvicorn backend:app --reload

🚀 Deploying

Docker: Build and push Docker images manually or use GitHub Actions

Render / Railway / EC2: Use Docker or uvicorn to run backend

Streamlit Cloud: For Streamlit-only version

💪 Contributing

Feel free to open issues or PRs for improvements and new features!

😎 License

MIT License. Use freely for learning and educational purposes.
