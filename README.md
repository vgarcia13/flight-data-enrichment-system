# FlyFlat Flight Data Enrichment System

A system for managing, enriching, and visualizing flight data. It features both Django and FastAPI backends, background task processing with Celery, and a dashboard for monitoring. The project is containerized with Docker and uses SQLite for development.

## Technologies Used

- **Python 3.10+**
- **Django** (web framework, dashboard, admin)
- **Django REST Framework** (API for Django)
- **FastAPI** (async API)
- **Celery** (background task processing)
- **SQLite** (development database)
- **Redis** (Celery broker and result backend)
- **Poetry** (Python dependency management)
- **Docker & Docker Compose** (containerization)

## Prerequisites

- **Docker** and **Docker Compose** installed ([Install Docker](https://docs.docker.com/get-docker/))
- **Git** installed ([Install Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git))
- (Optional) **Poetry** for Python dependency management ([Install Poetry](https://python-poetry.org/docs/#installation))

## Local Setup

1. **Clone the repository:**
   ```sh
   git clone https://github.com/vgarcia13/ff-flight-data-enrichment-system.git
   cd ff-flight-data-enrichment-system
   
2. **Copy and configure environment variables:**
   ```sh
   cp .env.example .env
   ```
   Edit `.env` to set your environment variables.


3. **Build and start the containers:**
    ```sh
    docker compose up --build
    ```
   
4. **Access the applications:**
   - Flight API Browser: [http://localhost:8000/api/](http://localhost:8000/api/)
   - FastAPI: [http://localhost:8080/docs](http://localhost:8080/docs)
   - Dashboard (Flights): [http://localhost:8000/dashboard/flights/](http://localhost:8000/dashboard/flights/)
   - Dashboard (Completed Tasks): [http://localhost:8000/dashboard/tasks/](http://localhost:8000/dashboard/tasks/)

## Testing the API

#### Using Postman

- Import the API endpoints (Django: /api/, FastAPI: /docs) into Postman.
- For Django endpoints, use http://localhost:8000/api/.
- For FastAPI endpoints, use http://localhost:8080/. 
- Send requests (e.g., POST /enrich-flight, GET /task-status/{task_id}) and inspect responses.

#### Using Django REST Framework API Browser

- Open http://localhost:8000/api/ in your browser. 
- Browse available endpoints, submit requests, and view responses interactively.

## Author

**Victor Garcia** <[https://github.com/vgarcia13](https://github.com/vgarcia13)>