from requests import get
from bs4 import BeautifulSoup
import csv


def list_files(url):
    """List files from the directory in a CSV file recursively."""
    response = get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.find('table')
    rows = table.find_all('tr')
    for row in rows[3:-1]:
        tds = row.find_all('td')
        filename = tds[1].text
        if filename.strip().endswith('/'):
            list_files(url+filename.strip())
        else:
            d = {"filename": filename, "download_link": url+tds[1].a["href"], "filesize": tds[3].text}
            csv_write(d)


def csv_write(c):
    """CSV writing and appending."""
    if c == 'header':
        with open(f'test.csv', 'w+', newline='') as csv_file:
            field_n = ['filename', 'download_link', 'filesize']
            writer = csv.DictWriter(csv_file, fieldnames=field_n)
            writer.writeheader()
    else:
        with open('test.csv', 'a', newline='') as csv_file:
            field_n = ['filename', 'download_link', 'filesize']
            writer = csv.DictWriter(csv_file, fieldnames=field_n)
            writer.writerow(c)
    return 'csv done.'


if __name__ == "__main__":
    base_url = 'http://mirror.rise.ph/centos/7/'
    csv_write('header')
    list_files(base_url)
