# api.py
from fastapi import FastAPI, HTTPException
from modules.monitor_github import fetch_github_commits
from modules.track_job_postings import fetch_job_postings
from modules.analyze_app_reviews import fetch_app_reviews, analyze_sentiment
from modules.scan_pricing_pages import fetch_pricing
from modules.summarize_data import summarize_data
from modules.visualize_dashboard import update_notion

app = FastAPI()

# Configuration (Store tokens in environment variables for security)
GITHUB_TOKEN = "your_github_token"
NOTION_TOKEN = "your_notion_token"
OPENAI_API_KEY = "your_openai_api_key"
NOTION_PAGE_ID = "your_notion_page_id"

@app.get("/")
def home():
    return {"message": "Competitor Intelligence System API is running!"}

@app.get("/github-commits")
def github_commits(repo_owner: str, repo_name: str):
    try:
        commits = fetch_github_commits(repo_owner, repo_name, GITHUB_TOKEN)
        return {"commits": commits}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/job-postings")
def job_postings(job_url: str):
    try:
        postings = fetch_job_postings(job_url)
        return {"job_postings": postings}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/app-reviews")
def app_reviews(app_url: str):
    try:
        reviews = fetch_app_reviews(app_url)
        sentiment = analyze_sentiment(reviews)
        return {"reviews": sentiment}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/pricing-data")
def pricing_data(pricing_url: str):
    try:
        pricing = fetch_pricing(pricing_url)
        return {"pricing": pricing}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/summarize")
def summarize(data: str):
    try:
        summary = summarize_data(data, OPENAI_API_KEY)
        return {"summary": summary}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/update-notion")
def update_dashboard(content: str):
    try:
        response = update_notion(NOTION_PAGE_ID, content, NOTION_TOKEN)
        return {"notion_response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=3000)
