# ELT-docker-sql-azure

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-12%2B-blue?logo=postgresql)
![Docker](https://img.shields.io/badge/Docker-Ready-blue?logo=docker)

This project demonstrates a simple ETL pipeline using Python, Docker, and PostgreSQL.

## Overview
- Pulls a dataset of the top 1000 YouTube videos from a public URL
- Processes the data using pandas
- Loads the data into a PostgreSQL database running inside a Docker container
- Uses Azure Data Studio optionally for database inspection

## How it Works
1. **Configuration:**
   - Database credentials are stored in `postgres_creds.json` for security and flexibility.
2. **Database Creation:**
   - The script automatically checks for the target database (e.g., `kaggle`) and creates it if it does not exist.
3. **Data Loading:**
   - The script downloads the CSV data and loads it into the specified PostgreSQL database table.

## Setup Instructions

### 1. Clone the Repository
```sh
git clone <https://github.com/AhmedFrz/ELT-docker-sql-azure>
cd ELT-docker-sql-azure
```

### 2. Configure Database Credentials
Edit `postgres_creds.json` to match your PostgreSQL setup:
```json
{
  "dbname": "your_db_name",
  "user": "your_username",
  "password": "your_password",
  "host": "your_host",
  "port": "your_port"
}
```

### 3. Install Dependencies
```sh
pip install -r requirements.txt
```

### 4. Start PostgreSQL (Docker Example)
If you want to use Docker, you can use the provided `docker-compose.yml`:
```sh
docker-compose up -d
```

### 5. Run the ETL Script
```sh
python elt.py
```

## Notes
- The script will create the target database if it does not exist.
- Data is loaded into the `kaggle_1000_youtube_videos` table.
- You can inspect the database using Azure Data Studio or any other PostgreSQL client.

## Requirements
- Python 3.8+
- Docker (optional, for local PostgreSQL)
- Azure Data Studio (optional, for inspection)

---

Feel free to fork, modify, and use this project for your own ETL/data engineering learning!
