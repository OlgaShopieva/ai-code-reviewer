# 🤖 AI Code Reviewer for GitHub PRs

AI-powered service that automatically reviews GitHub Pull Requests using LLMs.

## 🚀 Features

- 🔍 Fetches PR diff from GitHub
- 🤖 Uses AI to analyze code changes
- ⚠️ Detects bugs, bad practices, and improvements
- ⚡ FastAPI backend with REST API
- 🔐 Secure environment variables handling

---

## 🛠 Tech Stack

- Python
- FastAPI
- OpenAI API
- GitHub REST API
- Requests

---

## 📦 How It Works

1. User sends request:
/review-pr?owner=repo_owner&repo=repo_name&pr=123

2. Service:
   - Fetches PR diff from GitHub
   - Sends diff to AI model
   - Returns structured review

---

## ▶️ Run Locally

### 1. Clone repo
git clone https://github.com/YOUR\_USERNAME/ai-code-reviewer.git

cd ai-code-reviewer

### 2. Create virtual environment
python -m venv venv
venv\Scripts\activate


### 3. Install dependencies
pip install -r requirements.txt


### 4. Add `.env`
OPENAI_API_KEY=your_key
GITHUB_TOKEN=your_token


### 5. Run server
uvicorn app.main:app --reload

---

## 📡 API Example
GET /review-pr?owner=python&repo=cpython&pr=148694

### Response:

```json
{
  "review": "Detailed AI-generated code review..."
}

⚠️ Limitations
Large PRs are truncated due to token limits
Depends on external APIs (GitHub & OpenAI)