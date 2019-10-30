from requests import get
from bs4 import BeautifulSoup
import csv


def recr(url):
    """List files from the directory in a csv file recursively."""
    response = get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.find('table')
    rows = table.find_all('tr')
    for row in rows[3:-1]:
        tds = row.find_all('td')
        filename = tds[1].text
        if filename.strip().endswith('/'):
            recr(url+filename.strip())
        else:
            d = {"filename": filename, "download_link": url+tds[1].a["href"], "filesize": tds[3].text}
            csv_append(d)


def csv_file_headers():
    """Write the csv file headers."""
    with open(f'test.csv', 'w+', newline='') as csv_file:
        field_n = ['filename', 'download_link', 'filesize']
        writer = csv.DictWriter(csv_file, fieldnames=field_n)
        writer.writeheader()
    return ''


def csv_append(d):
    """Append the encountered files in the existing csv file."""
    with open('test.csv', 'a', newline='') as csv_file:
        field_n = ['filename', 'download_link', 'filesize']
        writer = csv.DictWriter(csv_file, fieldnames=field_n)
        writer.writerow(d)
    return ''


if __name__ == "__main__":
    url = 'http://mirror.rise.ph/centos/7/'
    csv_file_headers()
    recr(url)
