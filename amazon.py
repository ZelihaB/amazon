import requests

url = 'https://www.amazon.com/Best-Sellers-Toys-Games/zgbs/toys-and-games/ref=zg_bs_nav_toys-and-games_0'
response = requests.get(url)

print (response.text)
