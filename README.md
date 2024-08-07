# Book Recommendation Project

## Overview

The Book Recommendation Project is a Django-based web application that integrates with the Google Books API. The app allows users to fetch and display book information and manage book recommendations.

## Features

- Fetch books from the Google Books API.
- Display a list of books with details such as title, author, description, and cover image.
- Add and manage book recommendations.

## Requirements

- Python 3.8 or higher
- Django 5.0.7
- Django REST framework
- Requests library

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/toshiladitya/BookRecommandation.git
   cd book_recommendation

2. Create a Virtual Environment:

     ```bash
       python -m venv venv

3. Activate the Virtual Environment:

   - On Windows:

         venv\Scripts\activate

   - On macOS/Linux:

         source venv/bin/activate

4. Install Dependencies:

       pip install -r requirements.txt

5. Apply Migrations:

       python manage.py migrate
6. Run the Development Server:

       python manage.py runserver

7. You can now access the application at http://127.0.0.1:8000/

       http://127.0.0.1:8000/ 


## API Endpoints
- Books

        GET /api/books/

- Lists all books in the database.

- Response:

      [
       {
        "id": 1,
        "title": "Book Title",
        "author": "Author Name",
        "description": "Book description...",
        "cover_image": "http://example.com/image.jpg",
         "rating": 4.5
       },
       ...
       ]
    POST /api/books/fetch_books/

- Fetches books from the Google Books API and adds them to the database. Requires a JSON payload with the key "query" for search terms.

- Request:

      {
      "query": "Python programming"
      }
 Response:

    [
     {
      "id": 1,
      "title": "Python Programming",
      "author": "John Doe",
      "description": "A comprehensive guide to Python programming...",
      "cover_image": "http://example.com/image.jpg",
      "rating": 4.8
     },
     ...
    ]
# Recommendations

 GET /api/recommendations/

# Lists all recommendations.

 Response:

     [
      {
      "id": 1,
      "book": 1,
      "user": "Alice",
      "comment": "Great book for learning Python!",
      "likes": 10
     },
    ...
    ]

POST /api/recommendations/

# Creates a new recommendation. 
## Requires a JSON payload with details of the recommendation.

- Request:

      {
       "book": 1,
       "user": "Alice",
       "comment": "Great book for learning Python!",
       "likes": 10
      }
- Response:

       {
         "id": 1,
         "book": 1,
         "user": "Alice",
         "comment": "Great book for learning Python!",
         "likes": 10
        }
          
## HTML Template
- The index.html file displays the list of books fetched from the API.
 It uses JavaScript to fetch data from the

        /api/books/

 endpoint and dynamically updates the page content.


## Acknowledgments
- Google Books API
- Django
- Django REST framework
- Requests Library
