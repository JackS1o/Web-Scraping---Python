import requests
from parsel import Selector


def get_page(url):
    try:
        response = requests.get(url)
    except requests.exceptions.RequestException:
        return None
    else:
        return response.text


def extract_data(html):
    selector = Selector(text=html)
    laptop_data = []
    for laptop in selector.css('div.thumbnail'):
        title = laptop.css('a.title::text').get()
        price = laptop.css('h4.pull-right::text').get()
        description = laptop.css('p::text').get()
        rating = laptop.css('p.pull-right::text').get()
        laptop_data.append({
            'title': title,
            'price': float(price[1:]),
            'description': description,
            'rating': rating
        })
    lenovo_laptops = list(filter(lambda x: 'Lenovo' in x['title'], laptop_data))
    sorted_list = sorted(lenovo_laptops, key=lambda x: x['price'])
    return sorted_list


if __name__ == '__main__':
    html_text = get_page(
        'https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops')
    laptop_data = extract_data(html_text)
    print(laptop_data[0]['price'])
