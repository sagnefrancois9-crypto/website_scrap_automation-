import requests
from bs4 import BeautifulSoup

URL = "https://www.arpej.fr/fr/nos-residences/?related_city=52728"

response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")

element = soup.select_one("h3.residences-list__number span")


if element is None:
    print("Impossible de trouver l'information.")
else:
    resultat = element.get_text(strip=True)

    if resultat.isdigit():
        print(f"🏠 {resultat} logement(s) disponible(s) !")
    else:
        print("❌ Aucune résidence disponible.")
print(soup.title)
print("residence-list__number" in response.text)