from bs4 import BeautifulSoup
import requests

URL = "https://web.archive.org/web/20231210134925/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)

website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")

titles = soup.findAll(name="h3" ,class_="listicleItem_listicle-item__title__BfenH")

movie_titles = []
for title in titles:
    movie_titles.append(title.getText())


with open("movies.txt", "w") as file:
    for items in movie_titles[::-1]:
        file.write(items + "\n")

