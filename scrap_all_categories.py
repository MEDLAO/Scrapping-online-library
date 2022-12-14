import time
from scrap_category import *


# Phase 3 et 4 : Extraire tous les produits de toutes les catégories + téléchargement des fichiers images :
def etl_categories():
    """
    Cette fonction permet d'extraire les données des livres de toutes les catégories du site pour les charger dans
    différents fichiers csv, et de télécharger les fichiers images de chaque livre dans un dossier approprié.
    :param
    :return: Affiche progressivement un message pour chaque catégorie pendant le scrapping.
    """
    home_url = "https://books.toscrape.com/"
    page = requests.get(home_url)
    soup = BeautifulSoup(page.content, 'html.parser')

    categories_links = [home_url + url_category.get('href') for url_category in soup.select('div ul li a')[:-1]][2:]
    categories_names = [url_category.string.strip() for url_category in soup.select('div ul li a')[:-1]][2:]

    td = time.time()
    for i in range(len(categories_links)):
        t1 = time.time()
        print(f"- Scrapping category ", categories_names[i], "....", end=" ", flush=True)
        scrap_category(categories_links[i])
        t2 = time.time()
        print("Completed in ", round(t2 - t1), "seconds")

    tf = time.time()
    print("Completed Scrapping all site in ", round(tf - td), "seconds")


# Ce code s'éxécute seulement si je fais >>> python scrap_all_categories.py dans le terminal
if __name__ == "__main__":
    import time
    t1 = time.time()
    etl_categories(home_url)
    t2 = time.time()
    print(t2 - t1)