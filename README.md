
# fastapi-crud

# FastAPI MongoDB CRUD

This project provides an example of developing a simple CRUD (Create, Read, Update, Delete) application using FastAPI and MongoDB. This application uses MongoDB for database operations and handles HTTP requests with FastAPI.

## Installation

### Installation on Local

Install requirements using pip
```bash
pip3 install -r requirements.txt
```

Start the project using uvicorn
```bash
python3 -m uvicorn main:app --host 0.0.0.0 --port 8000
```


### Installation on Container
Build the Dockerfile
```bash
docker build -t image-name .
```
Start a Container
```bash
docker run -d -p 8000:8000 --name container-name image-name
```

## Test
start the test file using the command
```bash
python3 -m pytest test.py
```
