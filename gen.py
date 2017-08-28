import csv
import os
import sys

import jinja2


def main(argv):
    csv_in = csv.DictReader(sys.stdin)
    rows = [{key: value.decode('utf-8') for key, value in row.items()}
            for row in csv_in]

    env = jinja2.Environment(
        autoescape=True,
        loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))
    template = env.get_template('template.html')
    sys.stdout.write(template.render(devices=rows).encode('utf-8'))


if __name__ == '__main__':
    sys.exit(main(sys.argv))
