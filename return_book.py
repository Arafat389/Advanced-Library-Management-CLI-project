from save_all_books import save_all_books
from save_lends import save_lends
def return_book(all_books, lends):
    if not lends:
        print("No books are currently lent.")
        return

    for idx, lend in enumerate(lends, start=1):
        print(f"{idx}. {lend['book_title']} lent to {lend['borrower_name']} (Phone: {lend['borrower_phone']}), Due: {lend['return_date']}")

    index = int(input("Enter the number of the lend record to return: ")) - 1
    if 0 <= index < len(lends):
        lend = lends.pop(index)

        for book in all_books:
            if book['title'] == lend['book_title']:
                book['quantity'] += 1
                break

        save_lends(lends)
        save_all_books(all_books)
        print(f"Book '{lend['book_title']}' returned successfully!")
    else:
        print("Invalid lend record number.")