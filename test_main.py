import unittest

from main import Book, Sale

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

if __name__ == "__main__":
    unittest.main()
