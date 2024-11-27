# track_job_postings.py
from bs4 import BeautifulSoup
import requests

def fetch_job_postings(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    jobs = soup.find_all("div", class_="job-card")
    return [{"title": job.find("h3").text, "company": job.find("h4").text} for job in jobs]

if __name__ == "__main__":
    JOB_URL = "https://www.example.com/jobs?q=competitor"
    postings = fetch_job_postings(JOB_URL)
    print(postings)
