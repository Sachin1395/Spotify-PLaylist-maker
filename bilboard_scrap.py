import requests
from bs4 import BeautifulSoup

date=input("Which year do you want to travel ? (YYYY-MM-DD):")


response=requests.get(f"https://www.billboard.com/charts/hot-100/{date}/")

soup = BeautifulSoup(response.text, 'html.parser')
song_names_spans = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_names_spans]
print(song_names)


