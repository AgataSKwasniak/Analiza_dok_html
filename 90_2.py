import requests
from bs4 import BeautifulSoup

strona = requests.get("https://www.alx.pl/pl/kontakt/")
soup = BeautifulSoup(strona.content, 'html.parser')
soup = soup.find_all("p", {"class", "tel"})
print(soup)
soup1 = soup[0].find_all("strong")
print(soup1)
print(soup1[0].get_text())
soup2 = soup[1].find_all("strong")
print(soup2)
print(soup2[0].get_text())


# for i in soup:
#     tel = i.find("strong")
#     print(tel.get_text())






# soup = soup.find("ul", {"class", "main-nav"})
# soup = soup.find("div")
# soup = soup.find_all("a")
# for x in soup:
#     print(x.get_text())