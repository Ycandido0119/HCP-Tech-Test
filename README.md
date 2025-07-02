# HarperCollins Python Test

## The Challenge

The aim of this exercise is to demonstrate your problem-solving skills and understanding of Python.

You are provided with two CSV files:

- **books.csv** – containing a list of books
- **sales.csv** – containing a list of sales

Using this raw data, implement the following functionality:

---

### 1. Total amount and number of all transactions

Example output:

200 sales, £1,500

yaml
Copy
Edit

---

### 2. Display the top-selling book (by units sold) in each category for 2023 and its sales

Example output:

Children's - Billionaire Boy - 100 sales, £1,000

yaml
Copy
Edit

*(one line for each category)*

---

### 3. List all shops and their total sales

Example output:

Amazon - 1000 sales, £100,000

yaml
Copy
Edit

*(one line for each shop)*

---

### Additional Notes

- Books may be sold in different bindings (e.g. paperback, hardcover). Combine all sales for all bindings to determine the overall sales for each book.
- You may add as many functions as you like to structure your code.

---

## How to Submit

- Please develop your solution in a Git repository.
- Start by creating an initial commit containing the contents of the provided zip file.
- When finished, use the `git archive` command to package your solution and submit it via email.

---

## Additional Terms

- Credit will be given for:
  - Approach
  - Correctness
  - Clean, maintainable code
  - Tests
- There’s no strict time limit, but as guidance, a senior developer might complete this in around an hour.
- **Please do not use external libraries** (except for a testing library).
- You may use online resources for specific techniques or syntax — but please do **not** simply copy code.
- Please do not share this exercise with anyone else.

---

## Instructions for Running

- To run the main program:

    ```bash
    python3 main.py
    ```

    This will execute the script and print all outputs.

- To run the test suite:

    ```bash
    python3 test_main.py
    ```

---

Good luck!