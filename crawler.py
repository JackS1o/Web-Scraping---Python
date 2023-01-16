import requests

def get_page(url):
    try:
        return requests.get(url).text
    except requests.exceptions.RequestException:
        print('Error during requests to {0} : {1}'.format(url, str(e)))
        return None
    
def main():
    url = 'https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops'
    print(get_page(url))

if __name__ == '__main__':
    main()