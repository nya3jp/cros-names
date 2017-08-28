#!/usr/bin/python

import csv
import datetime
import sys

import bs4

_DATE_FORMAT = '%B %d, %Y'


def main(argv):
    csv_out = csv.writer(sys.stdout)
    doc = bs4.BeautifulSoup(sys.stdin, 'html5lib')
    table = doc.select('#goog-ws-list-table')[0]
    for tr in table.select('tr'):
        row = [td.get_text().strip() for td in tr.children]
        for i, col in enumerate(row):
            try:
                dt = datetime.datetime.strptime(col, _DATE_FORMAT)
            except ValueError:
                pass
            else:
                row[i] = dt.strftime('%Y-%m-%d')
        csv_out.writerow([t.encode('utf-8') for t in row])


if __name__ == '__main__':
    sys.exit(main(sys.argv))
