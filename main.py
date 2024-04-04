import pandas
import collections
import argparse

from http.server import HTTPServer, SimpleHTTPRequestHandler
from datetime import datetime
from jinja2 import Environment, FileSystemLoader, select_autoescape

WINERY_FOUNDATION_YEAR = 1920
TEMPLATE_FILE = "template.html"

parser = argparse.ArgumentParser(
    prog='Winery'
)

parser.add_argument(
    'wine_file',
    type=str,
    default="wine.xlsx",
    help='Укажите excel-файл с винами',
)


def winery_age_format_handler(winery_age):
    delta_new = winery_age % 100

    if 21 > delta_new > 4:
        return "лет"

    delta_new = winery_age % 10

    if delta_new == 1:
        return "год"
    elif 1 < delta_new < 5:
        return "года"

    return "лет"


def read_data_from_excel(file_path):
    return pandas.read_excel(file_path).fillna("").to_dict(orient="records")


def update_page(wines, winery_age, template):
    categories = collections.defaultdict(list)

    formatted_winery_age = winery_age_format_handler(winery_age)

    for wine in wines:
        categories[wine['Категория']].append(wine)

    rendered_page = template.render(
        categories=categories,
        wines=wines,
        company_age=winery_age,
        formatted_winery_age=formatted_winery_age
    )

    with open("index.html", "w", encoding="utf8") as file:
        file.write(rendered_page)


def main():
    env = Environment(
        loader=FileSystemLoader("."),
        autoescape=select_autoescape(["html", "xml"])
    )

    args = parser.parse_args()
    wines_path = args.wine_file

    template = env.get_template(TEMPLATE_FILE)

    winery_age = datetime.now().year - WINERY_FOUNDATION_YEAR
    wines = read_data_from_excel(wines_path)

    update_page(wines, winery_age, template)

    server = HTTPServer(("0.0.0.0", 8000), SimpleHTTPRequestHandler)
    server.serve_forever()


if __name__ == "__main__":
    main()
