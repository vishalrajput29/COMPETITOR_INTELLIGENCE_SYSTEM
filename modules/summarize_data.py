# summarize_data.py
import openai

def summarize_data(data, api_key):
    openai.api_key = api_key
    prompt = f"Summarize the following competitor insights:\n{data}"
    response = openai.Completion.create(engine="gpt-4", prompt=prompt, max_tokens=200)
    return response.choices[0].text.strip()

if __name__ == "__main__":
    DATA = "Collected data here."
    API_KEY = "your_openai_api_key"
    summary = summarize_data(DATA, API_KEY)
    print(summary)
