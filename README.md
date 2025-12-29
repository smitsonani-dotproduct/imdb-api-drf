# IMDB Clone API

A Django REST Framework-based API for building a movie watchlist application inspired by IMDB. This project allows users to browse movies, manage their watchlists, and review content.

## Features

- **Movie Management**: Browse and manage a collection of movies
- **Streaming Platforms**: Associate movies with different streaming platforms
- **Watchlist System**: Users can add movies to their personal watchlists
- **Reviews & Ratings**: Users can write reviews and rate movies
- **RESTful API**: Complete REST API for all operations
- **User Authentication**: Review and watchlist ownership tied to user accounts

## Technology Stack

- **Backend**: Django 3.x+
- **API**: Django REST Framework
- **Database**: SQLite (default, configurable)
- **Python**: 3.8+

## Project Structure

```
imdb_clone/
├── imdb_clone/          # Project settings and configuration
├── watchlist_app/       # Main application
│   ├── api/             # API views, serializers, and URL routing
│   ├── migrations/      # Database migrations
│   ├── models.py        # Database models
│   ├── views.py         # View logic
│   └── admin.py         # Django admin configuration
├── manage.py            # Django management script
├── requirements.txt     # Project dependencies
└── db.sqlite3          # SQLite database
```

## Database Models

### Movie
- Title
- Description
- Release Date
- Streaming Platforms

### StreamPlatform
- Name
- About
- Website

### Watchlist
- Title
- Description
- Movie
- Streaming Platform
- Active status

### Review
- Created by User
- Rating
- Description
- Movie association
- Timestamps

## Getting Started

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd imdb_clone
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run migrations:
```bash
python manage.py migrate
```

5. Create a superuser (optional, for admin access):
```bash
python manage.py createsuperuser
```

6. Start the development server:
```bash
python manage.py runserver
```

The API will be available at `http://127.0.0.1:8000/`

## API Endpoints

### Movies
- `GET /api/movies/` - List all movies
- `GET /api/movies/{id}/` - Get movie details
- `POST /api/movies/` - Create a new movie (Admin only)
- `PUT /api/movies/{id}/` - Update a movie (Admin only)
- `DELETE /api/movies/{id}/` - Delete a movie (Admin only)

### Streaming Platforms
- `GET /api/platforms/` - List all platforms
- `GET /api/platforms/{id}/` - Get platform details
- `POST /api/platforms/` - Create a new platform (Admin only)

### Watchlist
- `GET /api/watchlist/` - Get user's watchlist
- `POST /api/watchlist/` - Add to watchlist
- `DELETE /api/watchlist/{id}/` - Remove from watchlist

### Reviews
- `GET /api/reviews/` - List all reviews
- `GET /api/reviews/{id}/` - Get review details
- `POST /api/reviews/` - Create a review
- `PUT /api/reviews/{id}/` - Update a review
- `DELETE /api/reviews/{id}/` - Delete a review

## Development

### Running Tests
```bash
python manage.py test
```

### Django Admin
Access the admin panel at `http://127.0.0.1:8000/admin/` using the superuser credentials.

## Future Enhancements

- [ ] Advanced filtering and search functionality
- [ ] Pagination for large datasets
- [ ] User profile management
- [ ] Social features (follow users, recommendations)
- [ ] Movie ratings aggregation
- [ ] Advanced permission system
- [ ] API documentation with Swagger/OpenAPI
