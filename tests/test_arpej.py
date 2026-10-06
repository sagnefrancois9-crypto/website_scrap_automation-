from playwright.sync_api import sync_playwright

URL = "https://www.arpej.fr/fr/nos-residences/?related_city=52728"

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    print("🌐 Ouverture...")
    page.goto(URL, wait_until="domcontentloaded")
    page.wait_for_timeout(5000)

    texte = page.locator("body").inner_text()

    if "Toutes les résidences aux alentours sont complètes" in texte:
        print("❌ Aucune résidence disponible")
    else:
        print("🏠 Quelque chose est disponible !")

    browser.close()