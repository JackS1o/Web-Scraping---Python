from playwright.sync_api import sync_playwright
from flask import Flask, jsonify

app = Flask(__name__)


def get_laptops(p):
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto(
        'https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops')
    laptop_data = []
    laptops = page.query_selector_all('div.thumbnail')
    for laptop in laptops:
        title = laptop.query_selector('a.title').inner_text()
        price = laptop.query_selector('h4.pull-right').inner_text()
        description = laptop.query_selector('p').inner_text()
        rating = laptop.query_selector('p.pull-right').inner_text()
        laptop_data.append({
            'title': title,
            'price': float(price[1:]),
            'description': description,
            'rating': rating,
        })
    browser.close()
    lenovo_laptops = list(
        filter(lambda x: 'Lenovo' in x['description'], laptop_data))
    sorted_list = sorted(lenovo_laptops, key=lambda x: x['price'])
    return sorted_list


@app.route('/', methods=['GET'])
def main():
    with sync_playwright() as p:
        result = get_laptops(p)
    return jsonify(result)


if __name__ == '__main__':
    app.run()
