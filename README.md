# FastAPI AWS S3 Service

This project is a FastAPI-based backend service that integrates with AWS S3 to manage files. Users can authenticate, store their AWS credentials, and perform CRUD operations on S3 buckets and objects.

## Features

- User authentication using OAuth2 with password flow.
- Store and manage AWS S3 credentials securely.
- List, upload, download, and delete files in S3 buckets.
- Create and delete S3 buckets.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
  - [Authentication](#authentication)
  - [S3 Credentials](#s3-credentials)
  - [S3 Bucket Operations](#s3-bucket-operations)
  - [S3 Item Operations](#s3-item-operations)
- [API Endpoints](#api-endpoints)
- [Database Initialization](#database-initialization)
- [Notes](#notes)
- [License](#license)

## Installation

### Prerequisites

- Python 3.8+
- AWS Account with S3 permissions

### Setup

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/s3_bucket_manager.git
    cd s3_bucket_manager/s3_bucket_manager_backend
    ```

2. Create and activate a virtual environment:

    ```bash
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3. Install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Run the FastAPI application:

    ```bash
    uvicorn main:app --reload
    ```

    The application will be available at `http://127.0.0.1:8000`.

## Usage

### Authentication

1. **Sign Up**:
    ```bash
    curl -X POST "http://127.0.0.1:8000/auth/register" -H "Content-Type: application/json" -d '{"username": "testuser", "password": "testpassword"}'
    ```

2. **Login**:
    ```bash
    curl -X POST "http://127.0.0.1:8000/auth/login" -H "Content-Type: application/json" -d '{"username": "testuser", "password": "testpassword"}'
    ```

    The response will include a JWT token.

### S3 Credentials

```bash
curl -X PUT "http://127.0.0.1:8000/s3/credentials" -H "Authorization: Bearer <token>" -H "Content-Type: application/json" -d '{"access_key_id": "<your_access_key_id>", "secret_access_key": "<your_secret_access_key>"}'
```

### S3 Bucket Operations

**Create a Bucket**
```bash
curl -X POST "http://127.0.0.1:8000/s3/buckets/mybucket" -H "Authorization: Bearer <token>"
```

**Delete a Bucket**
```bash
curl -X DELETE "http://127.0.0.1:8000/s3/buckets/mybucket" -H "Authorization: Bearer <token>"
```

### S3 Item Operations

**List Items in a Bucket**
```bash
curl -X GET "http://127.0.0.1:8000/s3/buckets/mybucket/items" -H "Authorization: Bearer <token>"
```

**Upload a File**
```bash
curl -X POST "http://127.0.0.1:8000/s3/buckets/mybucket/items" -H "Authorization: Bearer <token>" -F "file=@/path/to/your/file"
```

**Download a File**
```bash
curl -X GET "http://127.0.0.1:8000/s3/buckets/mybucket/items/myfile.txt" -H "Authorization: Bearer <token>" -O
```

**Delete a File**
```bash
curl -X DELETE "http://127.0.0.1:8000/s3/buckets/mybucket/items/myfile.txt" -H "Authorization: Bearer <token>"
```

## API Endpoints

### Authentication

- **POST /auth/register**: Register a new user.
- **POST /auth/login**: Authenticate and get a token.

### S3 Credentials

- **PUT /s3/credentials**: Store AWS S3 credentials.

### S3 Bucket Operations

- **POST /s3/buckets/{bucket_name}**: Create a new S3 bucket.
- **DELETE /s3/buckets/{bucket_name}**: Delete an existing S3 bucket.

### S3 Item Operations

- **GET /s3/buckets/{bucket_name}/items**: List items in a bucket.
- **POST /s3/buckets/{bucket_name}/items**: Upload a file to a bucket.
- **DELETE /s3/buckets/{bucket_name}/items/{item_name}**: Delete a file from a bucket.
- **GET /s3/buckets/{bucket_name}/items/{item_name}**: Download a file from a bucket.

## Database Initialization

Ensure the database tables are created by running the application. The database file (`test.db`) will be created in the project directory.

## Notes

- Replace `<token>` with the JWT token obtained from the login endpoint.
- Replace `mybucket` with your bucket name and `myfile.txt` with your file name.
- The project uses SQLite for development. For production, consider using a more robust database like PostgreSQL or MySQL.
- For enabling foreign key constraints in SQLite, ensure `PRAGMA foreign_keys = ON` is set.

## License

This project is licensed under the MIT License.
