import requests
from bs4 import BeautifulSoup

# Hacemos una petición GET a la URL deseada
url = 'https://www.google.com'
response = requests.get(url)

# Analizamos el contenido HTML de la respuesta
soup = BeautifulSoup(response.text, 'html.parser')

# Extraemos todos los enlaces
links = [a['href'] for a in soup.find_all('a', href=True)] # lista por comprensión

# Imprimimos los enlaces
for link in links:
    print(link)