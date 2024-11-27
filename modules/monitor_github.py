# monitor_github.py
import requests

def fetch_github_commits(repo_owner, repo_name, token):
    url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/commits"
    headers = {"Authorization": f"token {token}"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception("Failed to fetch commits. Check token or repo details.")

if __name__ == "__main__":
    TOKEN = "your_github_token"
    REPO_OWNER = "competitor"
    REPO_NAME = "repo-name"
    commits = fetch_github_commits(REPO_OWNER, REPO_NAME, TOKEN)
    print(commits)
