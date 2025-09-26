import requests
import csv

posts = []
page = 1

while True:
    r = requests.get(f"https://www.agile611.com/wp-json/wp/v2/posts?per_page=100&page={page}")
    r.encoding = 'utf-8'
    data = r.json()
    if not isinstance(data, list) or not data:
        break
    for post in data:
        if isinstance(post, dict) and 'title' in post and isinstance(post['title'], dict):
            title = post['title']['rendered']
        else:
            title = str(post.get('title', ''))
        title = title.replace(',', '')  # Remove commas from the title
        date = post.get('date', '')
        link = post.get('link', '')
        posts.append([title, date, link])
    page += 1

with open('agile611_posts.csv', 'w', newline='', encoding='utf-8-sig') as f:
    writer = csv.writer(f)
    writer.writerow(['Title', 'Date', 'URL'])
    writer.writerows(posts)

print(f"Saved {len(posts)} posts to agile611_posts.csv")