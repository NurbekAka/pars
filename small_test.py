import requests
import csv
from bs4 import BeautifulSoup


def get_html(url):
    response = requests.get(url)
    return response.text


def get_total_info(html, response):
    soup = BeautifulSoup(response.text, 'lxml')
    pages = soup.find('ul', class_='pagn').find_all("li", class_='pagn-page')
    for page in pages:
            page_href = page.find_all('a')
            for ssylka in page_href:
                ssylka = page_href.get('href')
    total_pages = ssylka.split('=')[1]

    return int(total_pages)
    print(total_pages)


def get_page_info(text):
    name = []
    price = []
    photo_link = []

    soup = BeautifulSoup(text, 'lxml')
    
    ads = soup.find_all('a', class_='name')
    for ad_name in ads:
            name.append(ad_name.string)
    #print('\n'.join(name))
    #print()
    
    prices = soup.find_all('div', class_='price')
    for ad_price in prices:
            price.append(ad_price.string.strip())
    #print('\n'.join(price))

    imgs_a = soup.find_all('a', class_='image-holder')
    for img_a in imgs_a:
        photo_link.append((img_a.find('img')['src']))

    #print('\n'.join(photo_link))

    data = {'name': name,
            'price': price,
            'photo_link': photo_link}
    print (data)
    return data


def write_csv(data):
    with open('lalafo.csv', 'a') as file:
        writer = csv.writer(file)
        info = writer.writerows((data['name'],
                                data['price'],
                                data['photo_link']))
        
    return info


def main():
    url = "https://lalafo.kg/kyrgyzstan/mobilnye-telefony-i-aksessuary/mobilnye-telefony"
    page_part = '?page='
    url_gen = url + page_part + str(i)
    total_page = 3

    for i in total_page:
        html = get_html(url_gen)
        write_csv(get_page_info(html))
        print(url_gen)

        
main()