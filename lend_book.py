
from save_all_books import save_all_books
from save_lends import save_lends

def lend_book(all_books, lends):
    save_all_books(all_books)
    if not all_books:
        return

    index = int(input("Enter the number of the book to lend: ")) - 1
    if 0 <= index < len(all_books):
        if all_books[index]['quantity'] > 0:
            borrower_name = input("Enter borrower's name: ")
            borrower_phone = input("Enter borrower's phone: ")
            return_date = input("Enter return due date (DD-MM-YYYY): ")

            lend = {
                "borrower_name": borrower_name,
                "borrower_phone": borrower_phone,
                "book_title": all_books[index]['title'],
                "return_date": return_date
            }

            lends.append(lend)
            all_books[index]['quantity'] -= 1

            save_lends(lends)
            save_all_books(all_books)
            print(f"Book '{all_books[index]['title']}' lent successfully!")
        else:
            print("Not enough books are available to lend.")
    else:
        print("Invalid book number.")