# visualize_dashboard.py
import requests

def update_notion(page_id, content, notion_token):
    url = f"https://api.notion.com/v1/pages"
    headers = {
        "Authorization": f"Bearer {notion_token}",
        "Content-Type": "application/json",
        "Notion-Version": "2022-06-28"
    }
    data = {
        "parent": {"type": "page_id", "page_id": page_id},
        "properties": {
            "title": [{"type": "text", "text": {"content": "Competitor Insights"}}]
        },
        "children": [{"object": "block", "type": "paragraph", "paragraph": {"text": [{"type": "text", "text": {"content": content}}]}}]
    }
    response = requests.post(url, headers=headers, json=data)
    return response.json()

if __name__ == "__main__":
    PAGE_ID = "your_page_id"
    CONTENT = "Summarized insights here."
    NOTION_TOKEN = "your_notion_token"
    response = update_notion(PAGE_ID, CONTENT, NOTION_TOKEN)
    print(response)
