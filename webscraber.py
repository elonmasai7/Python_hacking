import requests

def fetch_url(url):
    try:
        response = requests.get(url, timeout=10)  # Add a timeout to the request
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None

if __name__ == "__main__":
    url = "your_url_here"  # Replace with the actual URL
    content = fetch_url(url)
    if content:
        print(content)
