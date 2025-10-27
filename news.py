import requests
from datetime import date, timedelta

#Replace with your actual API key
API_KEY = "dbe57b028aeb41e285a226a94865f7a7"

#Ask user what kind of news they want
query = input("What type of news are you interested in today? ")

#Calculate the 'from' date (7 days ago)
from_date = (date.today()-timedelta(days=7)).isoformat()

# Create the URL
url = f"https://newsapi.org/v2/everything?q={query}&from={from_date}&sortBy=publishedAt&apiKey={API_KEY}"

print(url)

#Send the request
response = requests.get(url)
data = response.json()

#Check for errors before trying to access 'articles'
if data.get("status") != "ok":
    print("\n Error fetching news:")
    print(f"Code: {data.get('code')}")
    print(f"Message: {data.get('message')}")
else:
    articles = data.get("articles", [])
    if not articles:
        print("\nNo articles found for your search.")
    else:
        print("\nHere are some recent articles:\n")
        for i, article in enumerate(articles[:5], start=1):
            print(f"{i}. {article['title']}")
            print(f"  {article['url']}\n")
