# scan_pricing_pages.py
import requests
from bs4 import BeautifulSoup

def fetch_pricing(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    prices = soup.find_all("div", class_="pricing-tier")
    return [{"tier": price.find("h3").text, "cost": price.find("span", class_="cost").text} for price in prices]

if __name__ == "__main__":
    PRICING_URL = "https://www.example.com/pricing"
    pricing = fetch_pricing(PRICING_URL)
    print(pricing)
