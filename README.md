# BeesKnees-BE solo project made by Luwam G. https://kneesrehab.netlify.app/

BeesKnees is a Django-based REST API for managing exercise information. It allows users to create, read, update, and delete exercise records.

# BeesKnees Exercise API

BeesKnees is a Django-based REST API for managing exercise information. It allows users to create, read, update, and delete exercise records.

## Features

- RESTful API for exercise management
- CRUD operations on exercise records
- PostgreSQL database integration
- Cross-Origin Resource Sharing (CORS) support

## Technical Stack

- Django 4.2.3
- Django REST Framework
- PostgreSQL
- dj-database-url for database configuration
- python-dotenv for environment variable management

## API Endpoints

- `GET /exercises/`: Retrieve all exercises
- `POST /exercises/`: Create a new exercise
- `GET /exercises/<id>`: Retrieve a specific exercise
- `PUT /exercises/<id>`: Update a specific exercise
- `DELETE /exercises/<id>`: Delete a specific exercise

## Models

### Exercise
- `name`: CharField (max length: 200)
- `description`: CharField (max length: 500)
- `image`: URLField (max length: 200)

### User
- `name`: CharField (max length: 30)
- `email`: EmailField

### Entry
- `date`: CharField (max length: 20)
- `sets`: CharField (max length: 20)
- `reps_or_mins`: CharField (max length: 20)
- `user`: ForeignKey to User model (with CASCADE on delete, can be null)
- `exercise`: ForeignKey to Exercise model (with CASCADE on delete)

Relationships:
- A User can have multiple Entries (one-to-many relationship)
- An Exercise can be associated with multiple Entries (one-to-many relationship)
