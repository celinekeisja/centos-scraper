from requests import get
from bs4 import BeautifulSoup
import re
import csv
# filename,download_link,filesize


def recr(files):
    table = soup.find('table')
    rows = table.find_all('tr')
    if 'str'.endswith('/'):
        csv_file(rows)
        'list files'
    else:
        recr()


def csv_file(rows):
    with open(f'test.csv', 'a', newline='') as csv_file:
        field_n = ['filename', 'download_link', 'filesize']
        writer = csv.DictWriter(csv_file, fieldnames=field_n)
        writer.writeheader()
        for row in rows[3:-1]:
            tds = row.find_all('td')
            d = {"filename": tds[1].text, "download_link": tds[1].href, "filesize": tds[3].text}
            print(d)
            writer.writerow(d)
    return 'here'


if __name__ == "__main__":
    url = 'http://mirror.rise.ph/centos/7/'
    response = get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    files=[]
    recr(files)
    csv_file()
