import requests

def fetch_url(url):
    try:
        response = requests.get(url, timeout=10)
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None
