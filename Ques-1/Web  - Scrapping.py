import requests
from bs4 import BeautifulSoup
import os 
import time

from types import resolve_bases
os.makedirs('File')

visited_urls =set()
def scrap_site(url, site_count):
    if url in visited_urls:
        return
    visited_urls.add(url)
    # https://www.kochbar.de
    try:
        response = requests.get(url)
        if response.status_code!=200:
            print(f"Error : {response.status_code} - {url}")
        soup = BeautifulSoup(response.text, 'html.parser')
        

        links = soup.find_all('a', href=True)
        links = [link['href'] for link in links]
        links = [link for link in links if link.startswith('http')]
        links = list(set(links))

        text_content = soup.get_text(strip=True)
        file_name = f"File/site_{site_count}.txt"
        with open(file_name, 'w', encoding='utf-8') as file:
            file.write(text_content)
            print(f"Content Save to {file_name}")

        for link in links:
            full_link = requests.compat.urljoin(url, link)
            scrap_site(link, site_count+1)
        # time.sleep(1)

    except Exception as e:
        print(f"Error : {e} - {url}")
        return 


start_url = "URL"
scrap_site(start_url, 1)