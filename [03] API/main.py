"""
The Challenge: The "Lumina" Library API
Objective: Develop a production-ready RESTful API for a digital library system.

The Requirements:

Endpoints:

Implement a GET endpoint that returns a list of all books in the system.

Implement a POST endpoint that accepts a JSON object (title, author, and year) and stores it in a persistent SQLite database.

Validation: Ensure that the API returns a 422 Unprocessable Entity error if a user tries to add a book without a title.

Persistence: Data must survive a server restart (i.e., use a database file, not a Python list).

Documentation: The API must be self-documenting (FastAPI does this automatically via Swagger UI).

Deployment (Stretch Goal): Host the finished API on a platform like Render, Railway, or Fly.io.
"""