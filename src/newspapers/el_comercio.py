import requests
import pandas as pd
from bs4 import BeautifulSoup

test_url = 'https://elcomercio.pe/lima/sucesos/la-marcha-del-bicentenario-un-mes-despues-un-reportaje-especial-con-la-voz-de-sus-protagonistas-noticia/?ref=ecr'

article = {
    'url': test_url, 
    'ponderacion': 0.0,
    'verificabilidad': False
}

article_request = requests.get(article['url'])
article_soup = BeautifulSoup(article_request.text, 'lxml')

article['nombre'] = article_soup.find('h1', attrs={'class': 'sht__title'}).get_text().strip()
article['contenido'] = article_soup.find('div', attrs={'class': 'story-contents__content'}).get_text().strip()
article['autoria'] = article_soup.find('a', attrs={'class': 'story-contents__author-link'}).get_text()
article['seccion'] = article_soup.find('a', attrs={'class': 'st-social__link oflow-h'}).get_text()
article['fecha_de_publicacion'] = article_soup.find('time', attrs={'class': 'story-contents__time'}).get('datetime')

if article['url'].startswith('https://elcomercio.pe/'):
  article['ponderacion'] += 0.3

if article['autoria'] is not None:
  article['ponderacion'] += 0.1

try:
  article['tweet'] = article_soup.find('blockquote', attrs={'class': 'twitter-tweet'}).get_text()
  article['ponderacion'] += 0.1
except:
  article['tweet'] = None

if article['fecha_de_publicacion'] is not None:
  article['ponderacion'] += 0.1

if article['ponderacion'] >= 0.6:
  article['verificabilidad'] = True

pd.DataFrame([article])
