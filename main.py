import mechanicalsoup
import pandas as pd
browser = mechanicalsoup.Browser()
url = "http://olympus.realpython.org/login"
page = browser.get(url)
login = page.soup

form = login.select("form")[0]
form.select("input")[0]["value"] = "zeus"
form.select("input")[1]["value"] = "ThunderDude"

profile = browser.submit(form,page.url)

links = profile.soup.select("a")
page2 = "http://olympus.realpython.org"
for link in links:
    address =page2 +  link["href"]
    text = link.text
    print(f"{text}: {address}")
    
