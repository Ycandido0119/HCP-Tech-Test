from io import StringIO
import unittest
from unittest.mock import patch

from main import Book, Sale, read_books_from_csv_file, read_sales_from_csv_file

# Test cases for the Book model
class TestBook(unittest.TestCase):
    # Test Book model initialisation
    def test_book_initialisation(self):
        # Arrange
        book = Book(1234567890, "Test Book", "Paperback", "Author Name", "Fiction", 19.99)

        # Assert
        self.assertEqual(book.ISBN, 1234567890)
        self.assertEqual(book.title, "Test Book")
        self.assertEqual(book.binding, "Paperback")
        self.assertEqual(book.author, "Author Name")
        self.assertEqual(book.category, "Fiction")
        self.assertEqual(book.unit_price, 19.99)

    # Test __repr__ method for Book
    def test_book_repr(self):
        # Arrange
        book = Book(1234567890, "Test Book", "Paperback", "Author Name", "Fiction", 19.99)
        expected_repr = (
            "Book(ISBN=1234567890, title='Test Book', binding='Paperback', "
            "author='Author Name', category='Fiction', unit_price=19.99)"
        )

        # Assert
        self.assertEqual(repr(book), expected_repr)


# Test cases for the Sale model
class TestSale(unittest.TestCase):
    # Test Sale model initialisation
    def test_sale_initialisation(self):
        # Arrange
        sale = Sale("2023-10-01", 1234567890, "Seller Name", 5)

        # Assert
        self.assertEqual(sale.date.strftime("%Y-%m-%d"), "2023-10-01")
        self.assertEqual(sale.ISBN, 1234567890)
        self.assertEqual(sale.seller, "Seller Name")
        self.assertEqual(sale.quantity, 5)

    # Test __repr__ method for Sale
    def test_sale_repr(self):
        # Arrange
        sale = Sale("2023-10-01", 1234567890, "Seller Name", 5)
        expected_repr = (
            "Sale(date=2023-10-01, ISBN=1234567890, seller='Seller Name', "
            "quantity=5)"
        )

        # Assert
        self.assertEqual(repr(sale), expected_repr)

# Test cases for reading from CSV files

class TestCSVReading(unittest.TestCase):
    def setUp(self):
        # Common test data for books and sales in memory
        self.book_csv_data = StringIO(
            "ISBN,Title,Binding,Author,Category,Unit price\n"
            "1234567890,Test Book,Paperback,Author Name,Fiction,19.99\n"
        )
        self.sale_csv_data = StringIO(
            "Date,ISBN,Seller,Quantity\n"
            "2023-10-01,1234567890,Seller Name,5\n"
        )

    # Test reading books from CSV
    @patch("builtins.open")
    def test_read_books_from_csv_file(self, mock_open):
        # Arrange
        mock_open.return_value.__enter__.return_value = self.book_csv_data

        # Act
        books = read_books_from_csv_file("dummy/path/books.csv")

        # Assert
        self.assertEqual(len(books), 1)
        self.assertEqual(books[0].title, "Test Book")

    # Test reading sales from CSV
    @patch("builtins.open")
    def test_read_sales(self, mock_open):
        # Arrange
        mock_open.return_value.__enter__.return_value = self.sale_csv_data

        # Act
        sales = read_sales_from_csv_file("dummy/path/sales.csv")

        # Assert
        self.assertEqual(len(sales), 1)
        self.assertEqual(sales[0].seller, "Seller Name")

    # Test reading from an empty book CSV
    @patch("builtins.open")
    def test_read_books_from_empty_csv(self, mock_open):
        empty_book_csv_data = StringIO("ISBN,Title,Binding,Author,Category,Unit price\n")
        mock_open.return_value.__enter__.return_value = empty_book_csv_data

        books = read_books_from_csv_file("dummy/path/empty_books.csv")
        self.assertEqual(books, [])

    # Test reading from an empty sales CSV
    @patch("builtins.open")
    def test_read_sales_from_empty_csv(self, mock_open):
        empty_sales_csv_data = StringIO("date,ISBN,Seller,Quantity\n")
        mock_open.return_value.__enter__.return_value = empty_sales_csv_data

        sales = read_sales_from_csv_file("dummy/path/empty_sales.csv")
        self.assertEqual(sales, [])

    # Test for invalid price in books CSV
    @patch("builtins.open")
    def test_books_file_with_invalid_price(self, mock_open):
        bad_csv = StringIO("ISBN,Title,Binding,Author,Category,Unit price\n"
                           "1234567890,Book,Paperback,Author,Fiction,not_a_number\n")
        mock_open.return_value.__enter__.return_value = bad_csv

        with self.assertRaises(ValueError):
            read_books_from_csv_file("dummy/path/books.csv")

    # Test for invalid date in sales CSV
    @patch("builtins.open")
    def test_sales_with_bad_date(self, mock_open):
        bad_date_csv = StringIO("Date,ISBN,Seller,Quantity\n"
                                "01-06-2023,1234567890,Shop A,3\n")
        mock_open.return_value.__enter__.return_value = bad_date_csv

        with self.assertRaises(ValueError):
            read_sales_from_csv_file("dummy/path/sales.csv")


if __name__ == "__main__":
    unittest.main()
