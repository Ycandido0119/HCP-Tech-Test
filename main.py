from csv import DictReader
import datetime
# Book model
class Book:
    def __init__(self, ISBN, title, binding, author, category, unit_price):
        self.ISBN = int(ISBN)
        self.title = title
        self.binding = binding
        self.author = author
        self.category = category
        self.unit_price = float(unit_price)

    def __repr__(self):
        return (
            f"Book(ISBN={self.ISBN}, title='{self.title}', binding='{self.binding}', "
            f"author='{self.author}', category='{self.category}', unit_price={self.unit_price})"
        )

# Sale model
class Sale:
    def __init__(self, date, ISBN, seller, quantity):
        self.date = datetime.datetime.strptime(date, "%Y-%m-%d").date()
        self.ISBN = int(ISBN)
        self.seller = seller
        self.quantity = int(quantity)

    def __repr__(self):
        return (
            f"Sale(date={self.date}, ISBN={self.ISBN}, seller='{self.seller}', "
            f"quantity={self.quantity})"
        )

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
