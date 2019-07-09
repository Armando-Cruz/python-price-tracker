# Seguidor de Precios
import urllib.request
from bs4 import BeautifulSoup

# URL a  la que se hará la petición  
url = 'https://www.amazon.com.mx/Xiaomi-Brazalete-Inteligente-MGW4041ZGL-Version/dp/B07G7MBP49/ref=sr_1_1?__mk_es_MX=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=12TF9U28807VS&keywords=xiaomi+mi+band+3&qid=1562251333&s=gateway&sprefix=xiaomi+mi%2Caps%2C293&sr=8-1'


response = None
try:
    response = urllib.request.urlopen(url)
except Exception as err:
    print('Ocurrió un error al hacer la petición', err)
if (response):
    data = response.read()
    page = BeautifulSoup(data, 'html.parser')
    product_title = page.find(id = 'productTitle').get_text().strip()
    product_price = float(page.find(id = 'priceblock_ourprice').get_text()[1:])
    print(f'Producto\n{product_title}\nPrecio: $ {product_price}')