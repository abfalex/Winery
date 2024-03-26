import pandas
import collections

from http.server import HTTPServer, SimpleHTTPRequestHandler
from pprint import pprint
from datetime import datetime
from jinja2 import Environment, FileSystemLoader, select_autoescape

env = Environment(
    loader=FileSystemLoader("."),
    autoescape=select_autoescape(["html", "xml"])
)

template = env.get_template("template.html")

winery_age = datetime.now().year - 1920


def formatted_year_handler():
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


def update_page(wines):
    categories = collections.defaultdict(list)

    for wine in wines:
        categories[wine['Категория']].append(wine)

    rendered_page = template.render(
        categories=categories,
        company_age=winery_age,
        formatted_year=formatted_year_handler()
    )

    with open("index.html", "w", encoding="utf8") as file:
        file.write(rendered_page)


wines = read_data_from_excel("wine3.xlsx")

update_page(wines)

server = HTTPServer(("0.0.0.0", 8000), SimpleHTTPRequestHandler)
server.serve_forever()
