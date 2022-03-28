def addBook(isbn):
    book = {
        "name": "TJs first book",
        "isbn": isbn,
        "aisle": "73234",
        "author": "TJ Khara"
    }
    return book


def header():
    headers = {"Content-Type": "application/json"}
    return headers


def delete_json(book_id):
    return {
        "ID": book_id
    }
