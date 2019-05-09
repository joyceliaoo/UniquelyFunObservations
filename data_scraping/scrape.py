import sys
import urllib
import csv
import pandas as pd
from bs4 import BeautifulSoup

# retrive html code from given url
def read_url(url):
    with urllib.request.urlopen(url) as fp:
        mybytes = fp.read()
        mystr = mybytes.decode("utf8")
        # print(mystr)
    return mystr

# get all target links on a page
def get_pgs(dir_url):
    direc = read_url(dir_url)
    soup = BeautifulSoup(direc, 'html.parser')
    table = soup.find('table', **{'class': 'results-table'})
    tbody = table.find('tbody')
    links = []
    for tr in tbody.find_all('tr'):
        td = tr.find_all('td')[1]
        link = td.find('a')['href']
        links.append(link)
    return links

# open url for target page and generate dictionary
def read_id(pap_url):
    s = read_url(pap_url)
    soup = BeautifulSoup(s, 'html.parser')
    div = soup.find('div', **{'class': 'view-grid-column metadata-column'})
    d = {}
    for section in div.find_all('section'):
        dts = section.find_all('dt')
        dds = section.find_all('dd')
        for dt, dd in zip(dts, dds):
            key = dt.find('span')
            key.string
            if dd.find('a') is not None:
                dat = dd.find('a').string
            else:
                dat = dd.string
            d[key.string] = dat
    return d

# url = 'https://quod.lib.umich.edu/a/apis/x-16735/K22189R.TIF?auth=world;lasttype=boolean;lastview=reslist;resnum=13;size=50;sort=APIS_INV;start=1;subview=detail;view=entry;rgn1=ic_all;q1=apis'
# d = read_id(url)
# print(d)
# print(get_pgs())
pg_ct=1
with open('raw_data.csv', 'w') as csv_file:
    writer = csv.writer(csv_file)
    for start_num in range(1, 501, 50):
        print("processing listing pg", start_num // 50 + 1)
        dir_url = 'https://quod.lib.umich.edu/a/apis?auth=world;q1=apis;rgn1=ic_all;size=50;sort=APIS_INV;type=boolean;view=reslist;start=' + str(start_num)
        pages = get_pgs(dir_url)
        for page in pages:
            print("reading item pg", ct)
            row = read_id(page)
            writer.writerow(list(row.values()))
            ct += 1
