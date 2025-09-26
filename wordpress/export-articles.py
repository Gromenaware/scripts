import requests
import csv

posts = []
page = 1

while True:
    r = requests.get(f"https://www.agile611.com/wp-json/wp/v2/posts?per_page=100&page={page}")
    data = r.json()
    if not isinstance(data, list) or not data:
        break
    for post in data:
        # Defensive code for title
        if isinstance(post, dict) and 'title' in post and isinstance(post['title'], dict):
            title = post['title']['rendered']
        else:
            title = str(post.get('title', ''))
        date = post.get('date', '')
        link = post.get('link', '')
        posts.append([title, date, link])
    page += 1

# Save to CSV
with open('agile611_posts.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['Title', 'Date', 'URL'])  # Header
    writer.writerows(posts)

print(f"Saved {len(posts)} posts to agile611_posts.csv")
# File: wordpress/export-articles.py