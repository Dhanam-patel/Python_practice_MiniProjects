import requests

# API URL
url = "https://newsapi.org/v2/everything"
params = {
    "domains": "wsj.com",
    "q": "technology",
    "apiKey": "4e67960493ca496d8c15cd966c94e3a5",
    "sortBy": "publishedAt",  # Sort by recent articles
    "pageSize": 9,  # Fetch 10 articles
}

# Fetching the data
response = requests.get(url, params=params)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()
    articles = data.get("articles", [])
    if not articles:
        print("No articles found.")
    else:
        # Print each article
        for index, article in enumerate(articles, start=1):
            print(f"Article {index}:")
            print(f"Title: {article['title']}")
            print(f"Description: {article['description']}")
            print(f"URL: {article['url']}")
            print("-" * 40)
else:
    print(f"Error: {response.status_code}, {response.text}")
