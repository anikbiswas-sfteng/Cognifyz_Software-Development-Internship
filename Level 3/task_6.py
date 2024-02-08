import requests
from bs4 import BeautifulSoup

def fetch_data(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.content
        else:
            print("Failed to fetch data from the website. Please check the URL.")
            return None
    except requests.RequestException as e:
        print("An error occurred while fetching data:", e)
        return None

def parse_data(html_content):
    if html_content:
        soup = BeautifulSoup(html_content, 'html.parser')
        # Example: Extracting titles of articles from a news website
        titles = soup.find_all('h2', class_='article-title')
        return [title.text.strip() for title in titles]
    else:
        return None

def present_data(data):
    if data:
        print("Here are the titles of articles:")
        for index, title in enumerate(data, start=1):
            print(f"{index}. {title}")
    else:
        print("No data available.")

def main():
    url = input("Enter the URL of the website to scrape: ")
    html_content = fetch_data(url)
    if html_content:
        data = parse_data(html_content)
        present_data(data)

if __name__ == "__main__":
    main()
