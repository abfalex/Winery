import pandas
import collections
import argparse

from http.server import HTTPServer, SimpleHTTPRequestHandler
from datetime import datetime
from jinja2 import Environment, FileSystemLoader, select_autoescape


def format_winery_age(winery_age):
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

    formatted_winery_age = format_winery_age(winery_age)

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
    winery_foundation_year = 1920

    env = Environment(
        loader=FileSystemLoader("."),
        autoescape=select_autoescape(["html", "xml"])
    )

    parser = argparse.ArgumentParser(
        prog='Winery'
    )

    parser.add_argument(
        '--wine_file',
        type=str,
        default="wine.xlsx",
        help='Укажите excel-файл с винами',
    )

    args = parser.parse_args()
    wines_path = args.wine_file

    template = env.get_template("template.html")

    winery_age = datetime.now().year - winery_foundation_year
    wines = read_data_from_excel(wines_path)

    update_page(wines, winery_age, template)

    server = HTTPServer(("0.0.0.0", 8000), SimpleHTTPRequestHandler)
    server.serve_forever()


if __name__ == "__main__":
    main()
