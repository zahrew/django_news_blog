# News Blog API

This is a backend project for a News Blog application, built using Django and Django REST framework. It provides APIs for managing blog posts, user authentication, and more.

## About the Project

The News Blog API project is designed to serve as the backend for a news blogging platform. It allows users to create, read, update, and delete blog posts. Additionally, it provides user authentication using JWT (JSON Web Tokens) for secure access to the API endpoints.

## Features
* User Authentication: Secure user login and token generation using JWT.
* Blog Management: CRUD (Create, Read, Update, Delete) operations for blog posts.
* Admin Panel: A web-based interface for managing the blog content and users.
* API Endpoints: A set of RESTful API endpoints for interacting with the blog posts and user authentication.

## Getting Started


### Installing
* Python 3.8 or higher
* Git
* Virtualenv

### Steps
#### 1. Clone the repository:

```
git clone https://github.com/zahrew/news_api.git
cd news_api
```
#### 2. Create a virtual environment:

```
python -m venv venv
```
#### 3. Activate the virtual environment:

* On Windows:

```
venv\Scripts\activate
```
* On macOS/Linux:

```
source venv/bin/activate
```
#### 4. Install the dependencies:

```
pip install -r requirements.txt
```
#### 5. Apply migrations:


```
python manage.py migrate
```
#### 6. Create a superuser for accessing the admin site:

```
python manage.py createsuperuser
```
#### 7. Run the development server:

```
python manage.py runserver
```
#### 8. Access the application at http://127.0.0.1:8000/.


## Usage

* To access the admin panel, navigate to http://127.0.0.1:8000/admin/ and log in with the superuser credentials.
* To use the API endpoints, you can use tools like Postman or curl to interact with the APIs.

## API Endpoints


### Authentication
* Login

```
POST /api-token-auth/
```
### Blog Posts
* List all blog posts

```
GET /api/blogs/
```
* Create a new blog post

```
POST /api/blogs/
```
* Retrieve a single blog post

```
GET /api/blogs/<id>/
```

* Update a blog post

```
PUT /api/blogs/<id>/
```
* Delete a blog post
```
DELETE /api/blogs/<id>/
```


## Technologies

* Django: The web framework used for this project.
* Django REST Framework: For building the API endpoints.
* SQLite: The default database used for development.


## License

This project is licensed under the [NAME HERE] License - see the LICENSE.md file for details


