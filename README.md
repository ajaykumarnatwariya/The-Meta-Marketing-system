# Meta Marketing System API

A FastAPI-based API for managing metadata for Adsets, Groups, and Campaigns in the Meta Marketing system.

## Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/ajaykumarnatwariya/The-Meta-Marketing-system.git
   ```

2. **Install dependencies:**
   ```bash
   cd meta-marketing-system-api
   python -m venv venv
   venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Set up the database:**
   - Create a PostgreSQL database.
   - Run the SQL files in `sample_data/database_dump.sql` to populate the database with sample data.
   ```base
   psql -U <username> -d <database_name> -f sample_data/database_dump.sql
   ```

4. **Run the API:**
   ```bash
   uvicorn main:app --reload
   ```

5. **Access the API:**
   - API documentation: `http://localhost:8000/docs`
   - Sample data endpoints: `http://localhost:8000/adsets`, `http://localhost:8000/campaigns`, `http://localhost:8000/groups`

## Python Version

This project is built using Python 3.12.2.

## Structure

- **api/**: Contains modules for handling API routes.
- **database/**: Contains modules for defining database models and setting up the database connection.
- **sample_data/**: Contains SQL files with sample data to populate the database.
- **tests/**: Contains unit tests for testing API routes.

## Database

- PostgreSQL database is used to store metadata for Adsets, Groups, and Campaigns.
- Refer to the ER diagram in the `sample_data/ER_diagram_0*.png` file for the database schema.

## Documentation

- API routes are documented using FastAPI's automatic API documentation feature.
- Access the documentation at `http://localhost:8000/docs` when the API is running.

## Edge Cases

- Handle requests for non-existent campaigns or groups.
- Ensure that an adset can belong to multiple groups but only one campaign.
- Deal with invalid optimization goals or objectives.

## Contributing

- Fork the repository, make your changes, and submit a pull request.
- Report any issues or suggestions in the issues section.
