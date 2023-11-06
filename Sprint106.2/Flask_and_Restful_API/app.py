from flask import Flask, jsonify, request, json


app = Flask(__name__)

def loads_books():
    """
        Loads the existing book posts from a JSON file and returns them as a list.

        Returns:
        List[dict]: A list of books posts where each post is represented as a dictionary.
        """
    try:
        with open('books_data.json', 'r') as file_obj:
            list_of_books = json.load(file_obj)
    except (FileNotFoundError, json.JSONDecodeError):
        list_of_books = []

    return list_of_books

books_data = loads_books()

# create a function to save books data  to the json file
def save_books(books):
    """
        Saves the provided list of books posts to a JSON file.

        Args:
        blogs (List[dict]): A list of books posts to be saved.

        Returns:
        None
        """
    with open('books_data.json', 'w') as file_obj:
        json.dump(books, file_obj, indent=2)

# Function to get next available id
def get_next_id(books_data):
    """
     Get the next available ID for a new book entry.

    Args:
        books (list of dict): A list of existing book entries.

    Returns:
        int: The next available ID, which is one greater than the highest ID in the existing entries.
        If no existing entries are found, it returns 1.

    """
    if not books_data:
        return 1
    return max(book['id'] for book in books_data) + 1
# Function to fetch a blog post by id
def find_book_by_id(book_id):

    for book in books_data:
        if book['id'] == book_id:
            return book
    return None

@app.errorhandler(404)
def not_found_error(error):
    return jsonify({"error": "Not Found"}), 404


@app.errorhandler(405)
def method_not_allowed_error(error):
    return jsonify({"error": "Method Not Allowed"}), 405

def validate_book_data(data):
    if "title" not in data or "author" not in data:
        return False
    return True

@app.route('/api/books', methods=['GET', 'POST'])
def get_books():
    """
    Handle GET and POST requests for the '/api/books' endpoint.

    GET request:
    - Returns a list of books as JSON.

    POST request:
    - Accepts JSON data for creating a new book.
    - Validates the JSON data to ensure it contains 'title' and 'author'.
    - Generates a new book entry with a unique ID and adds it to the list of books.
    - Returns the newly created book as JSON with status code 201 (Created) on success.

    Returns:
    - If GET request: A JSON response with a list of books.
    - If POST request succeeds: A JSON response with the newly created book and status code 201.
    - If POST request fails: A JSON response with an error message and status code 400 (Bad Request) for invalid data
    or status code 500 (Internal Server Error) for other exceptions.
    """
    # For now, we'll return a static list
    # Handle the get request
    if request.method == "GET":

        return jsonify(books_data)

    elif request.method == "POST":
        data = request.get_json()
        if not validate_book_data(data):
            return jsonify({"error": "Invalid request data"}), 400

        title = data['title']
        author = data['author']
        try:
            list_of_books = loads_books()
            next_id = get_next_id(list_of_books)

            # creating new books
            new_book = {'id': next_id, 'title': title, 'author': author}

            # Add the new book to the list of the books
            books_data.append(new_book)

            save_books(books_data)

            # Return the new book as a response with status code  201 (Created)
            return jsonify(new_book), 201
        except Exception as e:

            # If the request data is not valid JSON, return an error
            return jsonify({"error": str(e)}), 500

@app.route('/api/books', methods=['GET'])
def handle_books_by_pagination():
    page = int(request.args.get('page', 1))
    limit = int(request.args.get('limit', 10))

    start_index = (page - 1) * limit
    end_index = start_index + limit

    paginated_books = list(books_data.values())[start_index:end_index]

    return jsonify(paginated_books)
# Define the route for getting a specific book by ID
@app.route('/api/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = find_book_by_id(book_id)
    if book is not None:
        return jsonify(book)
    else:
        return jsonify({"error": "Book not found"}), 404

@app.route('/api/books', methods=['GET'])
def handle_books():
    author = request.args.get('author')

    if author:
        # Filter books by author
        filtered_books = [book for book in books_data if book['author'] == author]
        return jsonify(filtered_books)
    else:
        return jsonify(books_data)


@app.route('/api/books/<int:id>', methods=['PUT'])
def handle_book(id):
    """
        Update a book with the given ID using the PUT method.

        Args:
            id (int): The ID of the book to be updated.

        Returns:
            str: A JSON response with the updated book if successful, or an error message and status code.

        HTTP Methods:
            - PUT

        Raises:
            - 400 Bad Request: If the request data is not valid JSON.
            - 404 Not Found: If the book with the specified ID is not found.
        """
    try:
        # Find the book with the given ID
        book = find_book_by_id(id)

        # If the book wasn't found, return a 404 error
        if book is None:
            return '', 404

        # Update the book with the new data
        new_data = request.get_json()
        if not new_data:
            return jsonify({"error": "Invalid request data"}), 400

        book.update(new_data)
        save_books(books_data)

        # Return the updated book
        return jsonify(book)
    except Exception as e:
        # Handle any unexpected errors and return a 500 Internal Server Error response
        return jsonify({"error": str(e)}), 500

@app.route('/api/books/<int:id>', methods=['DELETE'])
def delete_book(id):
    """
            Delete a book with the given ID using the DELETE method.

            Args:
                id (int): The ID of the book to be deleted.

            Returns:
                str: A JSON response with the deleted book if successful, or an error message and status code.

            HTTP Methods:
                - DELETE

            Raises:
                - 404 Not Found: If the book with the specified ID is not found.
            """
    try:

        # Find the book with the given ID
        book = find_book_by_id(id)

        # If the book wasn't found, return a 404 error
        if book is None:
            return '', 404

        # Remove the book from the list
        books_data.remove(book)
        save_books(books_data)

        # Return the deleted book
        return jsonify(book)
    except Exception as e:
        # Handle any unexpected errors and return a 500 Internal Server Error response
        return jsonify({"error": str(e)}), 500




if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    #app.run(debug=True)