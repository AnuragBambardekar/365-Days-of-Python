import requests

# proxy = '91.106.126.148:80'

# r = requests.get('https://httpbin.org/ip',
#                  proxies={'http':proxy,
#                           'https':proxy},
#                           timeout=3)

# print(r.status_code)
# print(r.json())

with open("260_Rotating_Proxies/valid_proxies.txt","r") as f:
    proxies = f.read().split("\n")

sites_to_check = ["http://books.toscrape.com/",
                  "http://books.toscrape.com/catalogue/category/books/childrens_11/index.html",
                  "http://books.toscrape.com/catalogue/category/books/travel_2/index.html"]

counter = 0
for site in sites_to_check:
    try:
        print(f"Using the proxy: {proxies[counter]}")
        res = requests.get(site, proxies={"http":proxies[counter],
                                          "https":proxies[counter]})
        print(res.status_code)
        print(res.text)
    except:
        print("Failed")
    finally:
        counter+=1