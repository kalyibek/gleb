import requests
from bs4 import BeautifulSoup as bs
from django.views.decorators.csrf import csrf_exempt


HOST = "https://medcenter.kg/"
URL = "https://medcenter.kg/doctorsmedcenter/"
HEADERS = {
    'Accept': 'image/avif,image/webp,*/*',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0'
}

@csrf_exempt
def get_html(url, params=''):
    req = requests.get(url, headers=HEADERS, params=params)
    return req


@csrf_exempt
def get_data(html):
    soup = bs(html, 'html.parser')
    items = soup.find_all('article', class_='elementor-post elementor-grid-item post-569 doctorsmedcenter type-doctorsmedcenter status-publish format-standard has-post-thumbnail hentry specializationvdoctors-neurologist')
    mediki = []

    for item in items:
        mediki.append(
            {
                'name': item.find('div', class_='elementor-post__text').get_text(),
                'image': item.find('div', class_='elementor-post__thumbnail').find('img').get('src')
            }
        )
        return mediki

@csrf_exempt
def parser():
    html = get_html(URL)
    if html.status_code == 200:
        mediks = []
        for page in range(0, 1):
            html = get_html(URL, params={'page': page})
            mediks.extend(get_data(html.text))
            return mediks
    else:
        raise ValueError('Error in parser function')
