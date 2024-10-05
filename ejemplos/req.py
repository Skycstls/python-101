import requests

url = 'https://google.com'
response = requests.get(url)

print(response.apparent_encoding) # Encoding usado para decodificar el contenido
print(response.status_code) # Código de estado de la respuesta
print(response.cookies) # Cookies de la respuesta
print(response.headers) # Cabeceras de la respuesta
print(response.text) # Contenido de la respuesta
print(response.content) # Contenido de la respuesta en bytes
print(response.links) # Links de la respuesta

def url_extractor(text):
    urls = []
    for word in text.split():
        # si la palabra contiene http, la añadimos a la lista
        if 'http' in word:
            urls.append(word)
    return urls

links = url_extractor(response.text)

for link in links:
    print(link)