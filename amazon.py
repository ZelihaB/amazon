# import requests
#
url = 'https://www.amazon.com/Best-Sellers-Toys-Games/zgbs/toys-and-games/ref=zg_bs_nav_toys-and-games_0'
#
# custom_headers = {'user-agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Safari/605.1.15'}
# response = requests.get(url, headers=custom_headers)
#
# print (response.text)

import time
import requests

def make_request_with_retry(url):
    max_retries = 5
    retry_delay = 10  # seconds

    for attempt in range(max_retries):
        response = requests.get(url)
        if response.status_code == 200:
            return response
        else:
            print(f"Request failed (attempt {attempt + 1}), retrying in {retry_delay} seconds...")
            time.sleep(retry_delay)

    print("Max retries reached. Request failed.")
    return None

# Example usage
response = make_request_with_retry("https://example.com")

