from collections import defaultdict
from csv import DictReader
import datetime
import csv
from pathlib import Path
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


# Main execution
if __name__ == "__main__":
    base_dir = Path(__file__).resolve().parent
    books = read_books_from_csv_file(base_dir / "files" / "books.csv")
    sales = read_sales_from_csv_file(base_dir / "files" / "sales.csv")

# Book lookup
book_lookup = {book.ISBN: book for book in books}

# Filter sales for 2023
sales_for_2023 = [sale for sale in sales if sale.date.year == 2023]

# Initialise summary data structures
total_units_by_book = defaultdict(int)
total_revenue_by_book = defaultdict(float)
totals_units_overall = 0
totals_revenue_overall = 0.0
shop_totals = defaultdict(lambda: {"units": 0, "revenue": 0.0})
category_books = defaultdict(list)

# Process each sale
for sale in sales_for_2023:
    book = book_lookup[sale.ISBN]
    quantity = sale.quantity
    revenue = quantity * book.unit_price

    total_units_by_book[book.ISBN] += quantity
    total_revenue_by_book[book.ISBN] += revenue

    totals_units_overall += quantity
    totals_revenue_overall += revenue

    shop_totals[sale.seller]["units"] += quantity
    shop_totals[sale.seller]["revenue"] += revenue

# Determine book with the highest revenue
if total_revenue_by_book:
    top_isbn = max(total_revenue_by_book, key=total_revenue_by_book.get)
    top_book = book_lookup[top_isbn]
    top_book_revenue = total_revenue_by_book[top_isbn]

    print("Book with the highest overall revenue:")
    print(f"{top_book.title} ({top_book.binding}) by {top_book.author}")
    print(f"Total Revenue: £{top_book_revenue:,.2f}\n")

# Grouping books by category
for isbn, units in total_units_by_book.items():
    book = book_lookup[isbn]
    category_books[book.category].append((book, units))

# Print top selling book per category
print("Top selling book by each category:")
for category, books_list in category_books.items():
    top_book, max_units = max(books_list, key=lambda x: x[1])
    revenue = max_units * top_book.unit_price
    print(f"{category} - {top_book.title} - {max_units:,} sales, £{revenue:,.2f}")
print()

# Print totals by shop
print("Sales totals by shop:")
for shop, totals in shop_totals.items():
    print(f"{shop} - {totals['units']:,} sales, £{totals['revenue']:,.2f}")
print()

# Print overall totals
print("      Summary of Sales      ")
print(f"Total sold in 2023: {totals_units_overall:,} units, £{totals_revenue_overall:,.2f}\n")

# Compute sales summary across all years
sales_summary = defaultdict(lambda: {"units": 0, "revenue": 0.0})
for sale in sales:
    sales_summary[sale.ISBN]["units"] += sale.quantity
    book_price = book_lookup[sale.ISBN].unit_price
    sales_summary[sale.ISBN]["revenue"] += sale.quantity * book_price

# Print sales summary
print("Sales Summary:\n")

max_revenue = 0.0
best_selling_ISBN = None

for isbn, summary in sales_summary.items():
    book = book_lookup[isbn]
    print(f"{book.title} ({book.binding}) by {book.author}")
    print(f" Units Sold: {summary['units']:,}")
    print(f" Total Revenue: £{summary['revenue']:,.2f}\n")

    if summary["revenue"] > max_revenue:
        max_revenue = summary["revenue"]
        best_selling_ISBN = isbn

if best_selling_ISBN:
    best_book = book_lookup[best_selling_ISBN]
    print("The book with the highest revenue is:")
    print(f"{best_book.title} ({best_book.binding}) by {best_book.author}")
    print(f"Total Revenue: £{max_revenue:,.2f}")