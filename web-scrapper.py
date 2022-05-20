import json

from bs4 import BeautifulSoup as bs
import requests


def get_data(urls):
    headers = ({'User-Agent':
                    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
                'Accept-Language': 'en-US, en;q=0.5'})
    new_data_array = []
    for url in urls:
        page = requests.get(url, headers=headers)
        soup = bs(page.text, 'html.parser')
        title_parent = soup.find('h1', {'class': 'x-item-title__mainTitle'})
        title = title_parent.find('span', {'class': 'ux-textspans ux-textspans--BOLD'}).text

        price_parent = soup.find('div', {'class': 'mainPrice'})
        text_price = price_parent.find('span', {'class': 'notranslate'}).text
        price = float(text_price.split('EUR')[1].strip())
        # print(text_price.split())
        currency = text_price.split()[0]

        shipping_cost_parent = soup.find('div', {'class': 'ux-labels-values col-12 ux-labels-values--shipping'})
        shipping_cost = shipping_cost_parent.find('span', {'class': 'ux-textspans ux-textspans--BOLD'}).text
        # print(shipping_cost.split('EUR'))
        if shipping_cost == 'FREE':
            shipping_cost = 0
        else:
            shipping_cost = float(shipping_cost.split('EUR')[1].strip())

        print(f'Obiectul: {title} are un pret de: {price} {currency}, iar transportul: {shipping_cost} {currency} \n')
        information = {
            "price": price,
            "currency": currency,
            "title": title,
            "shipping_cost": shipping_cost
        }
        new_data_array.append(information)
    return new_data_array


def write_json(data_array, filename="sample.json"):
    json_string = json.dumps(data_array)

    with open(filename, "w") as outfile:
        outfile.write(json_string)


def main():
    urls = ['https://www.ebay.com/itm/284806929955?hash=item424fd0de23:g:wCoAAOSwf8hieS5O',
            'https://www.ebay.com/itm/165481842789?hash=item26877c8865:g:5sUAAOSwcrph0Twb',
            'https://www.ebay.com/itm/170751082764?epid=1158289445&hash=item27c18ec10c:g:frIAAOSwTm1dZj7Y',
            'https://www.ebay.com/itm/154787458344?hash=item240a0d2d28:g:hdcAAOSwyG5h2oSp',
            'https://www.ebay.com/itm/363832730644?hash=item54b61ee414:g:-ZAAAOSw3xFieRc2',
            'https://www.ebay.com/itm/353958257450?hash=item52698e632a:g:B68AAOSwA-NhYzWW',
            # 'https://www.ebay.com/itm/294985798533?hash=item44ae861385:g:zfkAAOSwfnhigqH3'
            ]
    data_array = get_data(urls)
    write_json(data_array)


if __name__ == '__main__':
    main()
