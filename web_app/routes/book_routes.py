# web_app/routes/book_routes.py

from flask import Blueprint, jsonify

book_routes = Blueprint("book_routes", __name__)

@book_routes.route("/api/books")
@book_routes.route("/api/books.json")
def list_books():
    print("BOOKS...")
    books = [
        {"id": 1, "title": "Book 1", "year": 1957},
        {"id": 2, "title": "Book 2", "year": 1990},
        {"id": 3, "title": "Book 3", "year": 2031},
    ] # some dummy / placeholder data
    return jsonify(books)

@book_routes.route("/api/books/<int:book_id>")
@book_routes.route("/api/books/<int:book_id>.json")
def get_book(book_id):
    print("BOOK...", book_id)
    book = {"id": book_id, "title": f"Example Book", "year": 2000} # some dummy / placeholder data
    return jsonify(book)

