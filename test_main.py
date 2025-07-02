import unittest

from main import total_revenue


class TestTotalRevenue(unittest.TestCase):
    def test_total_revenue(self):
        total_revenue()
        self.assertFalse(True)


if __name__ == "__main__":
    unittest.main()
