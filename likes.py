from bs4 import BeautifulSoup as bs
import requests
import csv

def get_titles_and_likes(s, url, css_selector):
    r = s.get(url)
    soup = bs(r.content, 'lxml')
    info = [item.text.strip() for item in soup.select(css_selector)]
    titles = info[::2]
    likes = info[1::2]
    return list(zip(titles,likes))

results = []

with requests.Session() as s:

    for page in range(1,510):  #set number of pages
        data = get_titles_and_likes(s, 'https://data.nsw.gov.au/data/dataset?page={}'.format(page), '.dataset-heading .searchpartnership-url-analytics, .dataset-heading [href*="/data/dataset"], .dataset-item  #likes-count')
        results.append(data)

results = [i for item in results for i in item]

with open(r'print_all_likes_4.csv','w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['Title','Likes'])
        for row in results:
            w.writerow(row)