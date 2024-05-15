# Task Manager App Backend With Django

This project is the backend for a task manager app implemented with Django Rest Framework, Djoser for authentication, among others. 

## Table of Contents
- [Features](#features)
- [Project Setup](#getting-started)
- [Contribution](#contributing)

## Features

- User Account Registration
- User Account Login
- User Account Logout
- Github and Google OAuth2 support
- HttpOnly cookie authentication.
- CRUD implementations for tasks
- Postgres for database

## Getting Started
Follow the following instruction to setup this project locally on your device

#### 1. To begin first clone this project 
```bash
  git clone https://github.com/ktawiah/Task-Manager-App-Backend.git
```

#### 2. Create a virtual environment
``` bash
  python3 -m venv venv
```

#### 3. Install project dependencies
```bash
  pip install -r requirements.txt
```
#### 4. Setup setup environment variables

```
DJANGO_SECRET_KEY=""
DEBUG="True"
DEVELOPMENT_MODE="True"
AUTH_COOKIE_SECURE="True"
SOCIAL_AUTH_REDIRECT_URIS=""
SOCIAL_AUTH_GITHUB_KEY=""
SOCIAL_AUTH_GITHUB_SECRET=""
CORS_ALLOWED_ORIGINS=""
GOOGLE_OAUTH2_CLIENT_ID=""
GOOGLE_OAUTH2_CLIENT_SECRET=""

# PostgresDB config
DATABASE_NAME=""
DATABASE_USER=""
DATABASE_PASSWORD=""
DATABASE_HOST=""
DATABASE_PORT=""
```


#### 5. Run migrations
```bash
  python manage.py makemigrations
  python manage.py migrate
```
#### 6. Start the backend development server
```bash
  python manage.py runserver
```


## Contributing
Contributions to this project are welcomed! If you have any issues with the project or have some ideas for enhancements to contribute, please don't hesitate to open an issue or submit a pull request. Your input is much appreciated.
