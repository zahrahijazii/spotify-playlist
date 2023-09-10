import bs4
import requests 

user_input = input("What year would you like to travel to? Type the date in this format YYYY-MM-DD: ")

response = requests.get("https://www.billboard.com/charts/hot-100/" + user_input)

billboard_webpage = response.text

soup = bs4.BeautifulSoup(billboard_webpage, "html.parser")
