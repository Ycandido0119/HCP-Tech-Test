from csv import DictReader
import datetime
import csv
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

# Function to read books from a CSV file
def read_books_from_csv_file(file_path):
    books = []
    with open(file_path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            mapped_row = {
                "ISBN": row["ISBN"],
                "title": row["Title"],
                "binding": row["Binding"],
                "author": row["Author"],
                "category": row["Category"],
                "unit_price": row["Unit price"],
            }
            books.append(Book(**mapped_row))
    return books

# Function to read sales from a CSV file
def read_sales_from_csv_file(file_path):
    sales = []
    with open(file_path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            mapped_row = {
                "date": row["Date"],
                "ISBN": row["ISBN"],
                "seller": row["Seller"],
                "quantity": row["Quantity"],
            }
            sales.append(Sale(**mapped_row))
    return sales


def total_revenue():
    books = load_books()
    sales = load_sales()

    # TODO
