# https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313&_nkw=renault+r12&_sacat=0
from bs4 import BeautifulSoup as bs
import requests


def main():
    headers = ({'User-Agent':
                    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
                'Accept-Language': 'en-US, en;q=0.5'})
    urls = ['https://www.ebay.com/itm/284806929955?hash=item424fd0de23:g:wCoAAOSwf8hieS5O',
            # 'https://www.ebay.com/itm/165481842789?hash=item26877c8865:g:5sUAAOSwcrph0Twb',
            # 'https://www.ebay.com/itm/170751082764?epid=1158289445&hash=item27c18ec10c:g:frIAAOSwTm1dZj7Y',
            # 'https://www.ebay.com/itm/154787458344?hash=item240a0d2d28:g:hdcAAOSwyG5h2oSp',
            # 'https://www.ebay.com/itm/363832730644?hash=item54b61ee414:g:-ZAAAOSw3xFieRc2',
            # 'https://www.ebay.com/itm/353958257450?hash=item52698e632a:g:B68AAOSwA-NhYzWW'
            ]

    for url in urls:
        page = requests.get(url, headers=headers)
        soup = bs(page.text, 'html.parser')
        title_parent = soup.find('h1', {'class': 'x-item-title__mainTitle'})
        title = title_parent.find('span', {'class': 'ux-textspans ux-textspans--BOLD'}).text

        price_parent = soup.find('div', {'class': 'mainPrice'})
        price = price_parent.find('span', {'class': 'notranslate'}).text
        # price = price.split('EUR')[1]

        shipping_cost_parent = soup.find('div', {'class': 'ux-labels-values col-12 ux-labels-values--shipping'})
        shipping_cost = shipping_cost_parent.find('span', {'class': 'ux-textspans ux-textspans--BOLD'}).text
        print(shipping_cost)

        # todo write in file the result, and than everytime compare with the results
        # print(f'\nTitlul cartii: {title}Autorul: {author} \nAnul de publicare: {year}\n-------------------------------')


if __name__ == '__main__':
    main()
