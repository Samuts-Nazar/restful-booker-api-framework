# Restful Booker API Framework

QA automation framework for [Restful Booker Platform](https://github.com/mwinteringham/restful-booker-platform) — a Dockerized microservices system for hotel booking management.

Built as a portfolio project demonstrating a Junior AQA Engineer skill set: manual test design, API test automation, and SQL-level database verification.

## Architecture

Three-layer approach:

1. **Manual Test Design** — exploratory testing of each service via Swagger/OpenAPI before automation (positive/negative scenarios, validation rules).
2. **API Automation** — `pytest` + `requests`, built around a generic `ApiClient` (Service Layer pattern, Dependency Injection, DRY `_request()` method).
3. **SQL Verification (DAO)** — direct database assertions via JDBC (`jaydebeapi`) against the H2 database, confirming API operations are reflected at the data layer.

## Tech Stack

- **Language:** Python 3.13
- **Test framework:** pytest
- **HTTP client:** requests
- **Test data:** Faker
- **Data validation:** Pydantic
- **Database:** H2 (via JDBC / jaydebeapi)
- **CI/CD:** GitHub Actions
- **Reporting:** Allure

## Project Structure
src/
api/            # ApiClient, BaseService, service classes (Auth, Booking, Room, Health)
database/       # DatabaseConnection, DAO layer
models/         # Pydantic response/request models
config/         # Settings (Pydantic + .env)
utils/          # Logging
tests/
auth/
booking/
room/
health/
database/
conftest.py       # shared fixtures (clients, services, payloads, db_cursor)

## Key Design Decisions

- **Service Layer + Dependency Injection** — each API service (`AuthService`, `BookingService`, `RoomService`, `HealthService`) inherits from `BaseService`, receiving a shared `ApiClient` instance.
- **DAO pattern** for database access — tests never touch the DB cursor directly; a `BookingDAO` class encapsulates SQL and returns clean Python dicts.
- **Request/response logging** — every API call is logged (method, URL, payload, status, response body) via a centralized logger in `ApiClient`.
- **Faker-based test data** — all payloads use randomized, unique data to avoid collisions (`409 Conflict` on duplicate room IDs, etc.).

## Setup & Running

1. Clone the repo and install dependencies:
```bash
   pip install -r requirements.txt
```
2. Copy `.env.example` to `.env` and adjust if needed (default values work out of the box for local RBP setup).
3. Start the Restful Booker Platform services via Docker Compose (see [RBP repo](https://github.com/mwinteringham/restful-booker-platform)).
4. Run tests:
```bash
   pytest
```

## Test Coverage

- Auth: login (positive/negative)
- Booking: create, read, full E2E flow with auth, database verification
- Room: full CRUD-adjacent coverage (create, read, list), negative/validation scenarios (parametrized)
- Health: service status check
- Database: connection smoke test, booking DAO verification