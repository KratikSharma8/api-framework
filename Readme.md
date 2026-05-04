# API Test Framework

Automated API tests built with Python and pytest, testing a 
FastAPI backend with full CRUD coverage.

## Project Structure
api-framework/
  tests/         - pytest test files
  conftest.py    - shared fixtures
  my_api.py      - local FastAPI server
  requirements.txt

## Setup
pip install -r requirements.txt

## Start the API
python -m uvicorn my_api:app --reload

## Run Tests
python -m pytest tests/ -v

## Run with HTML Report
python -m pytest tests/ -v --html=report.html

## What's tested
- GET single user (200)
- GET all users (200)
- GET non-existent user (404)
- POST create user (201)
- Boundary tests (user ID 0, negative ID)
- Field validation (email format, required fields, valid roles)

## Generate HTML Report
python -m pytest tests/ -v --html=report.html --self-contained-html
Open report.html in your browser to view results.