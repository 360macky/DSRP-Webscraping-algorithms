# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import pandas as pd

# El Comercio ✔️

article = {
    'url': 'https://elcomercio.pe/lima/sucesos/la-marcha-del-bicentenario-un-mes-despues-un-reportaje-especial-con-la-voz-de-sus-protagonistas-noticia/?ref=ecr',
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

pd.DataFrame([article])

"""## La República ✔️

El patrón de los artículos de noticias de *El Comercio*, 

---

suelen tener esta URL:

`
https://larepublica.pe + /sección/ + año / mes / día + /nombre-del-articulo
`
"""

article = {
    'url': 'https://larepublica.pe/politica/2020/12/15/acusan-a-alarcon-de-haber-recibido-dos-millones-de-soles/',
    'ponderacion': 0.0,
    'verificabilidad': False
}

article_request = requests.get(article['url'])
article_soup = BeautifulSoup(article_request.text, 'lxml')

article['nombre'] = article_soup.find('h1', attrs={'class': 'DefaultTitle'}).get_text()
article['contenido'] = ''

paragraphs = article_soup.find('div', attrs={'class': 'page-internal-content'}).find('section').findAll('p')
for paragraph in paragraphs:
  article['contenido'] += paragraph.get_text()

article['autoria'] = article_soup.find('a', attrs={'class': 'click_perfil'}).find('strong').get_text()
article['seccion'] = article_soup.find('a', attrs={'class': 'DefaultSectionA'}).get_text()
article['fecha_de_publicacion'] = article_soup.find('div', attrs={'class': 'comp-autor-dateTime'}).find('time').get('datetime')

if article['url'].startswith('https://larepublica.pe/'):
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

"""## TV Perú ✔️"""

article = {
    'url': 'https://www.tvperu.gob.pe/noticias/nacionales/ejecutivo-dicta-toque-de-queda-de-10-pm-a-4-am-en-seis-regiones',
    'ponderacion': 0.0,
    'verificabilidad': False
}

article_request = requests.get(article['url'])
article_soup = BeautifulSoup(article_request.text, 'lxml')

article['nombre'] = article_soup.find('div', attrs={'id': 'content'}).find('h1').get_text()
article['contenido'] = article_soup.find('div', attrs={'class': 'paragraph'}).get_text()
article['autoria'] = None
article['seccion'] = article_soup.find('h1').get_text()
article['fecha_de_publicacion'] = article_soup.find('span', attrs={'class': 'date-display-single'}).get('content')

if article['url'].startswith('https://www.tvperu.gob.pe/'):
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

article2 = {
    'url': 'https://www.tvperu.gob.pe/noticias/nacionales/pfizer-confirma-que-enviara-al-peru-1-millon-50-mil-vacunas-entre-marzo-y-abril',
    'ponderacion': 0.0,
    'verificabilidad': False
}

article_request = requests.get(article2['url'])
article_soup = BeautifulSoup(article_request.text, 'lxml')

article2['nombre'] = article_soup.find('div', attrs={'id': 'content'}).find('h1').get_text()
article2['contenido'] = article_soup.find('div', attrs={'class': 'paragraph'}).get_text()
article2['autoria'] = None
article2['seccion'] = article_soup.find('h1').get_text()
article2['fecha_de_publicacion'] = article_soup.find('span', attrs={'class': 'date-display-single'}).get('content')

if article2['url'].startswith('https://www.tvperu.gob.pe/'):
  article2['ponderacion'] += 0.3

if article2['autoria'] is not None:
  article2['ponderacion'] += 0.1

try:
  article['tweet'] = article_soup.find('blockquote', attrs={'class': 'twitter-tweet'}).get_text()
  article['ponderacion'] += 0.1
except:
  article['tweet'] = None

if article2['fecha_de_publicacion'] is not None:
  article2['ponderacion'] += 0.1

if article2['ponderacion'] >= 0.6:
  article2['verificabilidad'] = True

article3 = {
    'url': 'https://www.tvperu.gob.pe/noticias/nacionales/gustavo-rivara-falta-muchos-estudios-y-evidencia-cientifica-para-poder-empezar-la-vacunacion-en-gestantes',
    'ponderacion': 0.0,
    'verificabilidad': False
}

article_request = requests.get(article3['url'])
article_soup = BeautifulSoup(article_request.text, 'lxml')

article3['nombre'] = article_soup.find('div', attrs={'id': 'content'}).find('h1').get_text()
article3['contenido'] = article_soup.find('div', attrs={'class': 'paragraph'}).get_text()
article3['autoria'] = None
article3['seccion'] = article_soup.find('h1').get_text()
article3['fecha_de_publicacion'] = article_soup.find('span', attrs={'class': 'date-display-single'}).get('content')

if article3['url'].startswith('https://www.tvperu.gob.pe/'):
  article3['ponderacion'] += 0.3

if article3['autoria'] is not None:
  article3['ponderacion'] += 0.1

try:
  article3['tweet'] = article_soup.find('blockquote', attrs={'class': 'twitter-tweet'}).get_text()
  article3['ponderacion'] += 0.1
except:
  article3['tweet'] = None

if article3['fecha_de_publicacion'] is not None:
  article3['ponderacion'] += 0.1

if article3['ponderacion'] >= 0.6:
  article3['verificabilidad'] = True

article4 = {
    'url': 'https://www.tvperu.gob.pe/noticias/politica/maria-antonieta-alva-no-he-participado-en-ningun-ensayo-clinico-para-la-vacuna-contra-el-covid-19',
    'ponderacion': 0.0,
    'verificabilidad': False
}

article_request = requests.get(article4['url'])
article_soup = BeautifulSoup(article_request.text, 'lxml')

article4['nombre'] = article_soup.find('div', attrs={'id': 'content'}).find('h1').get_text()
article4['contenido'] = article_soup.find('div', attrs={'class': 'paragraph'}).get_text()
article4['autoria'] = None
article4['seccion'] = article_soup.find('h1').get_text()
article4['fecha_de_publicacion'] = article_soup.find('span', attrs={'class': 'date-display-single'}).get('content')

if article4['url'].startswith('https://www.tvperu.gob.pe/'):
  article4['ponderacion'] += 0.3

if article4['autoria'] is not None:
  article4['ponderacion'] += 0.1

try:
  article4['tweet'] = article_soup.find('blockquote', attrs={'class': 'twitter-tweet'}).get_text()
  article4['ponderacion'] += 0.1
except:
  article4['tweet'] = None

if article4['fecha_de_publicacion'] is not None:
  article4['ponderacion'] += 0.1

if article4['ponderacion'] >= 0.6:
  article4['verificabilidad'] = True

article5 = {
    'url': 'https://www.tvperu.gob.pe/noticias/politica/keiko-fujimori-rechazo-pedido-de-napoleon-vigo-para-vacunar-a-congresistas-la-prioridad-la-tiene-la-primera-linea',
    'ponderacion': 0.0,
    'verificabilidad': False
}

article_request = requests.get(article5['url'])
article_soup = BeautifulSoup(article_request.text, 'lxml')

article5['nombre'] = article_soup.find('div', attrs={'id': 'content'}).find('h1').get_text()
article5['contenido'] = article_soup.find('div', attrs={'class': 'paragraph'}).get_text()
article5['autoria'] = None
article5['seccion'] = article_soup.find('h1').get_text()
article5['fecha_de_publicacion'] = article_soup.find('span', attrs={'class': 'date-display-single'}).get('content')

if article5['url'].startswith('https://www.tvperu.gob.pe/'):
  article5['ponderacion'] += 0.3

if article5['autoria'] is not None:
  article5['ponderacion'] += 0.1

try:
  article5['tweet'] = article_soup.find('blockquote', attrs={'class': 'twitter-tweet'}).get_text()
  article5['ponderacion'] += 0.1
except:
  article5['tweet'] = None

if article5['fecha_de_publicacion'] is not None:
  article5['ponderacion'] += 0.1

if article5['ponderacion'] >= 0.6:
  article5['verificabilidad'] = True

df = pd.DataFrame([article, article2, article3,article4,article5])
df

"""## RPP ✔️"""

article = {
    'url': 'https://rpp.pe/politica/elecciones/el-candidato-presidencial-julio-guzman-dio-positivo-a-la-covid-19-noticia-1316640',
    'ponderacion': 0.0,
    'verificabilidad': False
}

article_request = requests.get(article['url'])
article_soup = BeautifulSoup(article_request.text, 'lxml')
article['nombre'] = article_soup.find('header', attrs={'class': 'story-header'}).find('h1').get_text()
article['contenido'] = ''
article_body = article_soup.find('div', attrs={'id': 'article-body'}).find_all('p')
for paragraph in article_body:
  article['contenido'] += paragraph.get_text()
article['autoria'] = None
article['seccion'] = article_soup.find('div', attrs={'class': 'story-top'}).find('span').get_text()
article['fecha_de_publicacion'] = article_soup.find('time').get('datetime')

if article['url'].startswith('https://rpp.pe/'):
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



article2 = {
    'url': 'https://rpp.pe/lima/actualidad/coronavirus-en-peru-joven-denuncia-presunta-suplantacion-de-identidad-en-el-portal-para-solicitar-pase-laboral-noticia-1320751'
}
article_request = requests.get(article2['url'])
article_soup = BeautifulSoup(article_request.text, 'lxml')
article2['nombre'] = article_soup.find('header', attrs={'class': 'story-header'}).find('h1').get_text()
article2['contenido'] = ''
article_body = article_soup.find('div', attrs={'id': 'article-body'}).find_all('p')
for paragraph in article_body:
  article2['contenido'] += paragraph.get_text()
article2['autoria'] = None
try:
  article2['seccion'] = article_soup.find('div', attrs={'class': 'story-top'}).find('span').get_text()
except:
  article2['seccion'] = None

article2['fecha_de_publicacion'] = article_soup.find('time').get('datetime')

article3 = {
    'url': 'https://rpp.pe/politica/gobierno/coronavirus-peru-francisco-sagasti-advierte-que-intervendra-de-la-manera-mas-dura-si-una-empresa-se-niega-a-disponer-de-oxigeno-noticia-1320838'
}
article_request = requests.get(article3['url'])
article_soup = BeautifulSoup(article_request.text, 'lxml')
article3['nombre'] = article_soup.find('header', attrs={'class': 'story-header'}).find('h1').get_text()
article3['contenido'] = ''
article_body = article_soup.find('div', attrs={'id': 'article-body'}).find_all('p')
for paragraph in article_body:
  article3['contenido'] += paragraph.get_text()
article3['autoria'] = None
article3['seccion'] = article_soup.find('div', attrs={'class': 'story-top'}).find('span').get_text()
article3['fecha_de_publicacion'] = article_soup.find('time').get('datetime')
article_request.status_code

article4 = {
    'url': 'https://rpp.pe/politica/gobierno/coronavirus-peru-francisco-sagasti-advierte-que-intervendra-de-la-manera-mas-dura-si-una-empresa-se-niega-a-disponer-de-oxigeno-noticia-1320838'
}
article_request = requests.get(article2['url'])
article_soup = BeautifulSoup(article_request.text, 'lxml')
article2['nombre'] = article_soup.find('header', attrs={'class': 'story-header'}).find('h1').get_text()
article2['contenido'] = ''
article_body = article_soup.find('div', attrs={'id': 'article-body'}).find_all('p')
for paragraph in article_body:
  article['contenido'] += paragraph.get_text()
article2['autoria'] = None
try:
  article2['seccion'] = article_soup.find('div', attrs={'class': 'story-top'}).find('span').get_text()
except:
  article2['seccion'] = None
article2['fecha_de_publicacion'] = article_soup.find('time').get('datetime')

article5 = {
    'url': 'https://rpp.pe/politica/gobierno/coronavirus-peru-francisco-sagasti-advierte-que-intervendra-de-la-manera-mas-dura-si-una-empresa-se-niega-a-disponer-de-oxigeno-noticia-1320838'
}
article_request = requests.get(article2['url'])
article_soup = BeautifulSoup(article_request.text, 'lxml')
article2['nombre'] = article_soup.find('header', attrs={'class': 'story-header'}).find('h1').get_text()
article2['contenido'] = ''
article_body = article_soup.find('div', attrs={'id': 'article-body'}).find_all('p')
for paragraph in article_body:
  article['contenido'] += paragraph.get_text()
article2['autoria'] = None
# article2['seccion'] = article_soup.find('div', attrs={'class': 'story-top'}).find('span').get_text()
article2['fecha_de_publicacion'] = article_soup.find('time').get('datetime')
article_request.status_code

pd.DataFrame([article,article2])

"""## Alexa ✔️

El patrón de información de los principales portales de noticias provistos por *Alexa*:

`https://www.alexa.com/ siteinfo / + URL del portal de noticias`
"""

def get_rank_of_news_portal(url):
  url_media = f'https://www.alexa.com/siteinfo/{url}'
  url_media_request = requests.get(url_media)
  url_media_soup = BeautifulSoup(url_media_request.text, 'lxml')
  return url_media_soup.find('div', attrs={'class': 'rankmini-rank'}).get_text().strip().replace('#', '').replace(',', '')

"""Gracias a los datos provistos por Alexa podemos determinar el tráfico recibido por un portal de noticias en las últimas 24 horas, a través de un *Rank*.

Más cerca al 0, mayor popularidad
"""

media_information_example = [
                             {
                                 'url': 'elcomercio.pe',
                                 'rank': get_rank_of_news_portal('elcomercio.pe')
                             },
                             {
                                 'url': 'larepublica.pe',
                                 'rank': get_rank_of_news_portal('larepublica.pe')
                             },
                             {
                                 'url': 'rpp.pe',
                                 'rank': get_rank_of_news_portal('rpp.pe')
                             },
                             {
                                 'url': 'tvperu.gob.pe',
                                 'rank': get_rank_of_news_portal('tvperu.gob.pe')
                             },

                             {
                                 'url': 'ojo-publico.com',
                                 'rank': get_rank_of_news_portal('ojo-publico.com')
                             },
]

dataframe_media_information = pd.DataFrame(media_information_example)

# Ordernar desde el más visitado hasta el menos visitado en un conjunto de portales de noticias de ejemplo

dataframe_media_information.sort_values(by= "rank", ascending=False)
