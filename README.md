# Django DRF Post Rating API

This project is a simple Django application utilizing Django REST Framework (DRF) to allow users to view a list of posts and rate them. Each post includes a title and a detailed text description. Users can assign a score between 0 and 5 to each post and update their score if needed.

## Features

- **Post List**: Retrieve a list of posts, each with the title, description, number of ratings, and an average score of ratings.
- **Post Detail**: View detailed information about a single post, including the user's own rating if they have rated it.
- **Rate Posts**: Authenticated users can rate a post or update their existing rating. Each user can only have one rating per post.

## Setup

To get this project up and running, follow these steps:

1. Clone the repository:


git clone https://github.com/M0d3v1/bitpin-django-task.git
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

Usage
Once the server is running, the API will be available at http://127.0.0.1:8000/.

To view the list of posts: GET /posts/
To view the detail of a single post: GET /posts/{post_id}/
To rate a post: POST /ratings/ with payload {"post": post_id, "score": score}
To update a rating: PUT /ratings/{rating_id}/ with payload {"score": new_score}
Authentication
This API requires users to be authenticated to rate posts. Use Django's authentication system to create users and manage sessions.

Testing
Test the API using tools like Postman or curl to ensure all endpoints are functioning as expected.

Deployment
When deploying to a production environment, be sure to set DEBUG = False in your settings and configure your database and other services securely.
