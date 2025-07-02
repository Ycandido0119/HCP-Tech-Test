from csv import DictReader


def load_books():
    with open("books.csv") as f:
        yield list(DictReader(f))


def load_sales():
    with open("sales.csv") as f:
        yield list(DictReader(f))


def total_revenue():
    books = load_books()
    sales = load_sales()

    # TODO
