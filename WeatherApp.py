from bs4 import BeautifulSoup
import requests
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}


def weather(city):
    city = city.replace(" ", "+")
    # Creating url and request instance
    res = requests.get(
        f'https://www.google.com/search?q={city}&oq={city}&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8', headers=headers)
    print("Searching in google......\n")

    # Getting the raw data
    soup = BeautifulSoup(res.text, 'html.parser')

    # Getting location, time, info and weather. And formatting the data
    location = soup.select('#wob_loc')[0].getText().strip()
    time = soup.select('#wob_dts')[0].getText().strip()
    skyDesc = soup.select('#wob_dc')[0].getText().strip()
    temperature = soup.select('#wob_tm')[0].getText().strip()

    # Print data
    print(location)
    print(time)
    print(skyDesc)
    print(temperature+"°C")


# Taking input from the user
city = input("Enter the city name:\n")
city = city+" weather"
weather(city)
