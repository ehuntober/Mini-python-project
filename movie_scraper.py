
import requests

from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/"\
	  "https://www.empireonline.com/movies/features/"\
	  "best-movies-2"

response = requests.get(URL)

webpage = response.text

soup = BeautifulSoup(webpage,'html.parser')
movie_tags = soup.find_all(name='h3', class_ ='title')

with open('movies.txt','w') as file:
	for movie in reversed(movie_tags):
		file.write(f"{movie.getText()}\n")