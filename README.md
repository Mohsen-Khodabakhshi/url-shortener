# FastAPI URL Shortener

A simple but fast URL shortener built using FastAPI, PostgreSQL, and Redis.

<p align="center">
    <img src="https://raw.githubusercontent.com/Mohsen-Khodabakhshi/url-shortener/main/assets/system-design.jpg">
</p>

## Load/Stress Test Result
System info:
- Memory: 16GB
- CPU: 8 cores

Redirect Result:
- Read from Redis(Cache): RPS(request per second) ≅ 900
- Read from Postgresql: RPS(request per second) ≅ 400
- AVG response time ≅ 200ms

## Installation

To run the project locally, follow these steps:

### Option 1:
#### Prerequisites
- Docker
- Docker Compose
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/url-shortener.git
   cd url-shortener

2. Setup configuration file:
    ```bash
   cp src/.env.sample src/.env
3. Run using docker-compose:
    ```bash
    docker-compose run --build

### Option 2:
#### Prerequisites
- Python 3.10.12
- Poetry 1.8.3
- Postgresql
- Redis
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/url-shortener.git
   cd url-shortener/src
2. Setup configuration file:
    ```bash
    cp .env.sample .env
3. Install dependencies:
    ```bash
    poetry install
4. Database migrations:
    ```bash
    poetry run alembic upgrade head
5. Run project:
    ```bash
   poetry run uvicorn core.main:app --host 127.0.0.1 --port 8000

## Contributing
Contributions are welcome! To contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch
3. Make your changes.
4. Install pre-commit hooks:
    ```bash
   pip install pre-commit
   pre-commit install
5. Commit your changes
6. Push to your branch
7. Submit a pull request.
